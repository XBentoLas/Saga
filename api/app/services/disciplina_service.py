from ..repositories.disciplina_repository import DisciplinaRepository


class DisciplinaService:
    @staticmethod
    def get_all(filters=None):
        try:
            disciplinas = DisciplinaRepository.get_all(filters)
            return [disciplina.to_dict() for disciplina in disciplinas]
        except Exception as e:
            raise Exception(f"Erro ao buscar disciplinas: {str(e)}")
    
    @staticmethod
    def get_by_id(id):
        try:
            disciplina = DisciplinaRepository.get_by_id(id)
            if not disciplina:
                return None
            return disciplina.to_dict()
        except Exception as e:
            raise Exception(f"Erro ao buscar disciplina: {str(e)}")
    
    @staticmethod
    def create(data):
        try:
            required_fields = ['Nome', 'codigoDisciplina', 'semestreOfertado']
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Campo obrigatório ausente: {field}")
            
            disciplina = DisciplinaRepository.create(data)
            return disciplina.to_dict()
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Erro ao criar disciplina: {str(e)}")
    
    @staticmethod
    def update(id, data):
        try:
            disciplina = DisciplinaRepository.get_by_id(id)
            if not disciplina:
                return None
            
            updated_disciplina = DisciplinaRepository.update(id, data)
            return updated_disciplina.to_dict()
        except Exception as e:
            raise Exception(f"Erro ao atualizar disciplina: {str(e)}")
    
    @staticmethod
    def delete(id):
        try:
            disciplina = DisciplinaRepository.get_by_id(id)
            if not disciplina:
                return False
            
            return DisciplinaRepository.delete(id)
        except Exception as e:
            raise Exception(f"Erro ao deletar disciplina: {str(e)}")
