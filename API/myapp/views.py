from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view,APIView,permission_classes
from myapp.models import *
from rest_framework.response import Response
from myapp.serializers import *
from rest_framework.permissions import IsAuthenticated
# from myapp.permissions import *
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users(request):
    return HttpResponse("GET API CALLING...")


@api_view(['POST'])
# @permission_classes([isAdminUserOnly])
def post_users(request):
    return HttpResponse("POST API CALLING...")

@api_view(['PUT'])
def put_users(request):
    return HttpResponse("PUT API CALLING...")

@api_view(['DELETE'])
def delete_users(request):
    return HttpResponse("DELETE API CALLING...")




class StudentView(APIView):

    def get(self,request):
        allstudents = Student.objects.all()
        students = StudentSerializer(allstudents,many=True)
        return Response({"students":students.data})

    def post(self,request):
        data = StudentSerializer(data = request.data)
        if not data.is_valid():
            return Response({"Errors":data.errors,"message":"something went wrong!!!"})
        else:
            data.save()
            return Response({"Data":data.data,"message":"data inserted sucessfully!!!"})
            
        # print(request.data)
        # return HttpResponse("POST API CALLING!!")
    
class StudentViewId(APIView):

    def get(self,request,id):
        # return HttpResponse("Calling!!!")
        student = Student.objects.get(pk=id)
        ser = StudentSerializer(student)
        return Response({"data":ser.data})


    def put(self,request,id):
        student = Student.objects.get(pk=id)
        ser = StudentSerializer(student,data=request.data)
        if not ser.is_valid():
            return Response({"Error":ser.errors,"message":"something went wrong"})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"data update sucessfully!!"})


    def patch(self,request,id):
        student = Student.objects.get(pk=id)
        ser = StudentSerializer(student,data=request.data,partial=True)
        if not ser.is_valid():
            return Response({"Error":ser.errors,"message":"something went wrong"})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"data update sucessfully!!"})


    def delete(self,request,id):
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({"message":"data delete!!"})
