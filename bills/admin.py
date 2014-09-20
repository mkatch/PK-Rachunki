from django.contrib import admin
from bills.models import Bill, BillEntry

admin.site.register(Bill)
admin.site.register(BillEntry)