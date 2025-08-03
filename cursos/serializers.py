from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):
  class Meta:
    extra_kwargs = {
        'email': {'write_only': True}
    }
    model = Avaliacao
    fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):

  #1. Nested Relationship (menos performático)
  #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

  #2. Hyperlinked Relationship (performático mas requer URLs)
  #avaliacoes = serializers.HyperlinkedRelatedField(many=True, view_name='avaliacao-detail', read_only=True)

  #3. Primary Key Relationship (mais performático)
  avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)



  class Meta:
    model = Curso
    fields = ('id','titulo', 'url', 'criacao', 'ativo' ,'avaliacoes')