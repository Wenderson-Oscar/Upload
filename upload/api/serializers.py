from rest_framework import serializers
from upload.models import Pessoa

class PessoaSerializes(serializers.ModelSerializer):
    class Meta:
        model= Pessoa
        fields= '__all__'
    