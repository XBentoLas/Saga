from .. import db
from ..models.agendamento_professor import AgendamentoProfessor


class AgendamentoProfessorRepository:
    @staticmethod
    def get_all(filters=None):
        query = AgendamentoProfessor.query
        
        if filters:
            if 'IdAgendamento' in filters:
                query = query.filter(AgendamentoProfessor.IdAgendamento == filters['IdAgendamento'])
            if 'IdProfessor' in filters:
                query = query.filter(AgendamentoProfessor.IdProfessor == filters['IdProfessor'])
        
        return query.all()
    
    @staticmethod
    def get_by_id(id_agendamento, id_professor):
        return AgendamentoProfessor.query.filter_by(
            IdAgendamento=id_agendamento,
            IdProfessor=id_professor
        ).first()
    
    @staticmethod
    def create(data):
        agendamento_professor = AgendamentoProfessor(**data)
        db.session.add(agendamento_professor)
        db.session.commit()
        return agendamento_professor
    
    @staticmethod
    def delete(id_agendamento, id_professor):
        agendamento_professor = AgendamentoProfessor.query.filter_by(
            IdAgendamento=id_agendamento,
            IdProfessor=id_professor
        ).first()
        
        if not agendamento_professor:
            return False
        
        db.session.delete(agendamento_professor)
        db.session.commit()
        return True
