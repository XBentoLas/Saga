from .. import db
from ..models.curso import Curso


class CursoRepository:
    @staticmethod
    def get_all(filters=None):
        query = Curso.query
        
        if filters:
            if 'nome' in filters:
                query = query.filter(Curso.Nome.ilike(f"%{filters['nome']}%"))
            if 'codigoCurso' in filters:
                query = query.filter(Curso.codigoCurso == filters['codigoCurso'])
        
        return query.all()
    
    @staticmethod
    def get_by_id(id):
        return Curso.query.get(id)
    
    @staticmethod
    def create(data):
        curso = Curso(**data)
        db.session.add(curso)
        db.session.commit()
        return curso
    
    @staticmethod
    def update(id, data):
        curso = Curso.query.get(id)
        if not curso:
            return None
        
        for key, value in data.items():
            if hasattr(curso, key):
                setattr(curso, key, value)
        
        db.session.commit()
        return curso
    
    @staticmethod
    def delete(id):
        curso = Curso.query.get(id)
        if not curso:
            return False
        
        db.session.delete(curso)
        db.session.commit()
        return True
