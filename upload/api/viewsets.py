from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PessoaSerializes
from upload.models import Pessoa
from rest_framework.response import Response
from datetime import datetime
import pandas as pd


class PessoaViewSets(viewsets.ModelViewSet):

    serializer_class = PessoaSerializes
    queryset = Pessoa.objects.all()

    def create(self, request):
        file1 = request.FILES.get('file')
        file = pd.read_excel(file1,engine='openpyxl')
        for i in range(len(file)):
            nascimento = file['nascimento'][i]
            data = datetime.fromtimestamp(nascimento/1e3)
            cadastro = Pessoa(codigo = file['id'][i], nome = file['nome'][i],
            sobrenome = file['sobrenome'][i], sexo = file['sexo'][i],
            altura = file['altura'][i], peso = file['peso'][i],
            nascimento = data, bairro = file['bairro'][i],
            cidade = file['cidade'][i], estado = file['estado'][i],
            numero = file['numero'][i], file = file1)
            cadastro.save()
        return Response('Dados Registrados')


class MulhereViewSets(viewsets.ModelViewSet):

    serializer_class= PessoaSerializes
    queryset= Pessoa.objects.filter(sexo='F', cidade='Meeren')


class NascimentoViewSets(viewsets.ModelViewSet):

    serializer_class = PessoaSerializes
    queryset = Pessoa.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['sexo']
    ordering_fields = ['nascimento']

