from .models import Record
from rest_framework import serializers

# class DeveloperSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Developer
#         fields = ['name']

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['name', 'date']