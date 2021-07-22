from django.urls import path, include
from rest_framework.routers import DefaultRouter
from example import views

# Create a router and register our viewsets with it.

car_list = views.CarViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
# The API URLs are now determined automatically by the router.
urlpatterns = [
    # path('cars', views.CarList.as_view()),
    # path('parts', views.PartItemList.as_view()),
    path('cars/', car_list, name='car-list'),
]