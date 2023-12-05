
from django.shortcuts import render
# import Q: for complex queries.
from django.db.models import Q 
# DRF provides generic views for common CRUD operations (Create, Retrieve, Update, Delete). Used to simplify view creation.
from rest_framework import generics
# Django Rest Framework's class for handling HTTP responses.
from rest_framework.response import Response
from . models import Product, Product_Image, Offering, Deal
# Importing the serializers for these models. Serializers help convert complex data types (models) into Python data types that can be easily rendered into JSON.
from . serializers import ProductSerializer, Product_ImageSerializer, OfferingSerializer, DealSerializer, ProductSearchSerializer


# Create your views here. ok

# generic view that allows listing all instances of a model (List) and creating new instances of a model 
class ProductListCreateView(generics.ListCreateAPIView):
    # Specifies the set of products to be used (in this case, all products). It's a query that fetches the data from the database.
    # objects.all() To retrieve all products from the database:
    queryset = Product.objects.all()
    # serializer_class: Specifies the serializer to be used for converting between Python objects and JSON for products.
    serializer_class = ProductSerializer

class ProductSearchView(generics.ListAPIView):
    serializer_class = ProductSearchSerializer
    def get_queryset(self):
        search_query = self.request.query_params.get('search', None)

        if search_query:
            # If there's a search query, filter the products based on name or description
            return Product.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
        else:
            # return all objects if no search query.
            return Product.objects.all()

# generic view for retrieving (Retrieve), updating (Update), and destroying (Destroy - deleting) a single instance of a model.
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# generics.ListCreateAPIView: generic view for creating a new Model
class ProductImageView(generics.CreateAPIView):
    queryset = Product_Image.objects.all()
    serializer_class = Product_ImageSerializer

class OfferingCreateView(generics.CreateAPIView):
    queryset = Offering.objects.all()
    serializer_class = OfferingSerializer

class DealCreateView(generics.CreateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer