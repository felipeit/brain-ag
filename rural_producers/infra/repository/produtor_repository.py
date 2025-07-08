from typing import Type
from rural_producers.domain.produtor import Produtor as ProdutorDomain
from rural_producers.models.cultura import CulturaPlantada
from rural_producers.models.produtor import Produtor
from rural_producers.models.propriedade_rural import PropriedadeRural
from rural_producers.models.safra import Safra


class ProdutorRepository:
    def __init__(self, db: Type[Produtor]) -> None:
        self._db = db

    def save(self, produtor: ProdutorDomain) -> None:
        produtor_model = self._db.objects.create(
            id=produtor.id,
            doc_identificacao=produtor.documento,
            nome_produtor=produtor.nome,
            email=produtor.email,
            telefone=produtor.telefone
        )
        propriedades = []
        culturas = []
        for prop in produtor.propriedades:
            prop_model = PropriedadeRural.objects.create(
                produtor=produtor_model,
                nome_fazenda=prop.nome_fazenda,
                cidade=prop.cidade,
                estado=prop.estado,
                area_total=prop.area_total,
                area_agricultavel=prop.area_agricultavel,
                area_vegetacao=prop.area_vegetacao,
            )
            propriedades.append(prop_model)

            for cultura in prop.culturas:
                safra_model, _ = Safra.objects.get_or_create(nome=cultura.safra.descricao)
                culturas.append(CulturaPlantada(
                    nome_cultura=cultura.nome,
                    safra=safra_model,
                    propriedade_rural=prop_model
                ))
        CulturaPlantada.objects.bulk_create(culturas)

    #@transaction.atomic
    def update(self, produtor: ProdutorDomain) -> None:
        produtor_model = self._db.objects.get(doc_identificacao=produtor.documento)
        produtor_model.nome_produtor = produtor.nome
        produtor_model.email = produtor.email
        produtor_model.telefone = produtor.telefone
        produtor_model.save()
        CulturaPlantada.objects.filter(propriedade_rural__produtor=produtor_model).delete()
        PropriedadeRural.objects.filter(produtor=produtor_model).delete()
        culturas = []
        for prop in produtor.propriedades:
            prop_model = PropriedadeRural.objects.create(
                produtor=produtor_model,
                nome_fazenda=prop.nome_fazenda,
                cidade=prop.cidade,
                estado=prop.estado,
                area_total=prop.area_total,
                area_agricultavel=prop.area_agricultavel,
                area_vegetacao=prop.area_vegetacao,
            )
            for cultura in prop.culturas:
                safra_model, _ = Safra.objects.get_or_create(nome=cultura.safra.descricao)
                culturas.append(CulturaPlantada(
                    nome_cultura=cultura.nome,
                    safra=safra_model,
                    propriedade_rural=prop_model
                ))

        CulturaPlantada.objects.bulk_create(culturas)
