from django.contrib import admin
from .models import MobilePspCustomerInfo, MobilePspTransactionCategorization
# Register your models here.
admin.site.register(MobilePspCustomerInfo)
admin.site.register(MobilePspTransactionCategorization)