from ..repositories.horario_repository import HorarioRepository
from ..repositories.professor_repository import ProfessorRepository
from ..models.horario_professor import HorarioProfessor
from datetime import time
from .. import db


class HorarioService:
    @staticmethod
    def get_all(filters=None):
        try:
            horarios = HorarioRepository.get_all(filters)
            return [horario.to_dict() for horario in horarios]
        except Exception as e:
            raise Exception(f"Erro ao buscar horários: {str(e)}")
    
    @staticmethod
    def get_by_id(id):
        try:
            horario = HorarioRepository.get_by_id(id)
            if not horario:
                return None
            return horario.to_dict()
        except Exception as e:
            raise Exception(f"Erro ao buscar horário: {str(e)}")
    
    @staticmethod
    def create(data):
        try:
            required_fields = ['turno', 'ordem', 'HoraInicio', 'HoraFim', 'descricao']
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Campo obrigatório ausente: {field}")
            
            if isinstance(data.get('HoraInicio'), str):
                h, m = data['HoraInicio'].split(':')
                data['HoraInicio'] = time(int(h), int(m))
            
            if isinstance(data.get('HoraFim'), str):
                h, m = data['HoraFim'].split(':')
                data['HoraFim'] = time(int(h), int(m))
            
            horario = HorarioRepository.create(data)
            return horario.to_dict()
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Erro ao criar horário: {str(e)}")
    
    @staticmethod
    def update(id, data):
        try:
            horario = HorarioRepository.get_by_id(id)
            if not horario:
                return None
            
            if isinstance(data.get('HoraInicio'), str):
                h, m = data['HoraInicio'].split(':')
                data['HoraInicio'] = time(int(h), int(m))
            
            if isinstance(data.get('HoraFim'), str):
                h, m = data['HoraFim'].split(':')
                data['HoraFim'] = time(int(h), int(m))
            
            updated_horario = HorarioRepository.update(id, data)
            return updated_horario.to_dict()
        except Exception as e:
            raise Exception(f"Erro ao atualizar horário: {str(e)}")
    
    @staticmethod
    def delete(id):
        try:
            horario = HorarioRepository.get_by_id(id)
            if not horario:
                return False
            
            return HorarioRepository.delete(id)
        except Exception as e:
            raise Exception(f"Erro ao deletar horário: {str(e)}")
    
    @staticmethod
    def get_professores(id_horario):
        try:
            horario = HorarioRepository.get_by_id(id_horario)
            if not horario:
                return None
            
            return [{
                'id': hp.professor.IdProfessor,
                'nome': hp.professor.Nome,
                'email': hp.professor.Email,
                'idHorarioProfessor': hp.IdHorarioProfessor
            } for hp in horario.professores]
        except Exception as e:
            raise Exception(f"Erro ao buscar professores do horário: {str(e)}")
    
    @staticmethod
    def add_professor(id_horario, id_professor):
        try:
            horario = HorarioRepository.get_by_id(id_horario)
            if not horario:
                raise ValueError("Horário não encontrado")
            
            professor = ProfessorRepository.get_by_id(id_professor)
            if not professor:
                raise ValueError("Professor não encontrado")
            
            existing = HorarioProfessor.query.filter_by(
                IdHorario=id_horario,
                IdProfessor=id_professor
            ).first()
            
            if existing:
                raise ValueError("Professor já está associado a este horário")
            
            horario_professor = HorarioProfessor(
                IdHorario=id_horario,
                IdProfessor=id_professor
            )
            db.session.add(horario_professor)
            db.session.commit()
            
            return {
                'idHorarioProfessor': horario_professor.IdHorarioProfessor,
                'idHorario': id_horario,
                'idProfessor': id_professor,
                'professor': professor.to_dict()
            }
        except ValueError as e:
            raise e
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Erro ao associar professor ao horário: {str(e)}")
    
    @staticmethod
    def remove_professor(id_horario, id_professor):
        try:
            horario_professor = HorarioProfessor.query.filter_by(
                IdHorario=id_horario,
                IdProfessor=id_professor
            ).first()
            
            if not horario_professor:
                return False
            
            db.session.delete(horario_professor)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Erro ao remover professor do horário: {str(e)}")
