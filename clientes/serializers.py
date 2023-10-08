from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import cpf_valido, nome_valido, rg_valido, celular_valido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({"cpf":"CPF inválido"})
        if nome_valido(data['nome']):
            raise serializers.ValidationError({"nome":"O campo nome não deve conter números"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({"rg":"O RG deve ter 9 dígitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({"celular": "O número do celular não é valido"})
        return data
    