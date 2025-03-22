from rest_framework.viewsets import ModelViewSet
#from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
#from django_filters.rest_framework import DjangoFilterBackend

from .models import BotUser
from .serializers import BotUserSerializer

# Foydalanuvchilar uchun ViewSet
class BotUserViewSet(ModelViewSet):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['username', 'full_name', 'chat_id']
