from flask import Blueprint, request, jsonify
from ..services.disciplina_service import DisciplinaService

disciplina_bp = Blueprint('disciplina', __name__, url_prefix='/disciplinas')


@disciplina_bp.route('', methods=['GET'])
def get_all_disciplinas():
    try:
        filters = {}
        if request.args.get('nome'):
            filters['nome'] = request.args.get('nome')
        if request.args.get('codigoDisciplina'):
            filters['codigoDisciplina'] = request.args.get('codigoDisciplina')
        if request.args.get('semestreOfertado'):
            filters['semestreOfertado'] = request.args.get('semestreOfertado')
        
        disciplinas = DisciplinaService.get_all(filters)
        return jsonify({"success": True, "data": disciplinas}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@disciplina_bp.route('/<int:id>', methods=['GET'])
def get_disciplina(id):
    try:
        disciplina = DisciplinaService.get_by_id(id)
        if not disciplina:
            return jsonify({"success": False, "error": "Disciplina não encontrada"}), 404
        return jsonify({"success": True, "data": disciplina}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@disciplina_bp.route('', methods=['POST'])
def create_disciplina():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        disciplina = DisciplinaService.create(data)
        return jsonify({"success": True, "data": disciplina}), 201
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@disciplina_bp.route('/<int:id>', methods=['PUT'])
def update_disciplina(id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        disciplina = DisciplinaService.update(id, data)
        if not disciplina:
            return jsonify({"success": False, "error": "Disciplina não encontrada"}), 404
        return jsonify({"success": True, "data": disciplina}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@disciplina_bp.route('/<int:id>', methods=['DELETE'])
def delete_disciplina(id):
    try:
        result = DisciplinaService.delete(id)
        if not result:
            return jsonify({"success": False, "error": "Disciplina não encontrada"}), 404
        return jsonify({"success": True, "data": {"message": "Disciplina deletada com sucesso"}}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@disciplina_bp.route('/<int:id>/professores', methods=['GET'])
def get_disciplina_professores(id):
    try:
        professores = DisciplinaService.get_professores(id)
        if professores is None:
            return jsonify({"success": False, "error": "Disciplina não encontrada"}), 404
        return jsonify({"success": True, "data": professores}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@disciplina_bp.route('/<int:id>/professores', methods=['POST'])
def add_professor_to_disciplina(id):
    try:
        data = request.get_json()
        if not data or 'idProfessor' not in data:
            return jsonify({"success": False, "error": "idProfessor é obrigatório"}), 400
        
        result = DisciplinaService.add_professor(id, data['idProfessor'])
        return jsonify({"success": True, "data": result}), 201
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@disciplina_bp.route('/<int:id>/professores/<int:id_professor>', methods=['DELETE'])
def remove_professor_from_disciplina(id, id_professor):
    try:
        result = DisciplinaService.remove_professor(id, id_professor)
        if not result:
            return jsonify({"success": False, "error": "Associação não encontrada"}), 404
        return jsonify({"success": True, "data": {"message": "Professor removido da disciplina com sucesso"}}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
