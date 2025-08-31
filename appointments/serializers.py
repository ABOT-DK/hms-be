from rest_framework import serializers
from .models import Appointment
from patients.serializers import PatientSerializer
from users.serializers import UserSerializer
from patients.models import Patient
from users.models import User

class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    doctor = UserSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), write_only=True, source='patient')
    doctor_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='Doctor'), write_only=True, source='doctor')


class Meta:
    model = Appointment
    fields = ['id', 'patient', 'doctor', 'patient_id', 'doctor_id', 'date', 'reason']