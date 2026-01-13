from ..repositories.disciplina_professor_repository import DisciplinaProfessorRepository


class DisciplinaProfessorService:
    @staticmethod
    def get_all(filters=None):
        try:
            disciplinas_professores = DisciplinaProfessorRepository.get_all(filters)
            return [{
                'IdDisciplina': dp.IdDisciplina,
                'IdProfessor': dp.IdProfessor
            } for dp in disciplinas_professores]
        except Exception as e:
            raise Exception(f"Erro ao buscar disciplinas-professores: {str(e)}")
    
    @staticmethod
    def get_by_id(id_disciplina, id_professor):
        try:
            dp = DisciplinaProfessorRepository.get_by_id(id_disciplina, id_professor)
            if not dp:
                return None
            return {
                'IdDisciplina': dp.IdDisciplina,
                'IdProfessor': dp.IdProfessor
            }
        except Exception as e:
            raise Exception(f"Erro ao buscar disciplina-professor: {str(e)}")
    
    @staticmethod
    def create(data):
        try:
            required_fields = ['IdDisciplina', 'IdProfessor']
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Campo obrigatório ausente: {field}")
            
            # Check if already exists
            existing = DisciplinaProfessorRepository.get_by_id(
                data['IdDisciplina'],
                data['IdProfessor']
            )
            if existing:
                raise ValueError("Relação já existe")
            
            dp = DisciplinaProfessorRepository.create(data)
            return {
                'IdDisciplina': dp.IdDisciplina,
                'IdProfessor': dp.IdProfessor
            }
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Erro ao criar disciplina-professor: {str(e)}")
    
    @staticmethod
    def delete(id_disciplina, id_professor):
        try:
            dp = DisciplinaProfessorRepository.get_by_id(id_disciplina, id_professor)
            if not dp:
                return False
            
            return DisciplinaProfessorRepository.delete(id_disciplina, id_professor)
        except Exception as e:
            raise Exception(f"Erro ao deletar disciplina-professor: {str(e)}")
