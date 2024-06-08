from django.urls import path
from . import views

urlpatterns = [

    #Get http://localhost:8000/api/products
    path("products", views.get_products),
    
    #Get http://localhost:8000/api/products/id
    path("products/<int:id>", views.get_product),

    #POST http://localhost:8000/api/products/new
    path("products/new", views.add_product),

    #PUT http://localhost:8000/api/products/edit/id
    path("products/edit/<int:id>", views.edit_product),

    #DELETE http://localhost:8000/api/products/delete/id
    path("products/delete/<int:id>", views.delete_product),

]