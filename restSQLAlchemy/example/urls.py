from django.urls import path, include
from example import views


car_list = views.CarViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

car_detail = views.CarViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
part_list = views.PartItemViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
part_detail = views.PartItemViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    path('cars/', car_list, name='car-list'),
    path('cars/<int:pk>/', car_detail, name='car-detail'),
    path('parts/', part_list, name='part-list'),
    path('parts/<int:pk>/', part_detail, name='part-detail'),

]