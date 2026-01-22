from ..repositories.agendamento_repository import AgendamentoRepository
from ..repositories.professor_repository import ProfessorRepository
from ..models.agendamento_professor import AgendamentoProfessor
from .. import db


class AgendamentoService:
    @staticmethod
    def get_all(filters=None):
        try:
            agendamentos = AgendamentoRepository.get_all(filters)
            return [agendamento.to_dict() for agendamento in agendamentos]
        except Exception as e:
            raise Exception(f"Erro ao buscar agendamentos: {str(e)}")
    
    @staticmethod
    def get_by_id(id):
        try:
            agendamento = AgendamentoRepository.get_by_id(id)
            if not agendamento:
                return None
            return agendamento.to_dict()
        except Exception as e:
            raise Exception(f"Erro ao buscar agendamento: {str(e)}")
    
    @staticmethod
    def create(data):
        try:
            required_fields = ['IdSala', 'IdHorario', 'IdDisciplina', 'semestreAno']
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Campo obrigatório ausente: {field}")
            
            agendamento = AgendamentoRepository.create(data)
            return agendamento.to_dict()
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Erro ao criar agendamento: {str(e)}")
    
    @staticmethod
    def update(id, data):
        try:
            agendamento = AgendamentoRepository.get_by_id(id)
            if not agendamento:
                return None
            
            updated_agendamento = AgendamentoRepository.update(id, data)
            return updated_agendamento.to_dict()
        except Exception as e:
            raise Exception(f"Erro ao atualizar agendamento: {str(e)}")
    
    @staticmethod
    def delete(id):
        try:
            agendamento = AgendamentoRepository.get_by_id(id)
            if not agendamento:
                return False
            
            return AgendamentoRepository.delete(id)
        except Exception as e:
            raise Exception(f"Erro ao deletar agendamento: {str(e)}")
    
    @staticmethod
    def get_professores(id_agendamento):
        try:
            agendamento = AgendamentoRepository.get_by_id(id_agendamento)
            if not agendamento:
                return None
            
            return [{
                'id': ap.professor.IdProfessor,
                'nome': ap.professor.Nome,
                'email': ap.professor.Email
            } for ap in agendamento.professores]
        except Exception as e:
            raise Exception(f"Erro ao buscar professores do agendamento: {str(e)}")
    
    @staticmethod
    def add_professor(id_agendamento, id_professor):
        try:
            agendamento = AgendamentoRepository.get_by_id(id_agendamento)
            if not agendamento:
                raise ValueError("Agendamento não encontrado")
            
            professor = ProfessorRepository.get_by_id(id_professor)
            if not professor:
                raise ValueError("Professor não encontrado")
            
            existing = AgendamentoProfessor.query.filter_by(
                IdAgendamento=id_agendamento,
                IdProfessor=id_professor
            ).first()
            
            if existing:
                raise ValueError("Professor já está associado a este agendamento")
            
            agendamento_professor = AgendamentoProfessor(
                IdAgendamento=id_agendamento,
                IdProfessor=id_professor
            )
            db.session.add(agendamento_professor)
            db.session.commit()
            
            return {
                'idAgendamento': id_agendamento,
                'idProfessor': id_professor,
                'professor': professor.to_dict()
            }
        except ValueError as e:
            raise e
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Erro ao associar professor ao agendamento: {str(e)}")
    
    @staticmethod
    def remove_professor(id_agendamento, id_professor):
        try:
            agendamento_professor = AgendamentoProfessor.query.filter_by(
                IdAgendamento=id_agendamento,
                IdProfessor=id_professor
            ).first()
            
            if not agendamento_professor:
                return False
            
            db.session.delete(agendamento_professor)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Erro ao remover professor do agendamento: {str(e)}")
