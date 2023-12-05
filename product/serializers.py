# in the Django REST Framework, serializers allow conversion of complex data types, such as Django models into a format that can be easily rendered into JSON

from rest_framework import serializers
# import models.
from . models import Product, Product_Image, Offering, Deal

class ProductSerializer(serializers.ModelSerializer):
    # is a inner class that provides metadata for the serializer.
    class Meta:
        #  specifies the model that the serializer will work with
        model = Product
        #  indicates that all fields from the Product model should be included in the serialized representation. 
        fields = '__all__'

class ProductSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

class Product_ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Image
        fields = '__all__'

class OfferingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offering
        fields = '__all__'

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'
