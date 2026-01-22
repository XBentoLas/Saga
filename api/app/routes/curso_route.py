from flask import Blueprint, request, jsonify
from ..services.curso_service import CursoService

curso_bp = Blueprint('curso', __name__, url_prefix='/cursos')


@curso_bp.route('', methods=['GET'])
def get_all_cursos():
    try:
        filters = {}
        if request.args.get('nome'):
            filters['nome'] = request.args.get('nome')
        if request.args.get('codigoCurso'):
            filters['codigoCurso'] = request.args.get('codigoCurso')
        
        cursos = CursoService.get_all(filters)
        return jsonify({"success": True, "data": cursos}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@curso_bp.route('/<int:id>', methods=['GET'])
def get_curso(id):
    try:
        curso = CursoService.get_by_id(id)
        if not curso:
            return jsonify({"success": False, "error": "Curso não encontrado"}), 404
        return jsonify({"success": True, "data": curso}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@curso_bp.route('', methods=['POST'])
def create_curso():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        curso = CursoService.create(data)
        return jsonify({"success": True, "data": curso}), 201
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@curso_bp.route('/<int:id>', methods=['PUT'])
def update_curso(id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        curso = CursoService.update(id, data)
        if not curso:
            return jsonify({"success": False, "error": "Curso não encontrado"}), 404
        return jsonify({"success": True, "data": curso}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@curso_bp.route('/<int:id>', methods=['DELETE'])
def delete_curso(id):
    try:
        result = CursoService.delete(id)
        if not result:
            return jsonify({"success": False, "error": "Curso não encontrado"}), 404
        return jsonify({"success": True, "data": {"message": "Curso deletado com sucesso"}}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@curso_bp.route('/<int:id>/disciplinas', methods=['GET'])
def get_curso_disciplinas(id):
    try:
        disciplinas = CursoService.get_disciplinas(id)
        if disciplinas is None:
            return jsonify({"success": False, "error": "Curso não encontrado"}), 404
        return jsonify({"success": True, "data": disciplinas}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@curso_bp.route('/<int:id>/disciplinas', methods=['POST'])
def add_disciplina_to_curso(id):
    try:
        data = request.get_json()
        if not data or 'idDisciplina' not in data:
            return jsonify({"success": False, "error": "idDisciplina é obrigatório"}), 400
        
        result = CursoService.add_disciplina(id, data['idDisciplina'])
        return jsonify({"success": True, "data": result}), 201
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@curso_bp.route('/<int:id>/disciplinas/<int:id_disciplina>', methods=['DELETE'])
def remove_disciplina_from_curso(id, id_disciplina):
    try:
        result = CursoService.remove_disciplina(id, id_disciplina)
        if not result:
            return jsonify({"success": False, "error": "Associação não encontrada"}), 404
        return jsonify({"success": True, "data": {"message": "Disciplina removida do curso com sucesso"}}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
