from flask import Blueprint, request, jsonify
from ..services.disciplina_professor_service import DisciplinaProfessorService

disciplina_professor_bp = Blueprint('disciplina_professor', __name__, url_prefix='/disciplinas-professores')


@disciplina_professor_bp.route('', methods=['GET'])
def get_all_disciplinas_professores():
    try:
        filters = {}
        if request.args.get('IdDisciplina'):
            filters['IdDisciplina'] = int(request.args.get('IdDisciplina'))
        if request.args.get('IdProfessor'):
            filters['IdProfessor'] = int(request.args.get('IdProfessor'))
        
        disciplinas_professores = DisciplinaProfessorService.get_all(filters)
        return jsonify({"success": True, "data": disciplinas_professores}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@disciplina_professor_bp.route('/<int:id_disciplina>/<int:id_professor>', methods=['GET'])
def get_disciplina_professor(id_disciplina, id_professor):
    try:
        dp = DisciplinaProfessorService.get_by_id(id_disciplina, id_professor)
        if not dp:
            return jsonify({"success": False, "error": "Relação não encontrada"}), 404
        return jsonify({"success": True, "data": dp}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@disciplina_professor_bp.route('', methods=['POST'])
def create_disciplina_professor():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        dp = DisciplinaProfessorService.create(data)
        return jsonify({"success": True, "data": dp}), 201
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@disciplina_professor_bp.route('/<int:id_disciplina>/<int:id_professor>', methods=['DELETE'])
def delete_disciplina_professor(id_disciplina, id_professor):
    try:
        result = DisciplinaProfessorService.delete(id_disciplina, id_professor)
        if not result:
            return jsonify({"success": False, "error": "Relação não encontrada"}), 404
        return jsonify({"success": True, "data": {"message": "Relação deletada com sucesso"}}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
