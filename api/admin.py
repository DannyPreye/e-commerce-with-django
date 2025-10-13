from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser, Category, Product, Cart, CartItem

# Register your models here.
# admin.site.register(CustomerUser)
# admin.site.register(Category)
# admin.site.register(Product)

class CustomerUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active']

admin.site.register(CustomerUser, CustomerUserAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'featured', 'created_at']
    # list_filter = ['category', 'featured']
    # search_fields = ['name', 'description']

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]


admin.site.register(Category, CategoryAdmin)

admin.site.register(Cart)
admin.site.register(CartItem)

admin.site.site_header = "E-Commerce Admin"
admin.site.site_title = "E-Commerce Admin Portal"
