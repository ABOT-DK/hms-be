from rest_framework import serializers
from .models import Message
from users.serializers import UserSerializer
from users.models import User


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    recipient = UserSerializer(read_only=True)
    sender_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='sender')
    recipient_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='recipient')


class Meta:
    model = Message
    fields = ['id', 'sender', 'recipient', 'sender_id', 'recipient_id', 'content', 'timestamp']