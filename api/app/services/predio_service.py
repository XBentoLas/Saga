from ..repositories.predio_repository import PredioRepository


class PredioService:
    @staticmethod
    def get_all(filters=None):
        try:
            predios = PredioRepository.get_all(filters)
            return [predio.to_dict() for predio in predios]
        except Exception as e:
            raise Exception(f"Erro ao buscar prédios: {str(e)}")
    
    @staticmethod
    def get_by_id(id):
        try:
            predio = PredioRepository.get_by_id(id)
            if not predio:
                return None
            return predio.to_dict()
        except Exception as e:
            raise Exception(f"Erro ao buscar prédio: {str(e)}")
    
    @staticmethod
    def create(data):
        try:
            required_fields = ['Nome']
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Campo obrigatório ausente: {field}")
            
            predio = PredioRepository.create(data)
            return predio.to_dict()
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Erro ao criar prédio: {str(e)}")
    
    @staticmethod
    def update(id, data):
        try:
            predio = PredioRepository.get_by_id(id)
            if not predio:
                return None
            
            updated_predio = PredioRepository.update(id, data)
            return updated_predio.to_dict()
        except Exception as e:
            raise Exception(f"Erro ao atualizar prédio: {str(e)}")
    
    @staticmethod
    def delete(id):
        try:
            predio = PredioRepository.get_by_id(id)
            if not predio:
                return False
            
            return PredioRepository.delete(id)
        except Exception as e:
            raise Exception(f"Erro ao deletar prédio: {str(e)}")
