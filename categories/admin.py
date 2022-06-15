
from django.contrib import admin
from .models import Category, Subcategory

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'sub_slug': ('sub_category_name',)}
    list_display = ('sub_category_name', 'sub_slug')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubCategoryAdmin)
