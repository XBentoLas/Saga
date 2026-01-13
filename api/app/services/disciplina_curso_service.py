from ..repositories.disciplina_curso_repository import DisciplinaCursoRepository


class DisciplinaCursoService:
    @staticmethod
    def get_all(filters=None):
        try:
            disciplinas_cursos = DisciplinaCursoRepository.get_all(filters)
            return [{
                'IdDisciplina': dc.IdDisciplina,
                'IdCurso': dc.IdCurso
            } for dc in disciplinas_cursos]
        except Exception as e:
            raise Exception(f"Erro ao buscar disciplinas-cursos: {str(e)}")
    
    @staticmethod
    def get_by_id(id_disciplina, id_curso):
        try:
            dc = DisciplinaCursoRepository.get_by_id(id_disciplina, id_curso)
            if not dc:
                return None
            return {
                'IdDisciplina': dc.IdDisciplina,
                'IdCurso': dc.IdCurso
            }
        except Exception as e:
            raise Exception(f"Erro ao buscar disciplina-curso: {str(e)}")
    
    @staticmethod
    def create(data):
        try:
            required_fields = ['IdDisciplina', 'IdCurso']
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Campo obrigatório ausente: {field}")
            
            # Check if already exists
            existing = DisciplinaCursoRepository.get_by_id(
                data['IdDisciplina'],
                data['IdCurso']
            )
            if existing:
                raise ValueError("Relação já existe")
            
            dc = DisciplinaCursoRepository.create(data)
            return {
                'IdDisciplina': dc.IdDisciplina,
                'IdCurso': dc.IdCurso
            }
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Erro ao criar disciplina-curso: {str(e)}")
    
    @staticmethod
    def delete(id_disciplina, id_curso):
        try:
            dc = DisciplinaCursoRepository.get_by_id(id_disciplina, id_curso)
            if not dc:
                return False
            
            return DisciplinaCursoRepository.delete(id_disciplina, id_curso)
        except Exception as e:
            raise Exception(f"Erro ao deletar disciplina-curso: {str(e)}")
