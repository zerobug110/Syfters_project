from django.contrib import admin

from products.views import portfolio

# Register your models here.

from . models import Product, New, About, LatestNew
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','created_at')
    list_links = ('id', 'name')
    list_filter = ('name','price','created_at')
    search_fields = ('name','price')
    ordering =('name','price','created_at')

class NewAdmin(admin.ModelAdmin):
    list_display=('title','time')
    list_filter=('title','time')
    search_fields = ('title','time')


admin.site.register(Product, ProductAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(LatestNew)
admin.site.register(About)