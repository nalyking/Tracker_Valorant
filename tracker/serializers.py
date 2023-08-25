from rest_framework import exceptions, serializers

class Tracker_serializer(serializers.Serializer):
    code= serializers.IntegerField(required= False)
    printar= serializers.CharField(required= False)
    name= serializers.CharField(required= False)