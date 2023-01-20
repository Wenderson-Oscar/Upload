from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from .serializers import PersonSerializer
from upload.models import Person
import datetime
import pandas as pd
from rest_framework.response import Response

class PersonViewSet(viewsets.ModelViewSet):

    serializer_class=PersonSerializer
    queryset= Person.objects.all()

    def create(self, request):
        arquivo1=request.FILES.get('file')
        arquivo=pd.read_excel(arquivo1,engine='openpyxl')
        for i in range(len(arquivo)):
            nascimento = arquivo['nascimento'][i]
            date = datetime.datetime.fromtimestamp(nascimento/1e3)
            cadastro =  Person(codigo=arquivo['id'][i],  nome=arquivo['nome'][i],
            sobrenome=arquivo['sobrenome'][i], sexo=arquivo['sexo'][i],
            altura=arquivo['altura'][i], peso=arquivo['peso'][i],
            nascimento=date , bairro=arquivo['bairro'][i],
            cidade=arquivo['cidade'][i], estado=arquivo['estado'][i],
            numero=arquivo['numero'][i], file=arquivo1)
            cadastro.save()
        return Response('Dados inseridos!')

class MulheresViewSet(viewsets.ModelViewSet):
    serializer_class= PersonSerializer
    queryset= Person.objects.filter(sexo='F', cidade='Meeren')

class NascimentoViewSet(viewsets.ModelViewSet):
    serializer_class= PersonSerializer
    queryset= Person.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['sexo']
    ordering_fields = ['nascimento']
