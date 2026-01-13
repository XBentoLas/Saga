from flask import Blueprint, request, jsonify
from ..services.agendamento_professor_service import AgendamentoProfessorService

agendamento_professor_bp = Blueprint('agendamento_professor', __name__, url_prefix='/agendamentos-professores')


@agendamento_professor_bp.route('', methods=['GET'])
def get_all_agendamentos_professores():
    try:
        filters = {}
        if request.args.get('IdAgendamento'):
            filters['IdAgendamento'] = int(request.args.get('IdAgendamento'))
        if request.args.get('IdProfessor'):
            filters['IdProfessor'] = int(request.args.get('IdProfessor'))
        
        agendamentos_professores = AgendamentoProfessorService.get_all(filters)
        return jsonify({"success": True, "data": agendamentos_professores}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@agendamento_professor_bp.route('/<int:id_agendamento>/<int:id_professor>', methods=['GET'])
def get_agendamento_professor(id_agendamento, id_professor):
    try:
        ap = AgendamentoProfessorService.get_by_id(id_agendamento, id_professor)
        if not ap:
            return jsonify({"success": False, "error": "Relação não encontrada"}), 404
        return jsonify({"success": True, "data": ap}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@agendamento_professor_bp.route('', methods=['POST'])
def create_agendamento_professor():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        ap = AgendamentoProfessorService.create(data)
        return jsonify({"success": True, "data": ap}), 201
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@agendamento_professor_bp.route('/<int:id_agendamento>/<int:id_professor>', methods=['DELETE'])
def delete_agendamento_professor(id_agendamento, id_professor):
    try:
        result = AgendamentoProfessorService.delete(id_agendamento, id_professor)
        if not result:
            return jsonify({"success": False, "error": "Relação não encontrada"}), 404
        return jsonify({"success": True, "data": {"message": "Relação deletada com sucesso"}}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
