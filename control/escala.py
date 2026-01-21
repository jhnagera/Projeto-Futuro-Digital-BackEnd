from flask import Flask, Blueprint, request
from sqlalchemy import text

from conf.database import db

escala_bp = Blueprint('escala', __name__, url_prefix = '/escala') 


# -------------------- CRUD escala --------------------
# Criar retornando ID (Insert com Returning)
@escala_bp.route("/", methods=["POST"])
def criar_escala():
    # dados que vieram
    nome_front = request.form.get("horario")
    data_front = request.form.get("data")
    matricula_front = request.form.get("matricula")
    posto_front = request.form.get("posto")

    # SQL
    sql = text("""
                INSERT INTO escala 
                    (horario, data, matricula, posto) 
                VALUES 
                    (:horario, :data, :matricula, :posto)                
                RETURNING id
                """)
    dados = {"horario": nome_front,
             "data": data_front,
             "matricula": matricula_front,
             "posto": posto_front}
             
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
@escala_bp.route('/<id>')
def get_escala(id):
    sql = text("SELECT * FROM escala WHERE id = :id")
    dados = {"id": id}
    
    try:
        result = db.session.execute(sql, dados)
        # Mapear todas as colunas para a linha
        linhas = result.mappings().all()
        
        if len(linhas) > 0:
            return dict(linhas[0])
        else:
            return "escala não encontrada"
            
    except Exception as e:
        return str(e)

# Ler todos (Select All)
@escala_bp.route('/all')
def get_all_escala():
    sql_query = text("SELECT * FROM escala")
    
    try:
        result = db.session.execute(sql_query)
        
        relatorio = result.mappings().all()
        json_output = [dict(row) for row in relatorio] # Converte linhas em lista de dicionários

        return json_output
    except Exception as e:
        return []

# Atualizar (Update)
@escala_bp.route("/<id>", methods=["PUT"])
def atualizar_escala(id):
    # dados que vieram
    horario = request.form.get("Nome")
    data = request.form.get("Descrição")
    matricula = request.form.get("Descrição")
    posto = request.form.get("Descrição")
    sql = text("""UPDATE escala SET 
                        horario = :horario, data = :data, matricula = :matricula, posto = :posto
                    WHERE id = :id""")

    dados = {"horario": horario, "data": data, "matricula": matricula, "posto": posto, "id": id}

    try:
        result = db.session.execute(sql, dados)
        linhas_afetadas = result.rowcount 

        if linhas_afetadas == 1: 
            db.session.commit()
            return f"Escala {id} atualizada com sucesso"
        else:
            db.session.rollback()
            return f"Escala não encontrada ou erro ao atualizar"
    except Exception as e:
        return str(e)

# Deletar (Delete)
@escala_bp.route("/<id>", methods=['DELETE'])
def delete_escala(id):
    sql = text("DELETE FROM escala WHERE id = :id")
    dados = {"id": id}

    try:
        result = db.session.execute(sql, dados)
        linhas_afetadas = result.rowcount 

        if linhas_afetadas == 1: 
            db.session.commit()
            return f"Escala {id} removida"
        else:
            db.session.rollback()
            return f"Erro: Escala não encontrada para deletar"
    except Exception as e:
        return str(e)
    
