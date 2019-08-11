from django.contrib import admin

# Register your models here.
from lathe_machine.models import lathe_machine,Customer
admin.site.register(lathe_machine)
admin.site.register(Customer)
