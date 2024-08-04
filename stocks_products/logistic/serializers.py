from rest_framework import serializers
from .models import Stock, Product


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'name']

    def create(self, validated_data):
        stock, created = Stock.objects.update_or_create(name=validated_data['name'], defaults=validated_data)
        return stock

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        product, created = Product.objects.update_or_create(name=validated_data['name'], defaults=validated_data)
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
