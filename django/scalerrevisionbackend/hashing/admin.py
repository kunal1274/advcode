from django.contrib import admin
from .models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list = ('id','name', 'mobile', 'active')

    admin.site.register(Customer)

