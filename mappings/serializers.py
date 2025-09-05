#mappings/serializers.py

from rest_framework import serializers
from .models import Mapping

class MappingSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.user.get_full_name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.user.get_full_name', read_only=True)

    class Meta:
        model = Mapping
        fields = ['id', 'patient', 'doctor', 'assigned_at', 'patient_name', 'doctor_name']
        read_only_fields = ['assigned_at']
