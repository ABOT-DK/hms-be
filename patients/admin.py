from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'age', 'gender')
    search_fields = ('user__username',)
