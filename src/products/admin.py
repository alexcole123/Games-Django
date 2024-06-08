from django.contrib.admin import ModelAdmin, site

from products.models import CategoryModel, ProductModel

#how to admin category
class CategoryAdmin(ModelAdmin):
    list_display = ("id", "name")
    
    #display name and id as link to edit products
    list_display_links = ("id", "name")

#how to admin product
class ProductAdmin(ModelAdmin):
    list_display = ("id", "name", "price", "stock", "category", "release_date")

#connect between admin models
site.register(CategoryModel, CategoryAdmin)
site.register(ProductModel, ProductAdmin)