import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from shop.models import *


class ProductsSerializer(serializers.ModelSerializer):
    colors = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    sizes = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    brand = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
    category = serializers.CharField(source='get_category_display')
    class Meta:
        model = Women
        fields = '__all__'


class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorProduct
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeProduct
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
