from ..repositories.horario_professor_repository import HorarioProfessorRepository


class HorarioProfessorService:
    @staticmethod
    def get_all(filters=None):
        try:
            horarios_professores = HorarioProfessorRepository.get_all(filters)
            return [{
                'IdHorarioProfessor': hp.IdHorarioProfessor,
                'IdHorario': hp.IdHorario,
                'IdProfessor': hp.IdProfessor
            } for hp in horarios_professores]
        except Exception as e:
            raise Exception(f"Erro ao buscar horários-professores: {str(e)}")
    
    @staticmethod
    def get_by_id(id):
        try:
            hp = HorarioProfessorRepository.get_by_id(id)
            if not hp:
                return None
            return {
                'IdHorarioProfessor': hp.IdHorarioProfessor,
                'IdHorario': hp.IdHorario,
                'IdProfessor': hp.IdProfessor
            }
        except Exception as e:
            raise Exception(f"Erro ao buscar horário-professor: {str(e)}")
    
    @staticmethod
    def create(data):
        try:
            required_fields = ['IdHorario', 'IdProfessor']
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Campo obrigatório ausente: {field}")
            
            hp = HorarioProfessorRepository.create(data)
            return {
                'IdHorarioProfessor': hp.IdHorarioProfessor,
                'IdHorario': hp.IdHorario,
                'IdProfessor': hp.IdProfessor
            }
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Erro ao criar horário-professor: {str(e)}")
    
    @staticmethod
    def update(id, data):
        try:
            hp = HorarioProfessorRepository.get_by_id(id)
            if not hp:
                return None
            
            updated_hp = HorarioProfessorRepository.update(id, data)
            return {
                'IdHorarioProfessor': updated_hp.IdHorarioProfessor,
                'IdHorario': updated_hp.IdHorario,
                'IdProfessor': updated_hp.IdProfessor
            }
        except Exception as e:
            raise Exception(f"Erro ao atualizar horário-professor: {str(e)}")
    
    @staticmethod
    def delete(id):
        try:
            hp = HorarioProfessorRepository.get_by_id(id)
            if not hp:
                return False
            
            return HorarioProfessorRepository.delete(id)
        except Exception as e:
            raise Exception(f"Erro ao deletar horário-professor: {str(e)}")
