from flask import Flask, Blueprint, request
from sqlalchemy import text

from conf.database import db

postos_bp = Blueprint('postos', __name__, url_prefix = '/postos') 


# -------------------- CRUD postos --------------------
# Criar retornando ID (Insert com Returning)
@postos_bp.route("/", methods=["POST"])
def criar_postos():
    # dados que vieram
    nome_front = request.form.get("Nome")
    descricao = request.form.get("Descrição")
    posto_especial = request.form.get("posto_especial")

    # SQL
    sql = text("""
                INSERT INTO postos 
                    (nome, descricao, posto_especial) 
                VALUES 
                    (:nome, :descricao, :posto_especial)                
                RETURNING id
                """)
    dados = {"nome": nome_front,
             "descricao": descricao,
             "posto_especial": posto_especial}
             
    try:
        # executar consulta
        result = db.session.execute(sql, dados)
        db.session.commit()

        # pega o id
        id_gerado = result.fetchone()[0]
        dados['id'] = id_gerado
        
        return dados
    except Exception as e:
        db.session.rollback()
        return f"Erro: {e}"

# Ler um (Select by ID)
@postos_bp.route('/<id>')
def get_postos(id):
    sql = text("SELECT * FROM postos WHERE id = :id")
    dados = {"id": id}
    
    try:
        result = db.session.execute(sql, dados)
        # Mapear todas as colunas para a linha
        linhas = result.mappings().all()
        
        if len(linhas) > 0:
            return dict(linhas[0])
        else:
            return "Posto não encontrado"
            
    except Exception as e:
        return str(e)

# Ler todos (Select All)
@postos_bp.route('/all')
def get_all_postos():
    sql_query = text("SELECT * FROM postos")
    
    try:
        result = db.session.execute(sql_query)
        
        relatorio = result.mappings().all()
        json_output = [dict(row) for row in relatorio] # Converte linhas em lista de dicionários

        return json_output
    except Exception as e:
        return []

# Atualizar (Update)
@postos_bp.route("/<id>", methods=["PUT"])
def atualizar_postos(id):
    # dados que vieram
    nome = request.form.get("Nome")
    descricao = request.form.get("Descrição")
    posto_especial = request.form.get("posto_especial")
    sql = text("""UPDATE postos SET 
                        nome = :nome, descricao = :descricao, posto_especial = :posto_especial
                    WHERE id = :id""")

    dados = {"nome": nome, "descricao": descricao, "posto_especial": posto_especial, "id": id}

    try:
        result = db.session.execute(sql, dados)
        linhas_afetadas = result.rowcount 

        if linhas_afetadas == 1: 
            db.session.commit()
            return f"Posto {id} atualizado com sucesso"
        else:
            db.session.rollback()
            return f"Posto não encontrado ou erro ao atualizar"
    except Exception as e:
        return str(e)

# Deletar (Delete)
@postos_bp.route("/<id>", methods=['DELETE'])
def delete_postos(id):
    sql = text("DELETE FROM postos WHERE id = :id")
    dados = {"id": id}

    try:
        result = db.session.execute(sql, dados)
        linhas_afetadas = result.rowcount 

        if linhas_afetadas == 1: 
            db.session.commit()
            return f"Posto {id} removido"
        else:
            db.session.rollback()
            return f"Erro: Posto não encontrado para deletar"
    except Exception as e:
        return str(e)
    
