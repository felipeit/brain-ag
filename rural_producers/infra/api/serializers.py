#from typing import Dict
#from rural_producers import models
from rest_framework import serializers
from rural_producers.models import CulturaPlantada, Produtor, Safra, PropriedadeRural
# from django.db.models import Model
# from django.db import transaction


class SafraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Safra
        fields = '__all__'

class CulturaPlantadaSerializer(serializers.ModelSerializer):
    safra = SafraSerializer()

    class Meta:
        model = CulturaPlantada
        exclude = ('propriedade_rural',)
        #fields = '__all__'

class PropriedadeRuralSerializer(serializers.ModelSerializer):
    culturas = CulturaPlantadaSerializer(many=True)

    # def validate(self, attrs) -> Dict:
    #     area_agricultavel = attrs.get('area_agricultavel')
    #     area_vegetacao = attrs.get('area_vegetacao')
    #     area_total = attrs.get('area_total')
    #     soma_areas = area_agricultavel + area_vegetacao
    #     if soma_areas > area_total:
    #         raise serializers.ValidationError(
    #             "A soma da área agricultável e da vegetação não pode ser maior que a área total da fazenda."
    #         )
    #     return attrs
    
    class Meta:
        model = PropriedadeRural
        exclude = ('produtor',)
        #fields = '__all__'

class ProdutorSerializer(serializers.ModelSerializer):
    propriedades = PropriedadeRuralSerializer(many=True)

    # def validate_doc_identificacao(self, value)-> str:
    #     value_clean = value.replace('.', '').replace('-', '').replace('/', '')
    #     match len(value_clean):
    #         case 11:
    #             cpf = CPF()
    #             if not cpf.validate(value_clean):
    #                 raise serializers.ValidationError("CPF inválido.")
    #         case 14:
    #             cnpj = CNPJ()
    #             if not cnpj.validate(value_clean):
    #                 raise serializers.ValidationError("CNPJ inválido.")
    #         case _:
    #             raise serializers.ValidationError("Documento deve conter 11 (CPF) ou 14 (CNPJ) dígitos.")
    #     return value
    
    # @transaction.atomic
    # def create(self, validated_data) -> Produtor:
    #     propriedades_data = validated_data.pop('propriedades', [])
    #     produtor = Produtor.objects.create(**validated_data)
    #     culturas_instances = []
    #     for prop_data in propriedades_data:
    #         culturas_data = prop_data.pop('culturas', [])
    #         prop_instance = PropriedadeRural.objects.create(produtor=produtor, **prop_data)
    #         for cultura_data in culturas_data:
    #             safra_data = cultura_data.pop('safra')
    #             safra, _ = Safra.objects.get_or_create(**safra_data)
    #             culturas_instances.append(CulturaPlantada(
    #                 nome_cultura=cultura_data['nome_cultura'],
    #                 safra=safra,
    #                 propriedade_rural=prop_instance
    #             ))
    #     CulturaPlantada.objects.bulk_create(culturas_instances)
    #     return produtor
    
    # @transaction.atomic
    # def update(self, instance, validated_data):
    #     propriedades_data = validated_data.pop('propriedades', [])
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #     instance.save()
    #     culturas_instances = []
    #     for prop_data in propriedades_data:
    #         culturas_data = prop_data.pop('culturas', [])
    #         prop_instance, _ = PropriedadeRural.objects.update_or_create(
    #             id=prop_data.get("id"),
    #             defaults={**prop_data, 'produtor': instance}
    #         )
    #         for cultura_data in culturas_data:
    #             safra_data = cultura_data.pop('safra')
    #             safra, _ = Safra.objects.get_or_create(**safra_data)
    #             culturas_instances.append(CulturaPlantada(
    #                 nome_cultura=cultura_data['nome_cultura'],
    #                 safra=safra,
    #                 propriedade_rural=prop_instance
    #             ))
    #     CulturaPlantada.objects.bulk_create(culturas_instances)
    #     return instance

    class Meta:
        model = Produtor
        fields = '__all__'