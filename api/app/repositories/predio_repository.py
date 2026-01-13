from .. import db
from ..models.predio import Predio


class PredioRepository:
    @staticmethod
    def get_all(filters=None):
        query = Predio.query
        
        if filters:
            if 'nome' in filters:
                query = query.filter(Predio.Nome.ilike(f"%{filters['nome']}%"))
        
        return query.all()
    
    @staticmethod
    def get_by_id(id):
        return Predio.query.get(id)
    
    @staticmethod
    def create(data):
        predio = Predio(**data)
        db.session.add(predio)
        db.session.commit()
        return predio
    
    @staticmethod
    def update(id, data):
        predio = Predio.query.get(id)
        if not predio:
            return None
        
        for key, value in data.items():
            if hasattr(predio, key):
                setattr(predio, key, value)
        
        db.session.commit()
        return predio
    
    @staticmethod
    def delete(id):
        predio = Predio.query.get(id)
        if not predio:
            return False
        
        db.session.delete(predio)
        db.session.commit()
        return True
