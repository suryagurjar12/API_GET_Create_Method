from django.shortcuts import render
from django .http import JsonResponse ,HttpResponse
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import io
from rest_framework.parsers import JSONParser
# Create your views here.

@api_view(['GET','POST'])
def Stu_list(request):
    if request.method=='GET':
        Stu=Student.objects.all()
        serializer=StudentSerializer(Stu,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
@api_view(['GET','PUT','DELETE'])
def Stu_details(request,pk):
    id= Student.objects.get(id=pk)
    if id:
        if request.method=='GET':
            Stu=Student.objects.get(id=pk)
            serializer=StudentSerializer(Stu)
            return Response(serializer.data)
        
        elif request.method=="PUT":
            Stu=Student.objects.get(id=pk)
            serializer=StudentSerializer(Stu,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        elif request.method=="DELETE":
            Stu=Student.objects.get(id=pk)
            Stu.delete()
            return Response({'msg':'Data Deleted Successfull'})
    else:
        res={'msg':'id nit persent in Database'}
        return Response(res)
    
    

        











# def Stu_list(request):
#     if request.method =='GET':
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         return JsonResponse(serializer.data,safe=False)
    
    
#     elif request.method =='POST':
#         json_data=request.body
#         stream= io.ByteIO(json_data)
#         python_data=JSONParser().render(stream)
#         serializer=StudentSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Data created'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content='application/json')
            

# @csrf_exempt
# def Stu_details(request,pk):
#     if request.method=='GET':
#         id=Student.objects.filter(id=pk)
#         if id:
#             stu=Student.objects.get(id=pk)
#             serializer=StudentSerializer(stu)
#             return JsonResponse(serializer.data,safe=False) # ek or logic ser return kr a skte hai 
            
#             # json_data=JSONRenderer().render(serializer.data)
#             # return HttpResponse(json_data,content='application/json')
            
#         else:
#               res = {'msg': 'id not present in Database'}
#               return JsonResponse(res)
    
#     elif request.method == 'PUT':
#         id = Student.objects.filter(id=pk)
#         if id:
#             json_data = request.body
#             stream = io.BytesIO(json_data)
#             python_data = JSONParser().parse(stream)
#             stu = Student.objects.get(id=pk)
#             serializer = StudentSerializer(stu, data=python_data, partial = True)
#             # serializer = StudentSerializer(stu, data=python_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 res = {'msg':'Data Updated !!'}
#                 json_data = JSONRenderer().render(res)
#                 return HttpResponse(json_data, content_type='application/json')
#             json_data = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data, content_type='application/json')
#         else:
#             res = {'msg': 'id not present in Database'}
#             return JsonResponse(res)
    
#     elif request.method == 'PATCH':
#         id = Student.objects.get(id=pk)
#         if id:
#             json_data = request.body
#             stream = io.BytesIO(json_data)
#             python_data = JSONParser().parse(stream)
#             stu = Student.objects.get(id=pk)
#             serializer = StudentSerializer(stu, data=python_data, partial = True)
#             # serializer = StudentSerializer(stu, data=python_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 res = {'msg':'Data Partially Updated !!'}
#                 json_data = JSONRenderer().render(res)
#                 return HttpResponse(json_data, content_type='application/json')
#             json_data = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data, content_type='application/json')
#         else:
#             res = {'msg': 'id not present in Database'}
#             return JsonResponse(res)

#     elif request.method == 'DELETE':
#         id = Student.objects.get(id=pk)
#         if id:
#             stu = Student.objects.get(id=pk)
#             stu.delete()
#             res = {'msg': 'Data Deleted!!'}
#             return JsonResponse(res, safe=False)
#         else:
#             res = {'msg': 'id not present in Database'}
#             return JsonResponse(res)
            
            
# @csrf_exempt
# def list(request):
#     if request.method =="GET":
#         Student = Student.objects.all()
#         serializer_data = StudentSerializer(Student,many=True)
#         # print(serializer_data.data)
#         json_data = JSONRenderer().render(serializer_data.data)
#         return HttpResponse(json_data,content_type = 'application/json')
    
#     elif request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data) 
#         python_data = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'data created'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
    
#     elif request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data) 
#         python_data = JSONParser().parse(stream)
#         id=python_data.get('id')
#         stu=Student.objects.get(id=id)
#         serializer = StudentSerializer(stu,data = python_data,partial=True) #partail=true isliye krte hai kyu ki agr kisi ek row mai change kr skte hai or PATCH ka code likhe bina
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'data updated'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
    
    
#     elif request.method == 'PATCH':
#         json_data = request.body
#         stream = io.BytesIO(json_data) 
#         python_data = JSONParser().parse(stream)
#         id=python_data.get('id')
#         stu=Student.objects.get(id=id)
#         serializer = StudentSerializer(stu,data = python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'data created'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
    
    
#     elif request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data) 
#         python_data = JSONParser().parse(stream)
#         id=python_data.get('id')
#         if id:
#             stu=Student.objects.get(id=id)
#             stu.delete()
#             res={'msg':'data Deleted'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')

    