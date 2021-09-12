from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Restaurant, Pizza
from .serializers import RestaurantSerializer, PizzaSerializer


@csrf_exempt
@swagger_auto_schema(method='POST', request_body=RestaurantSerializer)
@api_view(['GET', 'POST'])
def restaurants_list(request):
    if request.method == 'GET':
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RestaurantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=401)


@csrf_exempt
@swagger_auto_schema(method='PUT', request_body=RestaurantSerializer)
@api_view(['PUT', 'DELETE', 'GET'])
def restaurants_detail(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurant)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RestaurantSerializer(restaurant, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        restaurant.delete()
        return HttpResponse(status=204)


@csrf_exempt
@swagger_auto_schema(method='POST', request_body=PizzaSerializer)
@api_view(['GET', 'POST'])
def pizzas_list(request):
    if request.method == 'GET':
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PizzaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)


@csrf_exempt
@swagger_auto_schema(method='PUT', request_body=PizzaSerializer)
@api_view(['PUT', 'DELETE', 'GET'])
def pizzas_detail(request, pk):
    try:
        pizza = Pizza.objects.get(pk=pk)
    except PizzaSerializer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PizzaSerializer(pizza)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PizzaSerializer(pizza, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        pizza.delete()
        return HttpResponse(status=204)
