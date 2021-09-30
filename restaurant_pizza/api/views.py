from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant, Pizza
from django.http import Http404
from .serializers import RestaurantSerializer, PizzaSerializer
from rest_framework import mixins, generics

class RestaurantList(APIView):
    def get(self, request, format=None):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_description="description", request_body=RestaurantSerializer)
    def post(self, request, format=None):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        restaurant = self.get_object(pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=RestaurantSerializer)
    def put(self, request, pk, format=None):
        restaurant = self.get_object(pk)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        restaurant = self.get_object(pk)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




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
