from django.contrib import admin
from .models import LabResult

@admin.register(LabResult)
class LabResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'test_name', 'uploaded_at')
    search_fields = ('patient__user__username', 'test_name')
