from rest_framework import serializers
from crudapp.models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Employee
        fields = '__all__'


    def validate(self, attrs):
        errors = {}

        if attrs.get('age') is not None and attrs['age'] <18:
            errors['age'] = "Age must be above 18"

        if attrs.get('name') and not attrs['name'].isalpha():
            errors['name'] = "Only Charachters allowed in name"

        if errors:
            raise serializers.ValidationError(errors)
        return attrs
        