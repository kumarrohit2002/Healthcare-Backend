# Create your models here.
#mappings/models.py

from django.db import models
from doctors.models import Doctor
from patients.models import Patient

from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class Mapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='mappings')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='mappings')
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('patient', 'doctor')  # Prevent duplicate assignments

    def __str__(self):
        return f"{self.patient.user.get_full_name()} -> {self.doctor.user.get_full_name()}"
