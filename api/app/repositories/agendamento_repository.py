from .. import db
from ..models.agendamento import Agendamento


class AgendamentoRepository:
    @staticmethod
    def get_all(filters=None):
        query = Agendamento.query
        
        if filters:
            if 'IdSala' in filters:
                query = query.filter(Agendamento.IdSala == filters['IdSala'])
            if 'IdHorario' in filters:
                query = query.filter(Agendamento.IdHorario == filters['IdHorario'])
            if 'IdDisciplina' in filters:
                query = query.filter(Agendamento.IdDisciplina == filters['IdDisciplina'])
            if 'semestreAno' in filters:
                query = query.filter(Agendamento.semestreAno == filters['semestreAno'])
        
        return query.all()
    
    @staticmethod
    def get_by_id(id):
        return Agendamento.query.get(id)
    
    @staticmethod
    def create(data):
        agendamento = Agendamento(**data)
        db.session.add(agendamento)
        db.session.commit()
        return agendamento
    
    @staticmethod
    def update(id, data):
        agendamento = Agendamento.query.get(id)
        if not agendamento:
            return None
        
        for key, value in data.items():
            if hasattr(agendamento, key):
                setattr(agendamento, key, value)
        
        db.session.commit()
        return agendamento
    
    @staticmethod
    def delete(id):
        agendamento = Agendamento.query.get(id)
        if not agendamento:
            return False
        
        db.session.delete(agendamento)
        db.session.commit()
        return True
