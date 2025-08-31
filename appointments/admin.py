from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'date', 'reason')
    list_filter = ('doctor', 'date')
    search_fields = ('patient__user__username', 'doctor__username')
