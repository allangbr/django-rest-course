from rest_framework import serializers
from .models import Curso, Avaliacao
from django.db.models import Avg

class AvaliacaoSerializer(serializers.ModelSerializer):
  class Meta:
    extra_kwargs = {
        'email': {'write_only': True}
    }
    model = Avaliacao
    fields = '__all__'

  def validate_avalicao(self, valor):
    if valor in range(1,6):
      return valor
    raise serializers.ValidationError('A avaliação deve ser entre 1 e 5.')

class CursoSerializer(serializers.ModelSerializer):

  #1. Nested Relationship (menos performático)
  #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

  #2. Hyperlinked Relationship (performático mas requer URLs)
  #avaliacoes = serializers.HyperlinkedRelatedField(many=True, view_name='avaliacao-detail', read_only=True)

  #3. Primary Key Relationship (mais performático)
  avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

  media_avalicoes = serializers.SerializerMethodField()

  class Meta:
    model = Curso
    fields = ('id','titulo', 'url', 'criacao', 'ativo' ,'avaliacoes', 'media_avalicoes')

  def get_media_avalicoes(self, obj):
    media = obj.avaliacoes.aggregate(Avg('avalicao')).get('avalicao__avg')
    if media is None:
      return 0
    return round(media*2)/2
  