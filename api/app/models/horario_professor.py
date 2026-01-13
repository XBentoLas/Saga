from .. import db

class HorarioProfessor(db.Model):
    __tablename__ = "horarios_professores"

    IdHorarioProfessor = db.Column(db.Integer, primary_key=True)

    IdHorario = db.Column(
        db.Integer,
        db.ForeignKey("horarios.IdHorario"),
        nullable=False
    )
    IdProfessor = db.Column(
        db.Integer,
        db.ForeignKey("professores.IdProfessor"),
        nullable=False
    )

    horario = db.relationship("Horario", back_populates="professores")
    professor = db.relationship("Professor", back_populates="horarios")
