from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from ..config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

    db.init_app(app)
    migrate.init_app(app, db)

    # Register all blueprints
    from .routes.predio_route import predio_bp
    from .routes.sala_route import sala_bp
    from .routes.professor_route import professor_bp
    from .routes.curso_route import curso_bp
    from .routes.disciplina_route import disciplina_bp
    from .routes.horario_route import horario_bp
    from .routes.agendamento_route import agendamento_bp
    from .routes.disciplina_curso_route import disciplina_curso_bp
    from .routes.disciplina_professor_route import disciplina_professor_bp
    from .routes.horario_professor_route import horario_professor_bp
    from .routes.agendamento_professor_route import agendamento_professor_bp

    app.register_blueprint(predio_bp)
    app.register_blueprint(sala_bp)
    app.register_blueprint(professor_bp)
    app.register_blueprint(curso_bp)
    app.register_blueprint(disciplina_bp)
    app.register_blueprint(horario_bp)
    app.register_blueprint(agendamento_bp)
    app.register_blueprint(disciplina_curso_bp)
    app.register_blueprint(disciplina_professor_bp)
    app.register_blueprint(horario_professor_bp)
    app.register_blueprint(agendamento_professor_bp)

    from .models.predio import Predio
    from .models.sala import Sala
    from .models.disciplina import Disciplina
    from .models.professor import Professor
    from .models.curso import Curso
    from .models.disciplina_curso import DisciplinaCurso
    from .models.disciplina_professor import DisciplinaProfessor
    from .models.horario import Horario
    from .models.horario_professor import HorarioProfessor
    from .models.agendamento import Agendamento
    from .models.agendamento_professor import AgendamentoProfessor

    return app
