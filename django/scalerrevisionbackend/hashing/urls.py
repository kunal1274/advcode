#from django.conf.urls import url 
from django.urls import include, re_path
from hashing import views 
 
urlpatterns = [ 
    # customer
    #re_path(r'^customers$', views.customer_list),
    re_path(r'^customers$', views.customer_list_custom),
    re_path(r'^customers/create$', views.customer_create_custom),
    re_path(r'^customers/(?P<customer_id>[0-9]+)$', views.customer_detail_custom),
    re_path(r'^customers/(?P<customer_id>[0-9]+)/(?P<freq_field>\w+)$', views.customer_detail_custom_2),
    re_path(r'^customers/update/(?P<customer_id>[0-9]+)$', views.customer_update_custom),
    re_path(r'^customers/delete/(?P<customer_id>[0-9]+)$', views.customer_delete_custom),

    # hashing queries
    #re_path(r'^queries$', views.hashing_list),
]