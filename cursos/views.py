from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

# Create your views here.
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer
  #lookup_field = 'id'

class CursosAPIView(generics.ListCreateAPIView):
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Avaliacao.objects.all()
  serializer_class = AvaliacaoSerializer
  lookup_field = 'id'


class AvaliacoesAPIView(generics.ListCreateAPIView):
  queryset = Avaliacao.objects.all()
  serializer_class = AvaliacaoSerializer

  # def get_queryset(self):
  #   curso_id = self.kwargs.get('curso_id')
  #   if curso_id:
  #     return self.queryset.filter(curso_id=curso_id)
  #   return self.queryset