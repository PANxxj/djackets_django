from .views import *
from django.urls import path


urlpatterns = [
    path('latest-product',LatestProductList.as_view()),
    path('product/<slug:category_slug>/<slug:product_slug>',ProductDetail.as_view()),
    path('product/<slug:category_slug>',CategoryDetail.as_view()),
    path('product/search',Search.as_view())
]
