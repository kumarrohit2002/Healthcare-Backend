

# Create your models here.
#patients/models.py

from django.db import models
from accounts.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    age = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=15, blank=True)
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} (Patient)"
