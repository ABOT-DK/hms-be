from rest_framework import viewsets, permissions
from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        if user.role == 'Doctor':
            return self.queryset.filter(doctor=user)
        elif user.role == 'Patient':
            return self.queryset.filter(patient__user=user)
        return self.queryset