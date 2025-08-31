from rest_framework import viewsets, permissions
from .models import LabResult
from .serializers import LabResultSerializer


class LabResultViewSet(viewsets.ModelViewSet):
    queryset = LabResult.objects.all()
    serializer_class = LabResultSerializer
    permission_classes = [permissions.IsAuthenticated]