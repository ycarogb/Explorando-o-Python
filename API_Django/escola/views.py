from rest_framework import viewsets
from escola import serializer
from escola.models import Aluno
from escola.serializer import AlunoSerializer

class AunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()  #trazendo todos os alunos
    serializer_class = AlunoSerializer

    

