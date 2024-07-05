from django.contrib import admin
from .models import Account


# admin.site.register(Account)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass
    list_display = ['account_number', 'account_type', 'balance']
    list_per_page = 10
    # search_fields = ['account_number', 'first_name', 'last_name']
    list_editable = ['account_type', 'balance']
    # sortable_by = ['account_number', 'first_name', 'last_name', 'account_type']


