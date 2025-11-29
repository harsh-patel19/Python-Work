from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view,APIView
from myapp.models import *
from rest_framework.response import Response
from myapp.serializers import *

# Create your views here.
@api_view(['GET'])
def get_user(request):
    return HttpResponse("GET api calling")

@api_view(['POST'])
def post_user(request):
    return HttpResponse("POST api calling")

@api_view(['PUT'])
def put_user(request):
    return HttpResponse("PUT api calling")

@api_view(['DELETE'])
def delete_user(request):
    return HttpResponse("DELETE api calling")


class StudentView(APIView):

    def get(self,request):
      allstudents = Student.objects.all()
      students = StudentSerializer(allstudents,many =True)
      return Response({"students":students.data})
    
    def post(self,request):
        data= StudentSerializer(data=request.data)
        if not data.is_valid():
            return Response({"Errors":data.errors,"message":"somethinf went wrong"})
        else:
            data.save()
            return Response({"Data":data.data,"message":"Data inserted sucessfully"})
        

class StudentViewId(APIView):
    
    def get(self,request,id):
        student = Student.objects.get(pk=id)
        ser = StudentSerializer(student)
        return Response({"data":ser.data})
    
    def put(self,request,id):
        student = Student.objects.get(pk=id)
        ser = StudentSerializer(student,data=request.data)
        if not ser.is_valid():
            return Response({"Errors":ser.errors,"message":"something went wrong"})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"data updates sucessfully"})
        
    def patch(self,request,id):
        student = Student.objects.get(pk=id)
        ser = StudentSerializer(student,data=request.data,partial=True)
        if not ser.is_valid():
            return Response({"Errors":ser.errors,"message":"something went wrong"})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"data updates sucessfully"})
        
    def delete(self,request,id):
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({"message":"data deleted"})

