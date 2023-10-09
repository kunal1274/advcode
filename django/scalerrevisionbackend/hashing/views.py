from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Customer
from .serializers import CustomerSerializer

@api_view(['GET', 'POST','DELETE'])
def customers_list(request):
    """
    List customers, or create a new customer.

    Methods:
    GET -- Retrieve a paginated list of customers.
    POST -- Create a new customer.

    Returns:
    - If GET: A paginated list of customers along with pagination information.
    - If POST: The created customer's details on success, or error details on failure.
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        customers = Customer.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(customers, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = CustomerSerializer(data, context={'request': request}, many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({
            'data': serializer.data,
            'count': paginator.count,
            'numpages': paginator.num_pages,
            'nextlink': f'/api/customers/?page={nextPage}',
            'prevlink': f'/api/customers/?page={previousPage}'
        })

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Customer.objects.all().delete()
        return Response(
            {'message' : f'{count[0]} customers were deleted successfully'},
            status = status.HTTP_204_NO_CONTENT
        )


@api_view(['GET', 'PUT', 'DELETE'])
def customers_detail(request, pk):
    """
    Retrieve, update or delete a customer by id/pk.

    Methods:
    GET -- Retrieve customer details by id/pk.
    PUT -- Update customer details by id/pk.
    DELETE -- Delete customer by id/pk.

    Parameters:
    - pk (int): The primary key of the customer.

    Returns:
    - If GET: The details of the retrieved customer.
    - If PUT: The updated customer details on success, or error details on failure.
    - If DELETE: No content on successful deletion, or error details on failure.
    """
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Retrieve and serialize customer details for response
        serializer = CustomerSerializer(customer, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Update customer details based on provided data
        serializer = CustomerSerializer(customer, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete the customer instance
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def customer_detail_custom(request,customer_id):
    params={
        'd44_1_findfreq':'creditlimit',
        'sort':'id',
        'top':'',
        'bottom':'',
    }
    try:
        customer = Customer.objects.get(pk = customer_id)
    except Customer.DoesNotExist:
        response_data = {
           'error_k':'Customer Not Found',
           'status_k':"Error",
        }
        return Response(response_data,status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CustomerSerializer(customer,context={'request_k': request})
        response_data = {
            'customer_info_k':serializer.data,
            'status_k':"Success",
            
        }
        return Response(response_data)
    


@api_view(['GET'])
def customer_detail_custom_2(request, customer_id):
    if request.method == 'GET':
        try:
            customer = Customer.objects.get(pk=customer_id)
        except Customer.DoesNotExist:
            response_data = {
                'error_k': 'Customer Not Found',
                'status_k': "Error",
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        # Check if 'find_frequency' is in the query parameters and get the field name
        find_frequency_field = request.GET.get('find_frequency')
        if find_frequency_field:
            # Get the frequency of the specified field
            field_freq = Customer.objects.values(find_frequency_field).annotate(frequency=Count(find_frequency_field))
            frequency_dict = {item[find_frequency_field]: item['frequency'] for item in field_freq}

            serializer = CustomerSerializer(customer, context={'request_k': request})
            response_data = {
                'customer_info_k': serializer.data,
                #f'{find_frequency_field}_frequency': frequency_dict,  # Include field frequency data
                'frequency_k': frequency_dict,  # Include field frequency data
                'status_k': "Success",
            }
            print(response_data)
            return Response(response_data)

        serializer = CustomerSerializer(customer, context={'request_k': request})
        response_data = {
            'customer_info_k': serializer.data,
            'status_k': "Success",
        }
        return Response(response_data)

def dj_find_frequency(param_list):
    hm={}
    n=len(param_list)
    for i in range(n):
        if param_list[i] in hm:
            # 2nd time or more found 
            hm[param_list[i]] += 1
        else:
            hm[param_list[i]] = 1
    return hm

def dj_find_count_distinct(p_jsondata,p_key):
    hs = set()
    for i in p_jsondata:
        hs.add(i[p_key])
    return len(hs)

def dj_check_distinct(p_jsondata,p_key):
    hs=set()
    for i in p_jsondata:
        hs.add(i[p_key])
    if len(hs) == len(p_jsondata):
        return True
    else:
        return False


@api_view(['GET'])
def customer_list_custom(request):
    name_start = request.GET.get('name_start')
    find_frequency_field = request.GET.get('find_frequency')
        # Apply the filter if name_start parameter is provided
    c = Customer.objects.all() # all customers list 
    credit_list=[]
    for i in c:
        credit_list.append(str(i.creditlimit))# adding credit limit of each customers in the list.
    count_distinct = dj_find_count_distinct(c.values('creditlimit'),'creditlimit')
    check_distinct_names = dj_check_distinct(c.values('name'),'name')
    check_distinct_creditlimit = dj_check_distinct(c.values('creditlimit'),'creditlimit')

        
    try:
        #if find_frequency_field =='creditlimit' and name_start:
            
        if find_frequency_field == 'creditlimit':
            customers = Customer.objects.all()
            serializer = CustomerSerializer(customers,context={'request_k': request}, many=True)
            frequency_data = dj_find_frequency(credit_list)
            response_data = {
                'customer_info_k': serializer.data,
                'count_distinct_k':[count_distinct,c.values('creditlimit')],
                'frequency_k':frequency_data,
                'find_frequency_k':True,
                'status_k': "Success",
            }
            return Response(response_data, status=status.HTTP_200_OK)
        if name_start: 
            customers = Customer.objects.filter(name__istartswith=name_start)
            serializer = CustomerSerializer(customers,context={'request_k': request}, many=True)
            
            response_data = {
                'customer_info_k': serializer.data,
                'count_distinct_k':[count_distinct,c.values('name')],
                'name_start_k':True,
                'status_k': "Success",
            }
            return Response(response_data, status=status.HTTP_200_OK)
        
        else:
            customers = Customer.objects.all()
            serializer = CustomerSerializer(customers, context={'request_k': request}, many=True)
            response_data = {
                'customer_info_k': serializer.data,
                'count_distinct_k':[count_distinct,c.values()],
                'name_start_k':False,
                'find_frequency_k':False,
                'status_k': "Success",
                'd44_hashing_q3_k':[
                    {'question':"Check whether names and credit limits are distinct or not in customer master"},
                    {'answer':{
                        'names':check_distinct_names,
                        'creditlimits':check_distinct_creditlimit
                              }       
                    }]
            }
            return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        error_response_data = {
            'error_k': str(e),  # Provide an appropriate error message
            'status_k': "Error",
        }
        return Response(error_response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
def customer_create_custom(request):
    if request.method == 'POST':
        try:
            serializer = CustomerSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                response_data = {
                    'customer_info_k': serializer.data,
                    'status_k': "Success",
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                response_data = {
                    'error_k': serializer.errors,
                    'status_k': "Error",
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            error_response_data = {
                'error_k': str(e),  # Provide an appropriate error message
                'status_k': "Error",
            }
            return Response(error_response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

@api_view(['PUT'])
def customer_update_custom(request, customer_id):
    try:
        customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        response_data = {
            'error_k': 'Customer Not Found',
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'customer_info_k': serializer.data,
                'status_k': "Success",
            }
            return Response(response_data)
        else:
            response_data = {
                'error_k': serializer.errors,
                'status_k': "Error",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE'])
def customer_delete_custom(request, customer_id):
    try:
        customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        response_data = {
            'error_k': 'Customer Not Found',
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        deleted_customer_data = {
            'id_k': customer.id,
            'name_k': customer.name,
        }
        customer.delete()
        response_data = {
            'status_k': "Success",
            'deleted_customer_info_k': deleted_customer_data,
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)

    