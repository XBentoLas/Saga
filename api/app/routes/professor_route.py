from flask import Blueprint, request, jsonify
from ..services.professor_services import ProfessorService

professor_bp = Blueprint('professor', __name__, url_prefix='/professores')


@professor_bp.route('', methods=['GET'])
def get_all_professores():
    try:
        filters = {}
        if request.args.get('nome'):
            filters['nome'] = request.args.get('nome')
        if request.args.get('email'):
            filters['email'] = request.args.get('email')
        
        professores = ProfessorService.get_all(filters)
        return jsonify({"success": True, "data": professores}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@professor_bp.route('/<int:id>', methods=['GET'])
def get_professor(id):
    try:
        professor = ProfessorService.get_by_id(id)
        if not professor:
            return jsonify({"success": False, "error": "Professor não encontrado"}), 404
        return jsonify({"success": True, "data": professor}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@professor_bp.route('', methods=['POST'])
def create_professor():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        professor = ProfessorService.create(data)
        return jsonify({"success": True, "data": professor}), 201
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@professor_bp.route('/<int:id>', methods=['PUT'])
def update_professor(id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        professor = ProfessorService.update(id, data)
        if not professor:
            return jsonify({"success": False, "error": "Professor não encontrado"}), 404
        return jsonify({"success": True, "data": professor}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@professor_bp.route('/<int:id>', methods=['DELETE'])
def delete_professor(id):
    try:
        result = ProfessorService.delete(id)
        if not result:
            return jsonify({"success": False, "error": "Professor não encontrado"}), 404
        return jsonify({"success": True, "data": {"message": "Professor deletado com sucesso"}}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
