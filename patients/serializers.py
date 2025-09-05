# patients/serializers.py


from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='user.get_full_name', read_only=True)
    
    class Meta:
        model = Patient
        fields = ['id', 'user', 'full_name', 'age', 'contact_number', 'medical_history']
        read_only_fields = ['user']

