from ..repositories.disciplina_repository import DisciplinaRepository
from ..repositories.professor_repository import ProfessorRepository
from ..models.disciplina_professor import DisciplinaProfessor
from .. import db


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
    
    @staticmethod
    def get_professores(id_disciplina):
        try:
            disciplina = DisciplinaRepository.get_by_id(id_disciplina)
            if not disciplina:
                return None
            
            return [{
                'id': dp.professor.IdProfessor,
                'nome': dp.professor.Nome,
                'email': dp.professor.Email
            } for dp in disciplina.professores]
        except Exception as e:
            raise Exception(f"Erro ao buscar professores da disciplina: {str(e)}")
    
    @staticmethod
    def add_professor(id_disciplina, id_professor):
        try:
            disciplina = DisciplinaRepository.get_by_id(id_disciplina)
            if not disciplina:
                raise ValueError("Disciplina não encontrada")
            
            professor = ProfessorRepository.get_by_id(id_professor)
            if not professor:
                raise ValueError("Professor não encontrado")
            
            existing = DisciplinaProfessor.query.filter_by(
                IdDisciplina=id_disciplina,
                IdProfessor=id_professor
            ).first()
            
            if existing:
                raise ValueError("Professor já está associado a esta disciplina")
            
            disciplina_professor = DisciplinaProfessor(
                IdDisciplina=id_disciplina,
                IdProfessor=id_professor
            )
            db.session.add(disciplina_professor)
            db.session.commit()
            
            return {
                'idDisciplina': id_disciplina,
                'idProfessor': id_professor,
                'professor': professor.to_dict()
            }
        except ValueError as e:
            raise e
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Erro ao associar professor à disciplina: {str(e)}")
    
    @staticmethod
    def remove_professor(id_disciplina, id_professor):
        try:
            disciplina_professor = DisciplinaProfessor.query.filter_by(
                IdDisciplina=id_disciplina,
                IdProfessor=id_professor
            ).first()
            
            if not disciplina_professor:
                return False
            
            db.session.delete(disciplina_professor)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Erro ao remover professor da disciplina: {str(e)}")
