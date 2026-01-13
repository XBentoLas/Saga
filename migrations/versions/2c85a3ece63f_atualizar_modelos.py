"""Atualizar modelos

Revision ID: 2c85a3ece63f
Revises: 
Create Date: 2026-01-13 17:23:09.946318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c85a3ece63f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create predios table
    op.create_table('predios',
        sa.Column('IdPredio', sa.Integer(), nullable=False),
        sa.Column('Nome', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('IdPredio')
    )

    # Create professores table
    op.create_table('professores',
        sa.Column('IdProfessor', sa.Integer(), nullable=False),
        sa.Column('Nome', sa.String(length=100), nullable=False),
        sa.Column('Email', sa.String(length=120), nullable=False),
        sa.PrimaryKeyConstraint('IdProfessor'),
        sa.UniqueConstraint('Email')
    )

    # Create cursos table
    op.create_table('cursos',
        sa.Column('IdCurso', sa.Integer(), nullable=False),
        sa.Column('Nome', sa.String(length=100), nullable=False),
        sa.Column('codigoCurso', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('IdCurso')
    )

    # Create disciplinas table
    op.create_table('disciplinas',
        sa.Column('IdDisciplina', sa.Integer(), nullable=False),
        sa.Column('Nome', sa.String(length=100), nullable=False),
        sa.Column('codigoDisciplina', sa.String(length=255), nullable=False),
        sa.Column('semestreOfertado', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('IdDisciplina')
    )

    # Create horarios table
    op.create_table('horarios',
        sa.Column('IdHorario', sa.Integer(), nullable=False),
        sa.Column('turno', sa.Enum('MATUTINO', 'VESPERTINO', 'NOTURNO', name='turnoenum'), nullable=False),
        sa.Column('ordem', sa.Integer(), nullable=False),
        sa.Column('HoraInicio', sa.Time(), nullable=False),
        sa.Column('HoraFim', sa.Time(), nullable=False),
        sa.Column('descricao', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('IdHorario')
    )

    # Create salas table
    op.create_table('salas',
        sa.Column('IdSala', sa.Integer(), nullable=False),
        sa.Column('IdPredio', sa.Integer(), nullable=False),
        sa.Column('NumeroSala', sa.String(length=10), nullable=False),
        sa.Column('Capacidade', sa.Integer(), nullable=False),
        sa.Column('TipoSala', sa.String(length=50), nullable=True),
        sa.ForeignKeyConstraint(['IdPredio'], ['predios.IdPredio'], ondelete='RESTRICT'),
        sa.PrimaryKeyConstraint('IdSala')
    )

    # Create agendamentos table
    op.create_table('agendamentos',
        sa.Column('IdAgendamento', sa.Integer(), nullable=False),
        sa.Column('IdSala', sa.Integer(), nullable=False),
        sa.Column('IdHorario', sa.Integer(), nullable=False),
        sa.Column('IdDisciplina', sa.Integer(), nullable=False),
        sa.Column('semestreAno', sa.String(length=255), nullable=False),
        sa.ForeignKeyConstraint(['IdSala'], ['salas.IdSala'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['IdHorario'], ['horarios.IdHorario'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['IdDisciplina'], ['disciplinas.IdDisciplina'], ondelete='RESTRICT'),
        sa.PrimaryKeyConstraint('IdAgendamento')
    )

    # Create disciplinas_cursos table
    op.create_table('disciplinas_cursos',
        sa.Column('IdDisciplina', sa.Integer(), nullable=False),
        sa.Column('IdCurso', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['IdDisciplina'], ['disciplinas.IdDisciplina'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['IdCurso'], ['cursos.IdCurso'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('IdDisciplina', 'IdCurso')
    )

    # Create disciplinas_professores table
    op.create_table('disciplinas_professores',
        sa.Column('IdDisciplina', sa.Integer(), nullable=False),
        sa.Column('IdProfessor', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['IdDisciplina'], ['disciplinas.IdDisciplina'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['IdProfessor'], ['professores.IdProfessor'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('IdDisciplina', 'IdProfessor')
    )

    # Create horarios_professores table
    op.create_table('horarios_professores',
        sa.Column('IdHorarioProfessor', sa.Integer(), nullable=False),
        sa.Column('IdHorario', sa.Integer(), nullable=False),
        sa.Column('IdProfessor', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['IdHorario'], ['horarios.IdHorario']),
        sa.ForeignKeyConstraint(['IdProfessor'], ['professores.IdProfessor']),
        sa.PrimaryKeyConstraint('IdHorarioProfessor')
    )

    # Create agendamentos_professores table
    op.create_table('agendamentos_professores',
        sa.Column('IdAgendamento', sa.Integer(), nullable=False),
        sa.Column('IdProfessor', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['IdAgendamento'], ['agendamentos.IdAgendamento'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['IdProfessor'], ['professores.IdProfessor'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('IdAgendamento', 'IdProfessor')
    )


def downgrade():
    # Drop all tables in reverse order
    op.drop_table('agendamentos_professores')
    op.drop_table('horarios_professores')
    op.drop_table('disciplinas_professores')
    op.drop_table('disciplinas_cursos')
    op.drop_table('agendamentos')
    op.drop_table('salas')
    op.drop_table('horarios')
    op.drop_table('disciplinas')
    op.drop_table('cursos')
    op.drop_table('professores')
    op.drop_table('predios')
