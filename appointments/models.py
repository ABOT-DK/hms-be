from django.db import models
from users.models import User
from patients.models import Patient


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'Doctor'})
    date = models.DateTimeField()
    reason = models.TextField(blank=True)


    def __str__(self):
      return f"{self.patient} with {self.doctor} on {self.date}"