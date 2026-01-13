from .. import db
from ..models.horario_professor import HorarioProfessor


class HorarioProfessorRepository:
    @staticmethod
    def get_all(filters=None):
        query = HorarioProfessor.query
        
        if filters:
            if 'IdHorario' in filters:
                query = query.filter(HorarioProfessor.IdHorario == filters['IdHorario'])
            if 'IdProfessor' in filters:
                query = query.filter(HorarioProfessor.IdProfessor == filters['IdProfessor'])
        
        return query.all()
    
    @staticmethod
    def get_by_id(id):
        return HorarioProfessor.query.get(id)
    
    @staticmethod
    def create(data):
        horario_professor = HorarioProfessor(**data)
        db.session.add(horario_professor)
        db.session.commit()
        return horario_professor
    
    @staticmethod
    def update(id, data):
        horario_professor = HorarioProfessor.query.get(id)
        if not horario_professor:
            return None
        
        for key, value in data.items():
            if hasattr(horario_professor, key):
                setattr(horario_professor, key, value)
        
        db.session.commit()
        return horario_professor
    
    @staticmethod
    def delete(id):
        horario_professor = HorarioProfessor.query.get(id)
        if not horario_professor:
            return False
        
        db.session.delete(horario_professor)
        db.session.commit()
        return True
