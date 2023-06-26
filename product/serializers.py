from rest_framework import serializers
from . models import *

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=(
            'id',
            'name',
            'get_absolute_url',
            'description',
            'price',
            'get_image',
            'get_thumbnail'
        )
class CategorySerializers(serializers.ModelSerializer):
    # product=ProductSerializers(many=True)
    class Meta:
        model=Category
        fields=(
            'id',
            'name',
            'get_absolute_url',
            # 'product',
        )