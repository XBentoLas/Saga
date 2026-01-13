from .. import db

class Disciplina(db.Model):
    __tablename__ = "disciplinas"

    IdDisciplina = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(100), nullable=False)
    codigoDisciplina = db.Column(db.String(255), nullable=False)
    semestreOfertado = db.Column(db.String(255), nullable=False)

    cursos = db.relationship(
        "DisciplinaCurso",
        back_populates="disciplina"
    )

    professores = db.relationship(
        "DisciplinaProfessor",
        back_populates="disciplina"
    )

    agendamentos = db.relationship(
        "Agendamento",
        back_populates="disciplina"
    )

    def to_dict(self):
        return {
            "id": self.IdDisciplina,
            "nome": self.Nome,
            "codigoDisciplina": self.codigoDisciplina,
            "semestreOfertado": self.semestreOfertado
        }
