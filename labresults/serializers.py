from rest_framework import serializers
from .models import LabResult
from patients.serializers import PatientSerializer
from patients.models import Patient


class LabResultSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), write_only=True, source='patient')


class Meta:
    model = LabResult
    fields = ['id', 'patient', 'patient_id', 'test_name', 'file', 'uploaded_at']