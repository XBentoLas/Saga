from .. import db

class DisciplinaCurso(db.Model):
    __tablename__ = "disciplinas_cursos"

    IdDisciplina = db.Column(
        db.Integer,
        db.ForeignKey("disciplinas.IdDisciplina", ondelete="CASCADE"),
        primary_key=True
    )
    IdCurso = db.Column(
        db.Integer,
        db.ForeignKey("cursos.IdCurso", ondelete="CASCADE"),
        primary_key=True
    )

    disciplina = db.relationship("Disciplina", back_populates="cursos")
    curso = db.relationship("Curso", back_populates="disciplinas")
