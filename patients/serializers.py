from rest_framework import serializers
from .models import Patient
from users.serializers import UserSerializer


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

class Meta:
    model = Patient
    fields = ['id', 'user', 'age', 'gender']