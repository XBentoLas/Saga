from flask import Blueprint, request, jsonify
from ..services.agendamento_service import AgendamentoService

agendamento_bp = Blueprint('agendamento', __name__, url_prefix='/agendamentos')


@agendamento_bp.route('', methods=['GET'])
def get_all_agendamentos():
    try:
        filters = {}
        if request.args.get('IdSala'):
            filters['IdSala'] = int(request.args.get('IdSala'))
        if request.args.get('IdHorario'):
            filters['IdHorario'] = int(request.args.get('IdHorario'))
        if request.args.get('IdDisciplina'):
            filters['IdDisciplina'] = int(request.args.get('IdDisciplina'))
        if request.args.get('semestreAno'):
            filters['semestreAno'] = request.args.get('semestreAno')
        
        agendamentos = AgendamentoService.get_all(filters)
        return jsonify({"success": True, "data": agendamentos}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@agendamento_bp.route('/<int:id>', methods=['GET'])
def get_agendamento(id):
    try:
        agendamento = AgendamentoService.get_by_id(id)
        if not agendamento:
            return jsonify({"success": False, "error": "Agendamento não encontrado"}), 404
        return jsonify({"success": True, "data": agendamento}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@agendamento_bp.route('', methods=['POST'])
def create_agendamento():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        agendamento = AgendamentoService.create(data)
        return jsonify({"success": True, "data": agendamento}), 201
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@agendamento_bp.route('/<int:id>', methods=['PUT'])
def update_agendamento(id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        agendamento = AgendamentoService.update(id, data)
        if not agendamento:
            return jsonify({"success": False, "error": "Agendamento não encontrado"}), 404
        return jsonify({"success": True, "data": agendamento}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@agendamento_bp.route('/<int:id>', methods=['DELETE'])
def delete_agendamento(id):
    try:
        result = AgendamentoService.delete(id)
        if not result:
            return jsonify({"success": False, "error": "Agendamento não encontrado"}), 404
        return jsonify({"success": True, "data": {"message": "Agendamento deletado com sucesso"}}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
