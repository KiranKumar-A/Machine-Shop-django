from django.contrib import admin

# Register your models here.






from lathe_machine.models import lathe_machine,Customer,Country,Tool
admin.site.register(lathe_machine)
admin.site.register(Customer)



admin.site.register(Country)
admin.site.register(Tool)