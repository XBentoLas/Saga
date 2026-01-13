from .. import db

class AgendamentoProfessor(db.Model):
    __tablename__ = "agendamentos_professores"

    IdAgendamento = db.Column(
        db.Integer,
        db.ForeignKey("agendamentos.IdAgendamento", ondelete="CASCADE"),
        primary_key=True
    )

    IdProfessor = db.Column(
        db.Integer,
        db.ForeignKey("professores.IdProfessor", ondelete="CASCADE"),
        primary_key=True
    )

    agendamento = db.relationship("Agendamento", back_populates="professores")
    professor = db.relationship("Professor", back_populates="agendamentos")
