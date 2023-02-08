from django.contrib import admin
from.models import Category,Product,Customer,Order

# Register your models here.
admin.site.register(Category)
# admin.site.register(Product)

# admin.site.register(Customer)
# admin.site.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','name','purchage_price','sell_price','discount')
    list_filter=('category',)
admin.site.register(Product,ProductAdmin)


class CustomerAdmin(admin.ModelAdmin):
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    list_display=(full_name,'cell')
    list_filter=('email',)

admin.site.register(Customer,CustomerAdmin)


class orderAdmin(admin.ModelAdmin):
    list_display=('id','product','customer','quantity','delevery_address','date','status')
admin.site.register(Order,orderAdmin)
