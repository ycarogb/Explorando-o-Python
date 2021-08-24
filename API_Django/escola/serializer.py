from rest_framework import serializers
from escola.models import Aluno

#O Serializer traduz Json para Python e vice-versa

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg']
