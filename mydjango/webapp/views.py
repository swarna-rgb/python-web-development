from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from .models import Employees
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class EmployeeGenericViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class = EmployeeSerializer
    queryset = Employees.objects.all()

class EmployeeViewSet(viewsets.ViewSet):
    def list(self, request):
        all_employess = Employees.objects.all()
        serializer = EmployeeSerializer(all_employess, many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # 201 created status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        query_set = Employees.objects.all()
        employee = get_object_or_404(query_set,pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def update(self,request,pk=None):
        employee =  Employees.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # 201 created status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GenericAPIView
class EmployeeGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin,
                             mixins.CreateModelMixin, mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = EmployeeSerializer
    queryset = Employees.objects.all()
    lookup_field = 'id'
    # authentication_classes = [SessionAuthentication,BasicAuthentication] #it will check first session authentication if not basic authentication
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


# class based views
# class EmployeeAPIView(APIView):
#     def get(self,request):
#         all_employess = Employees.objects.all()
#         serializer = EmployeeSerializer(all_employess,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED) #201 created status
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class EmployeeDetailAPIView(APIView):
#     def get_object(self,id):
#         try:
#            return Employees.objects.get(pk=id)
#         except Employees.DoesNotExist:
#            return Response(status = status.HTTP_404_NOT_FOUND)
#
#     def get(self, request,id):
#         employee = self.get_object(id=id)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data)
#
#     def put(self, request, id ):
#         employee = self.get_object(id)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data)
#         return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         employee = self.get_object(id)
#         employee.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)

# api_view function based views
# @api_view(['GET', 'POST'])
# def employee_list_view(request):
#     if request.method == 'GET':
#         all_employess = Employees.objects.all()
#         serializer = EmployeeSerializer(all_employess,many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED) #201 created status
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def employee_detail(request,pk):
#         try:
#             employee = Employees.objects.get(pk=pk)
#         except Employees.DoesNotExist:
#             return Response(status = status.HTTP_404_NOT_FOUND)
#
#         if request.method == 'GET':
#             serializer = EmployeeSerializer(employee)
#             return Response(serializer.data)
#         elif request.method == 'PUT':
#             serializer = EmployeeSerializer(employee,data = request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         elif request.method == 'DELETE':
#             employee.delete()
#             return Response(status = status.HTTP_204_NO_CONTENT)

# model serializer
# @csrf_exempt
# def employee_list_view(request):
#     if request.method == 'GET':
#         all_employess = Employees.objects.all()
#         serializer = EmployeeSerializer(all_employess,many=True)
#         return JsonResponse(serializer.data,safe=False) #In order to allow non-dict objects to be serialized set the safe parameter to False.
#
#     elif request.method == 'POST':
#         emp_data = JSONParser().parse(request)
#         serializer = EmployeeSerializer(data=emp_data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201) #201 created status
#         return JsonResponse(serializer.errors, status=400)
#
# @csrf_exempt
# def employee_detail(request,pk):
#         try:
#             employee = Employees.objects.get(pk=pk)
#         except Employees.DoesNotExist:
#             return HttpResponse(status=404)
#
#         if request.method == 'GET':
#             serializer = EmployeeSerializer(employee)
#             return JsonResponse(serializer.data, safe=False)
#         elif request.method == 'PUT':
#             emp_data_toupdate = JSONParser().parse(request)
#             print(emp_data_toupdate)
#             serializer = EmployeeSerializer(employee,data=emp_data_toupdate)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data)
#             return  JsonResponse(serializer.errors, status=400)
#         elif request.method == 'DELETE':
#             employee.delete()
#             return HttpResponse(status=204)
