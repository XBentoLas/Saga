from ..repositories.curso_repository import CursoRepository
from ..repositories.disciplina_repository import DisciplinaRepository
from ..models.disciplina_curso import DisciplinaCurso
from .. import db


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
    
    @staticmethod
    def get_disciplinas(id_curso):
        try:
            curso = CursoRepository.get_by_id(id_curso)
            if not curso:
                return None
            
            return [{
                'id': dc.disciplina.IdDisciplina,
                'nome': dc.disciplina.Nome,
                'codigoDisciplina': dc.disciplina.codigoDisciplina,
                'semestreOfertado': dc.disciplina.semestreOfertado
            } for dc in curso.disciplinas]
        except Exception as e:
            raise Exception(f"Erro ao buscar disciplinas do curso: {str(e)}")
    
    @staticmethod
    def add_disciplina(id_curso, id_disciplina):
        try:
            curso = CursoRepository.get_by_id(id_curso)
            if not curso:
                raise ValueError("Curso não encontrado")
            
            disciplina = DisciplinaRepository.get_by_id(id_disciplina)
            if not disciplina:
                raise ValueError("Disciplina não encontrada")
            
            existing = DisciplinaCurso.query.filter_by(
                IdDisciplina=id_disciplina,
                IdCurso=id_curso
            ).first()
            
            if existing:
                raise ValueError("Disciplina já está associada a este curso")
            
            disciplina_curso = DisciplinaCurso(
                IdDisciplina=id_disciplina,
                IdCurso=id_curso
            )
            db.session.add(disciplina_curso)
            db.session.commit()
            
            return {
                'idCurso': id_curso,
                'idDisciplina': id_disciplina,
                'disciplina': disciplina.to_dict()
            }
        except ValueError as e:
            raise e
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Erro ao associar disciplina ao curso: {str(e)}")
    
    @staticmethod
    def remove_disciplina(id_curso, id_disciplina):
        try:
            disciplina_curso = DisciplinaCurso.query.filter_by(
                IdDisciplina=id_disciplina,
                IdCurso=id_curso
            ).first()
            
            if not disciplina_curso:
                return False
            
            db.session.delete(disciplina_curso)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Erro ao remover disciplina do curso: {str(e)}")
