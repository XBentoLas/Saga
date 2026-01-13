from flask import Blueprint, request, jsonify
from ..services.horario_service import HorarioService

horario_bp = Blueprint('horario', __name__, url_prefix='/horarios')


@horario_bp.route('', methods=['GET'])
def get_all_horarios():
    try:
        filters = {}
        if request.args.get('turno'):
            filters['turno'] = request.args.get('turno')
        if request.args.get('ordem'):
            filters['ordem'] = int(request.args.get('ordem'))
        
        horarios = HorarioService.get_all(filters)
        return jsonify({"success": True, "data": horarios}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@horario_bp.route('/<int:id>', methods=['GET'])
def get_horario(id):
    try:
        horario = HorarioService.get_by_id(id)
        if not horario:
            return jsonify({"success": False, "error": "Horário não encontrado"}), 404
        return jsonify({"success": True, "data": horario}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@horario_bp.route('', methods=['POST'])
def create_horario():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        horario = HorarioService.create(data)
        return jsonify({"success": True, "data": horario}), 201
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@horario_bp.route('/<int:id>', methods=['PUT'])
def update_horario(id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        horario = HorarioService.update(id, data)
        if not horario:
            return jsonify({"success": False, "error": "Horário não encontrado"}), 404
        return jsonify({"success": True, "data": horario}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@horario_bp.route('/<int:id>', methods=['DELETE'])
def delete_horario(id):
    try:
        result = HorarioService.delete(id)
        if not result:
            return jsonify({"success": False, "error": "Horário não encontrado"}), 404
        return jsonify({"success": True, "data": {"message": "Horário deletado com sucesso"}}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
