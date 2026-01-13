from .. import db

class Sala(db.Model):
    __tablename__ = "salas"

    IdSala = db.Column(db.Integer, primary_key=True)
    IdPredio = db.Column(
        db.Integer,
        db.ForeignKey("predios.IdPredio", ondelete="RESTRICT"),
        nullable=False
    )

    NumeroSala = db.Column(db.String(10), nullable=False)
    Capacidade = db.Column(db.Integer, nullable=False)
    TipoSala = db.Column(db.String(50))

    predio = db.relationship("Predio", back_populates="salas")
    agendamentos = db.relationship("Agendamento", back_populates="sala")

    def to_dict(self):
        return {
            "id": self.IdSala,
            "predio": self.IdPredio,
            "numero": self.NumeroSala,
            "capacidade": self.Capacidade,
            "tipo": self.TipoSala
        }
