from .. import db

class Predio(db.Model):
    __tablename__ = "predios"

    IdPredio = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(100), nullable=False)

    salas = db.relationship(
        "Sala",
        back_populates="predio",
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.IdPredio,
            "nome": self.Nome
        }
