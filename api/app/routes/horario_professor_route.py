from flask import Blueprint, request, jsonify
from ..services.horario_professor_service import HorarioProfessorService

horario_professor_bp = Blueprint('horario_professor', __name__, url_prefix='/horarios-professores')


@horario_professor_bp.route('', methods=['GET'])
def get_all_horarios_professores():
    try:
        filters = {}
        if request.args.get('IdHorario'):
            filters['IdHorario'] = int(request.args.get('IdHorario'))
        if request.args.get('IdProfessor'):
            filters['IdProfessor'] = int(request.args.get('IdProfessor'))
        
        horarios_professores = HorarioProfessorService.get_all(filters)
        return jsonify({"success": True, "data": horarios_professores}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@horario_professor_bp.route('/<int:id>', methods=['GET'])
def get_horario_professor(id):
    try:
        hp = HorarioProfessorService.get_by_id(id)
        if not hp:
            return jsonify({"success": False, "error": "Relação não encontrada"}), 404
        return jsonify({"success": True, "data": hp}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@horario_professor_bp.route('', methods=['POST'])
def create_horario_professor():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        hp = HorarioProfessorService.create(data)
        return jsonify({"success": True, "data": hp}), 201
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@horario_professor_bp.route('/<int:id>', methods=['PUT'])
def update_horario_professor(id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        hp = HorarioProfessorService.update(id, data)
        if not hp:
            return jsonify({"success": False, "error": "Relação não encontrada"}), 404
        return jsonify({"success": True, "data": hp}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@horario_professor_bp.route('/<int:id>', methods=['DELETE'])
def delete_horario_professor(id):
    try:
        result = HorarioProfessorService.delete(id)
        if not result:
            return jsonify({"success": False, "error": "Relação não encontrada"}), 404
        return jsonify({"success": True, "data": {"message": "Relação deletada com sucesso"}}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
