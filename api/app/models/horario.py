from .. import db
from enum import Enum

class TurnoEnum(str, Enum):
    MATUTINO = "matutino"
    VESPERTINO = "vespertino"
    NOTURNO = "noturno"

class Horario(db.Model):
    __tablename__ = "horarios"

    IdHorario = db.Column(db.Integer, primary_key=True)
    turno = db.Column(db.Enum(TurnoEnum), nullable=False)
    ordem = db.Column(db.Integer, nullable=False)
    HoraInicio = db.Column(db.Time, nullable=False)
    HoraFim = db.Column(db.Time, nullable=False)
    descricao = db.Column(db.String(255), nullable=False)

    professores = db.relationship(
        "HorarioProfessor",
        back_populates="horario"
    )

    agendamentos = db.relationship("Agendamento", back_populates="horario")

    def to_dict(self):
        return {
            "id": self.IdHorario,
            "turno": self.turno.value if self.turno else None,
            "ordem": self.ordem,
            "horaInicio": self.HoraInicio.strftime("%H:%M") if self.HoraInicio else None,
            "horaFim": self.HoraFim.strftime("%H:%M") if self.HoraFim else None,
            "descricao": self.descricao
        }
