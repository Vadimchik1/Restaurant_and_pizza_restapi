from django.urls import path
from api import views

urlpatterns = [
    path('restaurants/', views.RestaurantList.as_view()),
    path('restaurants/<int:pk>', views.RestaurantDetail.as_view()),
    path('pizzas/', views.pizzas_list),
    path('pizzas/<int:pk>', views.pizzas_detail),

]
