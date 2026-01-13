from .. import db
from ..models.disciplina import Disciplina


class DisciplinaRepository:
    @staticmethod
    def get_all(filters=None):
        query = Disciplina.query
        
        if filters:
            if 'nome' in filters:
                query = query.filter(Disciplina.Nome.ilike(f"%{filters['nome']}%"))
            if 'codigoDisciplina' in filters:
                query = query.filter(Disciplina.codigoDisciplina == filters['codigoDisciplina'])
            if 'semestreOfertado' in filters:
                query = query.filter(Disciplina.semestreOfertado == filters['semestreOfertado'])
        
        return query.all()
    
    @staticmethod
    def get_by_id(id):
        return Disciplina.query.get(id)
    
    @staticmethod
    def create(data):
        disciplina = Disciplina(**data)
        db.session.add(disciplina)
        db.session.commit()
        return disciplina
    
    @staticmethod
    def update(id, data):
        disciplina = Disciplina.query.get(id)
        if not disciplina:
            return None
        
        for key, value in data.items():
            if hasattr(disciplina, key):
                setattr(disciplina, key, value)
        
        db.session.commit()
        return disciplina
    
    @staticmethod
    def delete(id):
        disciplina = Disciplina.query.get(id)
        if not disciplina:
            return False
        
        db.session.delete(disciplina)
        db.session.commit()
        return True
