from django.db import models
from rest_framework.serializers import ModelSerializer
from products.models import ProductModel

class ProductsSerializer(ModelSerializer):

    class Meta:
        model = ProductModel
        fields = "__all__" #all fields

