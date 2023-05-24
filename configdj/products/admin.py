from django.contrib import admin
from products.models import Users, Firma, Computer, Smartphone, Smartwatch, Accessory, Otherproducts
from django.contrib.auth.models import Group

admin.site.unregister(Group)
    

admin.site.register(Users)
admin.site.register(Firma)
admin.site.register(Computer)
admin.site.register(Smartphone)
admin.site.register(Smartwatch)
admin.site.register(Accessory)
admin.site.register(Otherproducts)