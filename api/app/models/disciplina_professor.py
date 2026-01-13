from .. import db

class DisciplinaProfessor(db.Model):
    __tablename__ = "disciplinas_professores"

    IdDisciplina = db.Column(
        db.Integer,
        db.ForeignKey("disciplinas.IdDisciplina", ondelete="CASCADE"),
        primary_key=True
    )
    IdProfessor = db.Column(
        db.Integer,
        db.ForeignKey("professores.IdProfessor", ondelete="CASCADE"),
        primary_key=True
    )

    disciplina = db.relationship("Disciplina", back_populates="professores")
    professor = db.relationship("Professor", back_populates="disciplinas")
