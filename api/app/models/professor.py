from .. import db

class Professor(db.Model):
    __tablename__ = "professores"

    IdProfessor = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(120), unique=True, nullable=False)

    disciplinas = db.relationship(
        "DisciplinaProfessor",
        back_populates="professor"
    )

    agendamentos = db.relationship(
        "AgendamentoProfessor",
        back_populates="professor"
    )

    horarios = db.relationship(
        "HorarioProfessor",
        back_populates="professor"
    )

    def to_dict(self):
        return {
            "id": self.IdProfessor,
            "nome": self.Nome,
            "email": self.Email
        }
