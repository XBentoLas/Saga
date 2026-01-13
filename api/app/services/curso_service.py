from ..repositories.curso_repository import CursoRepository


class CursoService:
    @staticmethod
    def get_all(filters=None):
        try:
            cursos = CursoRepository.get_all(filters)
            return [curso.to_dict() for curso in cursos]
        except Exception as e:
            raise Exception(f"Erro ao buscar cursos: {str(e)}")
    
    @staticmethod
    def get_by_id(id):
        try:
            curso = CursoRepository.get_by_id(id)
            if not curso:
                return None
            return curso.to_dict()
        except Exception as e:
            raise Exception(f"Erro ao buscar curso: {str(e)}")
    
    @staticmethod
    def create(data):
        try:
            required_fields = ['Nome', 'codigoCurso']
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Campo obrigatório ausente: {field}")
            
            curso = CursoRepository.create(data)
            return curso.to_dict()
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Erro ao criar curso: {str(e)}")
    
    @staticmethod
    def update(id, data):
        try:
            curso = CursoRepository.get_by_id(id)
            if not curso:
                return None
            
            updated_curso = CursoRepository.update(id, data)
            return updated_curso.to_dict()
        except Exception as e:
            raise Exception(f"Erro ao atualizar curso: {str(e)}")
    
    @staticmethod
    def delete(id):
        try:
            curso = CursoRepository.get_by_id(id)
            if not curso:
                return False
            
            return CursoRepository.delete(id)
        except Exception as e:
            raise Exception(f"Erro ao deletar curso: {str(e)}")
