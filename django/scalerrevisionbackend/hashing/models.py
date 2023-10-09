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
    creditlimit = models.DecimalField(
        verbose_name="Credit Limit",
        max_digits=10, 
        decimal_places=3, 
        default=0.000,
        help_text="Enter the credit limit of the customer (in lacs Rupees)"
        )
    mobile = models.CharField(
        verbose_name="Mobile No.",
        max_length=13,
        help_text="Enter the Mobile No"
    )
    whatsapp = models.CharField(
        verbose_name="Whatsapp No.",
        max_length=13,
        null=True,
        blank=True,
        help_text="Enter the WhatsApp mobile No"
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

    
