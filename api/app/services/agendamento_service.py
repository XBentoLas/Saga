from ..repositories.agendamento_repository import AgendamentoRepository


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
