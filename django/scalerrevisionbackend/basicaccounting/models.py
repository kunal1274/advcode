from django.db import models

# Create your models here.
class Task(models.Model): # models is module and Model is a class 
    STATUS_CHOICES = (
        ('done', 'Done'),
        ('wip', 'WIP'),
        ('nys', 'Not Yet Started'),
        ('onHold', 'On Hold'),
        ('later', 'Later'),
    )
    name = models.CharField(
        verbose_name="Task Name",
        max_length=500,
        unique=True,
        help_text="Enter the name of the Task."
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        help_text='Status of the Task'
    )

    created_at = models.DateTimeField(
        verbose_name="Created At",
        auto_now_add=True,
        help_text="Date and time when the task was created."
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated At",
        auto_now=True,
        help_text="Date and time when the task was last updated."
    )

    def __str__(self):
        return f"{self.name} - {self.status}"
    

from django.db import models
#from django.contrib.auth import get_user_model

class Customer(models.Model):
    """
    Represents a customer entity in the database.

    Fields:
    - name (CharField): Customer name.Should be unique.
    - mobile (CharField): Mobile number of the customer.
    - whatsapp (CharField): WhatsApp mobile number of the customer.
    - address (TextField): Address of the customer.
    - altaddress (TextField): Alternate address of the customer.
    - created_at (DateTimeField): Date and time when the customer was created.
    - updated_at (DateTimeField): Date and time when the customer was last updated.

    Example:
    customer = Customer(
        name="John Doe",
        mobile="1234567890",
        whatsapp="9876543210",
        address="123 Main St, City",
        altaddress="456 Secondary St, City"
    )
    customer.save()
    """

    name = models.CharField(
        verbose_name="Customer Name",
        max_length=250,
        unique=True,
        help_text="Enter the name of the customer."
    )
    mobile = models.CharField(
        verbose_name="Mobile No.",
        max_length=13,
        help_text="Enter the Mobile No"
    )
    address = models.TextField(
        verbose_name="Address",
        help_text="Enter the address of the customer."
    )
    altaddress = models.TextField(
        verbose_name="Alternate Address",
        blank=True,
        null=True,
        help_text="Enter the alternate address of the customer."
    )
    active = models.BooleanField(
        verbose_name="Is Active",
        default=True
        )
    created_at = models.DateTimeField(
        verbose_name="Created At",
        auto_now_add=True,
        help_text="Date and time when the customer was created."
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated At",
        auto_now=True,
        help_text="Date and time when the customer was last updated."
    )

    def __str__(self):
        """
        Returns a string representation of the customer.
        """
        return f"{self.name} - {self.mobile} - {self.address}"
    

class Vendor(models.Model):
    """
    Represents a Vendor entity in the database.
    """

    name = models.CharField(
        verbose_name="Vendor Name",
        max_length=250,
        unique=True,
        help_text="Enter the name of the vendor."
    )
    mobile = models.CharField(
        verbose_name="Mobile No.",
        max_length=13,
        help_text="Enter the Mobile No"
    )
    address = models.TextField(
        verbose_name="Address",
        help_text="Enter the address of the vendor."
    )
    altaddress = models.TextField(
        verbose_name="Alternate Address",
        blank=True,
        null=True,
        help_text="Enter the alternate address of the vendor."
    )
    active = models.BooleanField(
        verbose_name="Is Active",
        default=True
        )
    created_at = models.DateTimeField(
        verbose_name="Created At",
        auto_now_add=True,
        help_text="Date and time when the vendor was created."
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated At",
        auto_now=True,
        help_text="Date and time when the vendor was last updated."
    )

    def __str__(self):
        """
        Returns a string representation of the Vendor.
        """
        return f"{self.name} - {self.mobile} - {self.address}"
    

class LedgerAccount(models.Model):
    """
    Represents a Vendor entity in the database.
    """

    code = models.CharField(
        verbose_name="Account Code",
        max_length=60,
        unique=True,
        help_text="Enter the code of the account."
    )
    name = models.CharField(
        verbose_name="Vendor Name",
        max_length=250,
        unique=True,
        help_text="Enter the name of the Ledger."
    )
    
    active = models.BooleanField(
        verbose_name="Is Active",
        default=True
        )
    created_at = models.DateTimeField(
        verbose_name="Created At",
        auto_now_add=True,
        help_text="Date and time when was created."
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated At",
        auto_now=True,
        help_text="Date and time when was last updated."
    )

    def __str__(self):
        """
        Returns a string representation of the Vendor.
        """
        return f"{self.code} - {self.name}"
    
class Item(models.Model):
    """
    Represents a Vendor entity in the database.
    """
    TYPE_CHOICES = (
    ('item', 'Item'),
    ('service', 'Service'),
    )

    code = models.CharField(
        verbose_name="Vendor Name",
        max_length=60,
        unique=True,
        help_text="Enter the code of the account."
    )
    name = models.CharField(
        verbose_name="Vendor Name",
        max_length=250,
        unique=True,
        help_text="Enter the name of the Ledger."
    )
    
    active = models.BooleanField(
        verbose_name="Is Active",
        default=True
        )
    created_at = models.DateTimeField(
        verbose_name="Created At",
        auto_now_add=True,
        help_text="Date and time when was created."
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated At",
        auto_now=True,
        help_text="Date and time when was last updated."
    )

    def __str__(self):
        """
        Returns a string representation of the Vendor.
        """
        return f"{self.code} - {self.name}"


    
