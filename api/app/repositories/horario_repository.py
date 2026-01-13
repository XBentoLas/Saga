from .. import db
from ..models.horario import Horario


class HorarioRepository:
    @staticmethod
    def get_all(filters=None):
        query = Horario.query
        
        if filters:
            if 'turno' in filters:
                query = query.filter(Horario.turno == filters['turno'])
            if 'ordem' in filters:
                query = query.filter(Horario.ordem == filters['ordem'])
        
        return query.order_by(Horario.turno, Horario.ordem).all()
    
    @staticmethod
    def get_by_id(id):
        return Horario.query.get(id)
    
    @staticmethod
    def create(data):
        horario = Horario(**data)
        db.session.add(horario)
        db.session.commit()
        return horario
    
    @staticmethod
    def update(id, data):
        horario = Horario.query.get(id)
        if not horario:
            return None
        
        for key, value in data.items():
            if hasattr(horario, key):
                setattr(horario, key, value)
        
        db.session.commit()
        return horario
    
    @staticmethod
    def delete(id):
        horario = Horario.query.get(id)
        if not horario:
            return False
        
        db.session.delete(horario)
        db.session.commit()
        return True
