"""
EXERCÍCIOS PYTHON PARA PROCESSOS SELETIVOS STRING/LISTAS

enunciados https://www.programcreek.com/2012/11/top-10-algorithms-for-coding-interview/

"""
from typing import Iterable
from itertools import chain
#métodos para memorizar

s= "banana"
a= list("banana") #tranformando uma string em lista
print(a)

#identificando um item em uma lista ou string
primeiraLetra = a[0] 

#em Python, você pode usar indices negativos
print(s[-2])
print(primeiraLetra)

#O método slice serve para dividir strings e listas
print(s[2:5])
print(a[2:5])

#ordenar os elementos usando sorted
ordenado = sorted(a)
print(ordenado)

#Rotacionando listas
#a classe Iterable é relacionada a elementos iteráveis, ex.Lista,string etc.
def rotacionar(iteravel: Iterable, k:int):
    lista = list(iteravel)
    primeira_fatia=lista[k+1:] #fatiamento a partir do ultimo elemento
    segunda_fatia=lista[:k+1] #fatiamento a partir do primeiro elemento
    return primeira_fatia + segunda_fatia

listaTeste = [1,2,3,4,5,6,7]
print(rotacionar(listaTeste,3))
