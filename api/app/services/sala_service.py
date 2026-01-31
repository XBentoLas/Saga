from ..repositories.sala_repository import SalaRepository
from ..models.agendamento import Agendamento
from .. import db


class SalaService:
    @staticmethod
    def get_all(filters=None):
        try:
            salas = SalaRepository.get_all(filters)
            return [sala.to_dict() for sala in salas]
        except Exception as e:
            raise Exception(f"Erro ao buscar salas: {str(e)}")
    
    @staticmethod
    def get_by_id(id):
        try:
            sala = SalaRepository.get_by_id(id)
            if not sala:
                return None
            return sala.to_dict()
        except Exception as e:
            raise Exception(f"Erro ao buscar sala: {str(e)}")
    
    @staticmethod
    def create(data):
        try:
            required_fields = ['NumeroSala', 'Capacidade', 'IdPredio']
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Campo obrigatório ausente: {field}")
            
            sala = SalaRepository.create(data)
            return sala.to_dict()
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Erro ao criar sala: {str(e)}")
    
    @staticmethod
    def update(id, data):
        try:
            sala = SalaRepository.get_by_id(id)
            if not sala:
                return None
            
            updated_sala = SalaRepository.update(id, data)
            return updated_sala.to_dict()
        except Exception as e:
            raise Exception(f"Erro ao atualizar sala: {str(e)}")
    
    @staticmethod
    def delete(id):
        try:
            sala = SalaRepository.get_by_id(id)
            if not sala:
                return False
            
            Agendamento.query.filter_by(IdSala=id).delete()
            db.session.commit()
            
            return SalaRepository.delete(id)
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Erro ao deletar sala: {str(e)}")
