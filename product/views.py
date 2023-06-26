from django.http import Http404
from django.shortcuts import render
from .models import *
from .serializers import*
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q

class LatestProductList(APIView):
    def get(self, request, *args, **kwargs):
        products=Product.objects.all()[0:4]
        ser=ProductSerializers(products,many=True)
        return Response(ser.data)
    
class ProductDetail(APIView):
    def get_object(self,category_slug,product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            return Http404
        
    def get(self,request,category_slug,product_slug,format=None):
        Product=self.get_object(category_slug,product_slug)
        ser=ProductSerializers(Product)
        return Response(ser.data)
    
class CategoryDetail(APIView):
    def get_object(self,category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            return Http404
        
    def get(self,request,category_slug,format=None):
        category=self.get_object(category_slug)
        ser=CategorySerializers(category)
        return Response(ser.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query','')

    if query:
        product=Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        ser=ProductSerializers(product,many=True)
        return Response(ser.data)
    else:
        Response({'product':[]})