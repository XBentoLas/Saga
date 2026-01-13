from ..repositories.horario_repository import HorarioRepository
from datetime import time


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
            
            # Convert string time to time object if needed
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
            
            # Convert string time to time object if needed
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
