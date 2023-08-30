from django.contrib import admin
from .models import *

admin.site.register(Slider)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Condition)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_by', 'created_at', 'updated_at')

admin.site.register(Product, ProductAdmin)
admin.site.register(Super_SubCategory)
admin.site.register(Cart)