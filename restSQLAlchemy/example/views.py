from example.serializers import PartItemSerializer, CarSerializer
from example.models import Car, PartItem, session
from rest_framework import viewsets


class CarViewSet(viewsets.ModelViewSet):
    """
    This viewset provides `list`, `retrieve`, `update` and `delete` actions.
    """
    queryset = session.query(Car).all()
    serializer_class = CarSerializer

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        car = session.query(Car).filter(Car.car_id==pk).first()
        return car

    def perform_destroy(self, instance):
        session.delete(instance)
        session.commit()

class PartItemViewSet(viewsets.ModelViewSet):
    """
    This viewset provides `list`, `retrieve`, `update` and `delete` actions.
    """
    queryset = session.query(PartItem).all()
    serializer_class = PartItemSerializer
    
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        part = session.query(PartItem).filter(PartItem.part_id==pk).first()
        return part

    def perform_destroy(self, instance):
        session.delete(instance)
        session.commit()