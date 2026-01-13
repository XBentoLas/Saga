from flask import Blueprint, request, jsonify
from ..services.sala_service import SalaService

sala_bp = Blueprint('sala', __name__, url_prefix='/salas')


@sala_bp.route('', methods=['GET'])
def get_all_salas():
    try:
        filters = {}
        if request.args.get('NumeroSala'):
            filters['NumeroSala'] = request.args.get('NumeroSala')
        if request.args.get('IdPredio'):
            filters['IdPredio'] = int(request.args.get('IdPredio'))
        if request.args.get('TipoSala'):
            filters['TipoSala'] = request.args.get('TipoSala')
        
        salas = SalaService.get_all(filters)
        return jsonify({"success": True, "data": salas}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@sala_bp.route('/<int:id>', methods=['GET'])
def get_sala(id):
    try:
        sala = SalaService.get_by_id(id)
        if not sala:
            return jsonify({"success": False, "error": "Sala não encontrada"}), 404
        return jsonify({"success": True, "data": sala}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@sala_bp.route('', methods=['POST'])
def create_sala():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        sala = SalaService.create(data)
        return jsonify({"success": True, "data": sala}), 201
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@sala_bp.route('/<int:id>', methods=['PUT'])
def update_sala(id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        sala = SalaService.update(id, data)
        if not sala:
            return jsonify({"success": False, "error": "Sala não encontrada"}), 404
        return jsonify({"success": True, "data": sala}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@sala_bp.route('/<int:id>', methods=['DELETE'])
def delete_sala(id):
    try:
        result = SalaService.delete(id)
        if not result:
            return jsonify({"success": False, "error": "Sala não encontrada"}), 404
        return jsonify({"success": True, "data": {"message": "Sala deletada com sucesso"}}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
