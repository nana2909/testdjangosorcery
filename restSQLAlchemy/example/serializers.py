from rest_framework import serializers
from rest_framework.relations import RelatedField
from example.models import Car, PartItem, session

class PartItemSerializer(serializers.Serializer):
    part_id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(required=False, allow_blank=True)
    series_num = serializers.IntegerField()
    car_id = serializers.IntegerField()

    def create(self, validated_data): 
        """
        Create and return a new 'Part Item', given the validated data.
        """    
        object = PartItem(**validated_data)
        session.add(object)
        session.commit()
        return object

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Part Item', given the validated data.
        """
        part = session.query(PartItem).filter(PartItem.part_id==instance.part_id).first()
        part.description = validated_data.get('description', instance.description)
        part.series_num = validated_data.get('series_num', instance.series_num)
        part.car_id = validated_data.get('car_id', instance.car_id)
        session.commit()
        return part
    
class CarSerializer(serializers.Serializer):
    car_id = serializers.IntegerField(read_only=True)
    make = serializers.CharField(required=False, allow_blank=True)
    model = serializers.CharField(required=False, allow_blank=True)
    year = serializers.CharField(required=False, allow_blank=True)
    parts = PartItemSerializer(many=True, read_only=True)

    def create(self, validated_data):
        """
        Create and return a new 'Car', given the validated data.
        """     
        object = Car(**validated_data)
        session.add(object)
        session.commit()
        return object
    
    def update(self, instance, validated_data):
        """
        Update and return an existing 'Car', given the validated data.
        """
        car = session.query(Car).filter(Car.car_id==instance.car_id).first()
        car.make = validated_data.get('make', instance.make)
        car.model = validated_data.get('model', instance.model)
        car.year = validated_data.get('year', instance.year)
        session.commit()
        return car
    
    
        