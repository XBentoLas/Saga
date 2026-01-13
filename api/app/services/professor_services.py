from ..repositories.professor_repository import ProfessorRepository


class ProfessorService:
    @staticmethod
    def get_all(filters=None):
        try:
            professores = ProfessorRepository.get_all(filters)
            return [professor.to_dict() for professor in professores]
        except Exception as e:
            raise Exception(f"Erro ao buscar professores: {str(e)}")
    
    @staticmethod
    def get_by_id(id):
        try:
            professor = ProfessorRepository.get_by_id(id)
            if not professor:
                return None
            return professor.to_dict()
        except Exception as e:
            raise Exception(f"Erro ao buscar professor: {str(e)}")
    
    @staticmethod
    def create(data):
        try:
            required_fields = ['Nome', 'Email']
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Campo obrigatório ausente: {field}")
            
            professor = ProfessorRepository.create(data)
            return professor.to_dict()
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Erro ao criar professor: {str(e)}")
    
    @staticmethod
    def update(id, data):
        try:
            professor = ProfessorRepository.get_by_id(id)
            if not professor:
                return None
            
            updated_professor = ProfessorRepository.update(id, data)
            return updated_professor.to_dict()
        except Exception as e:
            raise Exception(f"Erro ao atualizar professor: {str(e)}")
    
    @staticmethod
    def delete(id):
        try:
            professor = ProfessorRepository.get_by_id(id)
            if not professor:
                return False
            
            return ProfessorRepository.delete(id)
        except Exception as e:
            raise Exception(f"Erro ao deletar professor: {str(e)}")  