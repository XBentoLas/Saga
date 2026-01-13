from flask import Blueprint, request, jsonify
from ..services.disciplina_curso_service import DisciplinaCursoService

disciplina_curso_bp = Blueprint('disciplina_curso', __name__, url_prefix='/disciplinas-cursos')


@disciplina_curso_bp.route('', methods=['GET'])
def get_all_disciplinas_cursos():
    try:
        filters = {}
        if request.args.get('IdDisciplina'):
            filters['IdDisciplina'] = int(request.args.get('IdDisciplina'))
        if request.args.get('IdCurso'):
            filters['IdCurso'] = int(request.args.get('IdCurso'))
        
        disciplinas_cursos = DisciplinaCursoService.get_all(filters)
        return jsonify({"success": True, "data": disciplinas_cursos}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@disciplina_curso_bp.route('/<int:id_disciplina>/<int:id_curso>', methods=['GET'])
def get_disciplina_curso(id_disciplina, id_curso):
    try:
        dc = DisciplinaCursoService.get_by_id(id_disciplina, id_curso)
        if not dc:
            return jsonify({"success": False, "error": "Relação não encontrada"}), 404
        return jsonify({"success": True, "data": dc}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@disciplina_curso_bp.route('', methods=['POST'])
def create_disciplina_curso():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        dc = DisciplinaCursoService.create(data)
        return jsonify({"success": True, "data": dc}), 201
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@disciplina_curso_bp.route('/<int:id_disciplina>/<int:id_curso>', methods=['DELETE'])
def delete_disciplina_curso(id_disciplina, id_curso):
    try:
        result = DisciplinaCursoService.delete(id_disciplina, id_curso)
        if not result:
            return jsonify({"success": False, "error": "Relação não encontrada"}), 404
        return jsonify({"success": True, "data": {"message": "Relação deletada com sucesso"}}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
