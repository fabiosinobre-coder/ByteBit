from flask import Blueprint, jsonify, request
from database import estoque

### Criamos um Blueprint para organizar as rotas do inventário
inventory_bp = Blueprint('inventory', __name__)

### --- READ ALL (Listar todo o estoque) ---
@inventory_bp.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(estoque), 200

### --- READ ONE (Ver um item específico) ---
@inventory_bp.route('/produtos/<int:id_produto>', methods=['GET'])
def obter_produto(id_produto):
    for produto in estoque:
        if produto['id'] == id_produto:
            return jsonify(produto), 200
    return jsonify({"erro": "Produto não encontrado no estoque da ByteBite"}), 404

### --- CREATE (Adicionar novo ingrediente) ---
@inventory_bp.route('/produtos', methods=['POST'])
def adicionar_produto():
    dados = request.get_json()
    
    ### CORREÇÃO AQUI: Quebra de linha e indentação ajustadas
    novo_id = estoque[-1]['id'] + 1 if estoque else 1
    
    novo_produto = {
        "id": novo_id,
        "nome": dados.get('nome'),
        "quantidade": dados.get('quantidade')
    }
    estoque.append(novo_produto)
    return jsonify(novo_produto), 201

# --- UPDATE (Atualizar quantidade ou nome) ---
@inventory_bp.route('/produtos/<int:id_produto>', methods=['PUT'])
def atualizar_produto(id_produto):
    dados = request.get_json()
    for produto in estoque:
        if produto['id'] == id_produto:
            produto['nome'] = dados.get('nome', produto['nome'])
            produto['quantidade'] = dados.get('quantidade', produto['quantidade'])
            return jsonify(produto), 200
    return jsonify({"erro": "Produto não encontrado para atualização"}), 404

# --- DELETE (Remover item do estoque) ---
@inventory_bp.route('/produtos/<int:id_produto>', methods=['DELETE'])
def deletar_produto(id_produto):
    for produto in estoque:
        if produto['id'] == id_produto:
            estoque.remove(produto)
            return jsonify({"mensagem": "Item removido com sucesso!"}), 200
    return jsonify({"erro": "Produto não encontrado para remoção"}), 404