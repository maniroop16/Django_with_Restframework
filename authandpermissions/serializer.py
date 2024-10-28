from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Authoriseuser

class Authserializer(ModelSerializer):
    class Meta:
        model = Authoriseuser
        fields = "__all__"


class Loginserializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()        
