from .. import db

class Curso(db.Model):
    __tablename__ = "cursos"

    IdCurso = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(100), nullable=False)
    codigoCurso = db.Column(db.String(255), nullable=False)

    disciplinas = db.relationship(
        "DisciplinaCurso",
        back_populates="curso",
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.IdCurso,
            "nome": self.Nome,
            "codigoCurso": self.codigoCurso
        }
