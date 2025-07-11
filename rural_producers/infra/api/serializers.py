from rest_framework import serializers
from rural_producers.models import CulturaPlantada, Produtor, Safra, PropriedadeRural



class SafraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Safra
        fields = '__all__'

class CulturaPlantadaSerializer(serializers.ModelSerializer):
    safra = SafraSerializer()

    class Meta:
        model = CulturaPlantada
        fields = '__all__'

class PropriedadeRuralSerializer(serializers.ModelSerializer):
    culturas = CulturaPlantadaSerializer(many=True)
    class Meta:
        model = PropriedadeRural
        fields = '__all__'

class ProdutorSerializer(serializers.ModelSerializer):
    propriedades = PropriedadeRuralSerializer(many=True)
    class Meta:
        model = Produtor
        fields = '__all__'