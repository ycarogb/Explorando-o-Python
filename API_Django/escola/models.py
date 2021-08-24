from django.db import models

#criando um modelo para o banco de dados
#definimos um metodo __Str__ para referenciar o objeto da classe Aluno com o seu nome
class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)

    def __str__(self):
        return self.nome


