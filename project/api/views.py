from django.shortcuts import render
from django .http import JsonResponse ,HttpResponse
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
# Create your views here.

def Stu_list(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    return JsonResponse(serializer.data,safe=False)


def Stu_details(request,pk):
    user=Student.objects.get(id=pk)
    # print("stu_name =",user.name)
    serializer=StudentSerializer(user)
    return JsonResponse(serializer.data,safe=False)


@csrf_exempt
def list(request):
    if request.method =="GET":
        user = Student.objects.all()
        serializer_data = StudentSerializer(user,many=True)
        # print(serializer_data.data)
        json_data = JSONRenderer().render(serializer_data.data)
        return HttpResponse(json_data,content_type = 'application/json')
    
    elif request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data) 
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)

    