from .. import db
from ..models.professor import Professor


class ProfessorRepository:
    @staticmethod
    def get_all(filters=None):
        query = Professor.query
        
        if filters:
            if 'nome' in filters:
                query = query.filter(Professor.Nome.ilike(f"%{filters['nome']}%"))
            if 'email' in filters:
                query = query.filter(Professor.Email.ilike(f"%{filters['email']}%"))
        
        return query.all()
    
    @staticmethod
    def get_by_id(id):
        return Professor.query.get(id)
    
    @staticmethod
    def create(data):
        professor = Professor(**data)
        db.session.add(professor)
        db.session.commit()
        return professor
    
    @staticmethod
    def update(id, data):
        professor = Professor.query.get(id)
        if not professor:
            return None
        
        for key, value in data.items():
            if hasattr(professor, key):
                setattr(professor, key, value)
        
        db.session.commit()
        return professor
    
    @staticmethod
    def delete(id):
        professor = Professor.query.get(id)
        if not professor:
            return False
        
        db.session.delete(professor)
        db.session.commit()
        return True
