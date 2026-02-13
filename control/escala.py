from flask import Flask, Blueprint, request
from sqlalchemy import text
from datetime import datetime


from conf.database import db

escala_bp = Blueprint('escala', __name__, url_prefix = '/escala') 

# -------------------- CRUD escala --------------------
@escala_bp.route("/item", methods=["POST"])
def criar_escala():
    # 1. Coleta os dados
    horario = request.form.get("horario")
    data_front = request.form.get("data")
    matricula_front = request.form.get("matricula")
    posto_front = request.form.get("posto")

    # --- RESTRIÇÃO 1: TODOS OS CAMPOS SÃO OBRIGATÓRIOS ---
    dados_verificacao = {
        "horario": horario,
        "data": data_front,
        "matricula": matricula_front,
        "posto": posto_front
    }

    for campo, valor in dados_verificacao.items():
        if not valor or str(valor).strip() == "":
            return f"Erro: O campo '{campo}' deve ser preenchido.", 400

    # --- RESTRIÇÃO 2: VALIDAÇÃO DE FORMATO DE HORA (HH:MM) ---
    try:
        datetime.strptime(horario, "%H:%M")
    except ValueError:
        return "Erro: O horário deve estar no formato HH:MM (ex: 14:00).", 400

    # --- RESTRIÇÃO 3: VALIDAÇÃO DE FORMATO DE DATA (AAAA-MM-DD) ---
    try:
        # Tenta converter a string para uma data real
        datetime.strptime(data_front, "%Y-%m-%d")
    except ValueError:
        return "Erro: A data deve estar no formato AAAA-MM-DD (ex: 2023-12-31).", 400

    # --- VALIDAÇÃO DE EXISTÊNCIA E COMPATIBILIDADE DE TURNO ---
    sql_func = text("SELECT horario_inicio, horario_fim FROM funcionarios WHERE matricula = :matricula")
    
    try:
        result = db.session.execute(sql_func, {"matricula": matricula_front})
        funcionario = result.mappings().first()
        
        if not funcionario:
            return "Erro: Funcionário não encontrado.", 404
        
        # --- RESTRIÇÃO 4: HORÁRIO DENTRO DO PADRÃO DO FUNCIONÁRIO ---
        if horario < funcionario["horario_inicio"] or horario > funcionario["horario_fim"]:
            return (f"Erro: Horário {horario} fora do turno do funcionário "
                    f"({funcionario['horario_inicio']} às {funcionario['horario_fim']})."), 400
            
    except Exception as e:
        return f"Erro ao consultar funcionário: {str(e)}", 500

    # --- INSERÇÃO NA TABELA ESCALA ---
    sql_insert = text("""
        INSERT INTO escala (horario, data, matricula, posto_id) 
        VALUES (:horario, :data, :matricula, :posto)                
        RETURNING id
    """)
    
    dados_insert = {
        "horario": horario,
        "data": data_front,
        "matricula": matricula_front,
        "posto": posto_front
    }
             
    try:
        result = db.session.execute(sql_insert, dados_insert)
        id_gerado = result.fetchone()[0]
        db.session.commit()

        dados_insert['id'] = id_gerado
        return dados_insert, 201
        
    except Exception as e:
        db.session.rollback()
        return f"Erro ao inserir na escala: {e}", 500

# -------------------- CRUD escala --------------------
# Criar retornando ID (Insert com Returning)
# @escala_bp.route("/item", methods=["POST"])
# def criar_escala():
#     # dados que vieram
#     horario = request.form.get("horario")
#     data_front = request.form.get("data")
#     matricula_front = request.form.get("matricula")
#     posto_front = request.form.get("posto")


#     #validação
#     sql = text("SELECT * FROM funcionarios WHERE matricula = :matricula")
#     dados = {"matricula": matricula_front}
    
#     try:
#         result = db.session.execute(sql, dados)
#         # Mapear todas as colunas para a linha
#         linhas = result.mappings().all()
        
#         if len(linhas) > 0:
#             funcionario = dict(linhas[0])
#             if funcionario["horario_inicio"] > horario or funcionario["horario_fim"] < horario:
#                 return "Horário fora do padrão"
#         else:
#             return "Funcionário não encontrado"
            
#     except Exception as e:
#         return str(e)
#     # SQL
#     sql = text("""
#                 INSERT INTO escala 
#                     (horario, data, matricula, posto_id) 
#                 VALUES 
#                     (:horario, :data, :matricula, :posto)                
#                 RETURNING id
#                 """)
#     dados = {"horario": horario,
#              "data": data_front,
#              "matricula": matricula_front,
#              "posto": posto_front}
             
#     try:
#         # executar consulta
#         result = db.session.execute(sql, dados)
#         db.session.commit()

#         # pega o id
#         id_gerado = result.fetchone()[0]
#         dados['id'] = id_gerado
        
#         return dados
#     except Exception as e:
#         db.session.rollback()
#         return f"Erro: {e}"

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
    
