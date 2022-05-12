from django.contrib import admin
from .models import Transactions,Packages,Investments,Bank
# Register your models here.
admin.site.register(Transactions)
admin.site.register(Packages)
admin.site.register(Investments)
admin.site.register(Bank)