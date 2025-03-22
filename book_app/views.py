from rest_framework.viewsets import ModelViewSet
from .models import Textbook
from .serializers import TextbookSerializer
from rest_framework import generics

#from rest_framework.views import APIView
#from rest_framework.response import Response



class TextbookViewSet(ModelViewSet):
    queryset = Textbook.objects.all()
    serializer_class = TextbookSerializer
    #filter_backends = [DjangoFilterBackend]
    filterset_fields = ['grade', 'language']



class TextbookListView(generics.ListAPIView):
    queryset = Textbook.objects.all()
    serializer_class = TextbookSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        grade = self.request.query_params.get('grade')  # URL'dan grade olamiz
        if grade:
            queryset = queryset.filter(grade=grade)  # Faqat shu sinf uchun filterlash
        return queryset