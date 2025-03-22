
from rest_framework.serializers import ModelSerializer
from .models import BotUser

class BotUserSerializer(ModelSerializer):
    class Meta:
        model = BotUser
        fields = "__all__"

