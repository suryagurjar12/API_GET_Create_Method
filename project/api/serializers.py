from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    email=serializers.EmailField()
    city=serializers.CharField(max_length=100)
    
    
# def create(self, validated_data): #isko create krne ke liye ye method use kiye jati hai 
#         """
#         Create and return a new `Student` instance, given the validated data.
#         """
#         return Student.objects.create(**validated_data) 

# def update(self, instance, validated_data): #upadete krne ke liye use kiya jata hai
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         # return instance

# instance ek variable hai jese apn models.charfield lete the yese hi yeha par
# ham instance ka use krte hai or kya kya show krana hai name city ya email

class StudentSerializer(serializers.ModelSerializer):
        class Meta:
                model= Student
                fields =["id","name","email","city"]