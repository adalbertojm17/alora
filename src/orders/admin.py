from django.contrib import admin
from  .models import Service, Order, Order_Adress


admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Order_Adress)

