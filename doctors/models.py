# Create your models here.
#doctors/models.py
from django.db import models
from accounts.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialization = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=15, blank=True)
    availability = models.TextField(blank=True)  # e.g., "Mon-Fri 9AM-5PM"

    def __str__(self):
        return f"{self.user.get_full_name()} (Doctor - {self.specialization})"
