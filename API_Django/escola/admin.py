from django.contrib import admin
from escola.models import Aluno

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg') #dados que quero mostrar
    list_display_links = ('id', 'nome') #criando links com esses dados
    search_fields = ('nome',)


admin.site.register(Aluno, Alunos)

