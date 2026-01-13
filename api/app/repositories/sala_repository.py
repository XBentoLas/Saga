from .. import db
from ..models.sala import Sala


class SalaRepository:
    @staticmethod
    def get_all(filters=None):
        query = Sala.query
        
        if filters:
            if 'NumeroSala' in filters:
                query = query.filter(Sala.NumeroSala.ilike(f"%{filters['NumeroSala']}%"))
            if 'IdPredio' in filters:
                query = query.filter(Sala.IdPredio == filters['IdPredio'])
            if 'TipoSala' in filters:
                query = query.filter(Sala.TipoSala.ilike(f"%{filters['TipoSala']}%"))
        
        return query.all()
    
    @staticmethod
    def get_by_id(id):
        return Sala.query.get(id)
    
    @staticmethod
    def create(data):
        sala = Sala(**data)
        db.session.add(sala)
        db.session.commit()
        return sala
    
    @staticmethod
    def update(id, data):
        sala = Sala.query.get(id)
        if not sala:
            return None
        
        for key, value in data.items():
            if hasattr(sala, key):
                setattr(sala, key, value)
        
        db.session.commit()
        return sala
    
    @staticmethod
    def delete(id):
        sala = Sala.query.get(id)
        if not sala:
            return False
        
        db.session.delete(sala)
        db.session.commit()
        return True
