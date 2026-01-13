from ..repositories.agendamento_professor_repository import AgendamentoProfessorRepository


class AgendamentoProfessorService:
    @staticmethod
    def get_all(filters=None):
        try:
            agendamentos_professores = AgendamentoProfessorRepository.get_all(filters)
            return [{
                'IdAgendamento': ap.IdAgendamento,
                'IdProfessor': ap.IdProfessor
            } for ap in agendamentos_professores]
        except Exception as e:
            raise Exception(f"Erro ao buscar agendamentos-professores: {str(e)}")
    
    @staticmethod
    def get_by_id(id_agendamento, id_professor):
        try:
            ap = AgendamentoProfessorRepository.get_by_id(id_agendamento, id_professor)
            if not ap:
                return None
            return {
                'IdAgendamento': ap.IdAgendamento,
                'IdProfessor': ap.IdProfessor
            }
        except Exception as e:
            raise Exception(f"Erro ao buscar agendamento-professor: {str(e)}")
    
    @staticmethod
    def create(data):
        try:
            required_fields = ['IdAgendamento', 'IdProfessor']
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Campo obrigatório ausente: {field}")
            
            # Check if already exists
            existing = AgendamentoProfessorRepository.get_by_id(
                data['IdAgendamento'],
                data['IdProfessor']
            )
            if existing:
                raise ValueError("Relação já existe")
            
            ap = AgendamentoProfessorRepository.create(data)
            return {
                'IdAgendamento': ap.IdAgendamento,
                'IdProfessor': ap.IdProfessor
            }
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Erro ao criar agendamento-professor: {str(e)}")
    
    @staticmethod
    def delete(id_agendamento, id_professor):
        try:
            ap = AgendamentoProfessorRepository.get_by_id(id_agendamento, id_professor)
            if not ap:
                return False
            
            return AgendamentoProfessorRepository.delete(id_agendamento, id_professor)
        except Exception as e:
            raise Exception(f"Erro ao deletar agendamento-professor: {str(e)}")
