from rest_framework import serializers
from .models import Restaurant, Pizza


class RestaurantSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=250)

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance


class PizzaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    cheese_type = serializers.CharField(max_length=100)
    dough_thickness = serializers.CharField(max_length=100)
    secret_ingredient = serializers.CharField(max_length=100)
    restaurant = RestaurantSerializer()

    def create(self, validated_data):
        return Pizza.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.cheese_type = validated_data.get('cheese_type', instance.cheese_type)
        instance.dough_thickness = validated_data.get('dough_thickness', instance.dough_thickness)
        instance.secret_ingredient = validated_data.get('secret_ingredient', instance.secret_ingredient)
        instance.restaurant = validated_data.get('restaurant', instance.restaurant)
        instance.save()
        return instance
