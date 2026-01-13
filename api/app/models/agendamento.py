from .. import db

class Agendamento(db.Model):
    __tablename__ = "agendamentos"

    IdAgendamento = db.Column(db.Integer, primary_key=True)

    IdSala = db.Column(
        db.Integer,
        db.ForeignKey("salas.IdSala", ondelete="RESTRICT"),
        nullable=False
    )

    IdHorario = db.Column(
        db.Integer,
        db.ForeignKey("horarios.IdHorario", ondelete="RESTRICT"),
        nullable=False
    )

    IdDisciplina = db.Column(
        db.Integer,
        db.ForeignKey("disciplinas.IdDisciplina", ondelete="RESTRICT"),
        nullable=False
    )

    semestreAno = db.Column(
        db.String(255),
        nullable=False
    )

    sala = db.relationship("Sala", back_populates="agendamentos")
    horario = db.relationship("Horario", back_populates="agendamentos")
    disciplina = db.relationship("Disciplina", back_populates="agendamentos")

    professores = db.relationship(
        "AgendamentoProfessor",
        back_populates="agendamento",
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.IdAgendamento,
            "sala": self.IdSala,
            "horario": self.IdHorario,
            "disciplina": self.IdDisciplina,
            "semestreAno": self.semestreAno,
            "professores": [
                ap.IdProfessor for ap in self.professores
            ]
        }
