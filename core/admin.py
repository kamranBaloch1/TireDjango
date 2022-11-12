from django.contrib import admin
from .models import Product,Addres,OrderPlaced,Cart,Contact,ProductReview

# Register your models here.

admin.site.register(Product)
admin.site.register(Addres)
admin.site.register(OrderPlaced)
admin.site.register(Cart)
admin.site.register(Contact)
admin.site.register(ProductReview)
