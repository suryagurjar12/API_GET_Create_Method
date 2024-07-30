from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    email=serializers.EmailField()
    city=serializers.CharField(max_length=100)
    
    
def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Student.objects.create(**validated_data)

def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance