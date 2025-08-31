from rest_framework import viewsets, permissions
from .models import Patient
from .serializers import PatientSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['gender', 'age']