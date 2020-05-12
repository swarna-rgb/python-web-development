from rest_framework import serializers
from .models import Employees

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        #fields = ['first_name', 'last_name', 'department']
        fields = '__all__'
# class EmployeeSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=200)
#     last_name = serializers.CharField(max_length=200)
#     department = serializers.CharField(max_length=200)
#
#     def create(self, validated_data):
#         return  Employees.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.department = validated_data.get('department', instance.department)
#         instance.save()
#         return instance


