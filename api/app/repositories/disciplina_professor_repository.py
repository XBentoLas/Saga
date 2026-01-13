from .. import db
from ..models.disciplina_professor import DisciplinaProfessor


class DisciplinaProfessorRepository:
    @staticmethod
    def get_all(filters=None):
        query = DisciplinaProfessor.query
        
        if filters:
            if 'IdDisciplina' in filters:
                query = query.filter(DisciplinaProfessor.IdDisciplina == filters['IdDisciplina'])
            if 'IdProfessor' in filters:
                query = query.filter(DisciplinaProfessor.IdProfessor == filters['IdProfessor'])
        
        return query.all()
    
    @staticmethod
    def get_by_id(id_disciplina, id_professor):
        return DisciplinaProfessor.query.filter_by(
            IdDisciplina=id_disciplina,
            IdProfessor=id_professor
        ).first()
    
    @staticmethod
    def create(data):
        disciplina_professor = DisciplinaProfessor(**data)
        db.session.add(disciplina_professor)
        db.session.commit()
        return disciplina_professor
    
    @staticmethod
    def delete(id_disciplina, id_professor):
        disciplina_professor = DisciplinaProfessor.query.filter_by(
            IdDisciplina=id_disciplina,
            IdProfessor=id_professor
        ).first()
        
        if not disciplina_professor:
            return False
        
        db.session.delete(disciplina_professor)
        db.session.commit()
        return True
