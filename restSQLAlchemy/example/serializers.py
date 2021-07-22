from rest_framework import serializers
from rest_framework.relations import RelatedField
from example.models import Car, PartItem, session

class PartItemSerializer(serializers.Serializer):
    part_id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(required=False, allow_blank=True)
    series_num = serializers.IntegerField()
    car_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = PartItem
        fields = ["part_id","car_id","description","series_num",]
    

class CarSerializer(serializers.Serializer):
    car_id = serializers.IntegerField(read_only=True)
    make = serializers.CharField(required=False, allow_blank=True)
    model = serializers.CharField(required=False, allow_blank=True)
    year = serializers.CharField(required=False, allow_blank=True)
    parts = PartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = ["car_id","make","model","year","parts"]