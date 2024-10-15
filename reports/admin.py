from django.contrib import admin
from .models import psp_customer_info, psp_transac_categorization_info
# Register your models here.
admin.site.register(psp_customer_info)
admin.site.register(psp_transac_categorization_info)