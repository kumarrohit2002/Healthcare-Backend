#doctors/serializers.py

from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='user.get_full_name', read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'user', 'full_name', 'specialization', 'experience_years', 'contact_number', 'availability']
        read_only_fields = ['user']

