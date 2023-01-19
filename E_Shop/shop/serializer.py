from  rest_framework import serializers

from shop.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('title', 'price', 'category','brand',)

class GenderSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    slug = serializers.CharField(max_length=200)
    def create(self, validated_data):
        return Gender.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)

        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance
