from django.urls import path
from api import views

urlpatterns = [
    path('restaurants/', views.restaurants_list),
    path('restaurants/<int:pk>', views.restaurants_detail),
    path('pizzas/', views.pizzas_list),
    path('pizzas/<int:pk>', views.pizzas_detail),

]
