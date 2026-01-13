from flask import Blueprint, request, jsonify
from ..services.predio_service import PredioService

predio_bp = Blueprint('predio', __name__, url_prefix='/predios')


@predio_bp.route('', methods=['GET'])
def get_all_predios():
    try:
        filters = {}
        if request.args.get('nome'):
            filters['nome'] = request.args.get('nome')
        
        predios = PredioService.get_all(filters)
        return jsonify({"success": True, "data": predios}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@predio_bp.route('/<int:id>', methods=['GET'])
def get_predio(id):
    try:
        predio = PredioService.get_by_id(id)
        if not predio:
            return jsonify({"success": False, "error": "Prédio não encontrado"}), 404
        return jsonify({"success": True, "data": predio}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@predio_bp.route('', methods=['POST'])
def create_predio():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        predio = PredioService.create(data)
        return jsonify({"success": True, "data": predio}), 201
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@predio_bp.route('/<int:id>', methods=['PUT'])
def update_predio(id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        predio = PredioService.update(id, data)
        if not predio:
            return jsonify({"success": False, "error": "Prédio não encontrado"}), 404
        return jsonify({"success": True, "data": predio}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@predio_bp.route('/<int:id>', methods=['DELETE'])
def delete_predio(id):
    try:
        result = PredioService.delete(id)
        if not result:
            return jsonify({"success": False, "error": "Prédio não encontrado"}), 404
        return jsonify({"success": True, "data": {"message": "Prédio deletado com sucesso"}}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
