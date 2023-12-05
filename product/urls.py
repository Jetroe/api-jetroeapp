# product/urls.py

from django.urls import path
from . views import ProductListCreateView, ProductDetailView, ProductImageView, OfferingCreateView, DealCreateView, ProductSearchView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product-images/', ProductImageView.as_view(), name='product-image-create'),
    path('offerings/', OfferingCreateView.as_view(), name='offering-create'),
    path('deals/', DealCreateView.as_view(), name='deal-create'),
    path('search/', ProductSearchView.as_view(), name='product-search'),
]


# where you define the URL patterns for your web application.

# Each path function takes three arguments: (1) The URL pattern as a string. (2) The view that should handle the request. (3) An optional name for the URL pattern.
# <int:pk> is a path converter that captures an integer and passes it to the view as pk (primary key).

#path('products/', ProductListCreateView.as_view(), name='product-list-create') - Maps to a view that handles listing and creating products.
#path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail') - Maps to a view that handles retrieving, updating, and deleting a specific product.
#path('product-images/', ProductImageView.as_view(), name='product-image-create') - Maps to a view that handles creating product images.
#path('offerings/', OfferingCreateView.as_view(), name='offering-create') - Maps to a view that handles creating product offerings.
#path('deals/', DealCreateView.as_view(), name='deal-create') - Maps to a view that handles creating product deals.


