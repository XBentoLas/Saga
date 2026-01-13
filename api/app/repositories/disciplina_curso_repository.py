from .. import db
from ..models.disciplina_curso import DisciplinaCurso


class DisciplinaCursoRepository:
    @staticmethod
    def get_all(filters=None):
        query = DisciplinaCurso.query
        
        if filters:
            if 'IdDisciplina' in filters:
                query = query.filter(DisciplinaCurso.IdDisciplina == filters['IdDisciplina'])
            if 'IdCurso' in filters:
                query = query.filter(DisciplinaCurso.IdCurso == filters['IdCurso'])
        
        return query.all()
    
    @staticmethod
    def get_by_id(id_disciplina, id_curso):
        return DisciplinaCurso.query.filter_by(
            IdDisciplina=id_disciplina,
            IdCurso=id_curso
        ).first()
    
    @staticmethod
    def create(data):
        disciplina_curso = DisciplinaCurso(**data)
        db.session.add(disciplina_curso)
        db.session.commit()
        return disciplina_curso
    
    @staticmethod
    def delete(id_disciplina, id_curso):
        disciplina_curso = DisciplinaCurso.query.filter_by(
            IdDisciplina=id_disciplina,
            IdCurso=id_curso
        ).first()
        
        if not disciplina_curso:
            return False
        
        db.session.delete(disciplina_curso)
        db.session.commit()
        return True
