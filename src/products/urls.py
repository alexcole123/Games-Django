from django.urls import path
from . import views

urlpatterns = [

    # http://localhost:8000/products/sales
    path("sales", views.sales, name="sales"),

    # http://localhost:8000/products
    path("", views.list, name="products"),

    # http://localhost:8000/products/details/id
    path("details/<int:id>", views.details, name="details"),

    # http://localhost:8000/products/categories
    path("categories", views.categories, name="categories"),

    # http://localhost:8000/products/new
    path("new", views.insert, name="insert"),

    # http://localhost:8000/products/edit/id
    path("edit/<int:id>", views.edit, name="edit"),

    # http://localhost:8000/products/delete/id
    path("delete/<int:id>", views.delete, name="delete"),

    # http://localhost:8000/products/info
    path("info", views.info, name="info"),
]