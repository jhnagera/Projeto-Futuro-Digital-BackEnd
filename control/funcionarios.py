from flask import Flask, Blueprint, request
from sqlalchemy import text

from conf.database import db

funcionarios_bp = Blueprint('funcionarios', __name__, url_prefix = '/funcionarios') 


# -------------------- CRUD funcionarios --------------------
# Criar retornando ID (Insert com Returning)
@funcionarios_bp.route("/", methods=["POST"])
def criar_funcionarios():
    # dados que vieram
    nome_front = request.form.get("nome_funcionario")
    email = request.form.get("email")
    matricula = request.form.get("matricula")
    apelido = request.form.get("apelido")
    senha = request.form.get("senha")
    # SQL
    sql = text("""
                INSERT INTO funcionarios 
                    (nome_completo, email, matricula, apelido, senha) 
                VALUES 
                    (:nome_temp, :email, :matricula, :apelido, :senha) 
                RETURNING id
                
                """)
    dados = {"nome_temp": nome_front, "email": email, "matricula": matricula, "apelido": apelido, "senha": senha}

    try:
        # executar consulta
        result = db.session.execute(sql, dados)
        db.session.commit()

        # pega o id
        #id_gerado = result.fetchone()[0]
        #dados['id'] = id_gerado
        
        return dados
    except Exception as e:
        return f"Erro: {e}"

# Ler um (Select by ID)
@funcionarios_bp.route('/<matricula>')
def get_funcionarios(matricula):
    sql = text("SELECT * FROM funcionarios WHERE matricula = :matricula")
    dados = {"matricula": matricula}
    
    try:
        result = db.session.execute(sql, dados)
        # Mapear todas as colunas para a linha
        linhas = result.mappings().all()
        
        if len(linhas) > 0:
            return dict(linhas[0])
        else:
            return "Funcionário não encontrado"
            
    except Exception as e:
        return str(e)

# Ler todos (Select All)
@funcionarios_bp.route('/all')
def get_all_funcionarios():
    sql_query = text("SELECT * FROM funcionarios")
    
    try:
        result = db.session.execute(sql_query)
        
        relatorio = result.mappings().all()
        json_output = [dict(row) for row in relatorio] # Converte linhas em lista de dicionários

        return json_output
    except Exception as e:
        return []

# Atualizar (Update)
@funcionarios_bp.route("/<matricula>", methods=["PUT"])
def atualizar_funcionarios(matricula):
    # dados que vieram
    nome = request.form.get("nome_funcionario")
    email = request.form.get("email")
    matricula_nova = request.form.get("matricula", matricula)
    apelido = request.form.get("apelido")
    senha = request.form.get("senha")

    sql = text("""UPDATE funcionarios SET 
                        nome_completo = :nome_funcionario, email = :email, apelido = :apelido,
                        senha = :senha,
                        matricula = :matricula_nova 
                    WHERE matricula = :matricula""")
    
    dados = {   "nome_funcionario": nome, 
                "matricula_nova": matricula_nova, 
                "email": email, "apelido": apelido,
                "senha": senha,
                "matricula": matricula }

    try:
        result = db.session.execute(sql, dados)
        linhas_afetadas = result.rowcount 
        
        if linhas_afetadas == 1: 
            db.session.commit()
            return f"Funcionário {matricula} atualizado com sucesso"
        else:
            db.session.rollback()
            return f"Funcionário não encontrado ou erro ao atualizar"
    except Exception as e:
        return str(e)

# Deletar (Delete)
@funcionarios_bp.route("/<matricula>", methods=['DELETE'])
def delete_funcionarios(matricula):
    sql = text("DELETE FROM funcionarios WHERE matricula = :matricula")
    dados = {"matricula": matricula}
    
    try:
        result = db.session.execute(sql, dados)
        linhas_afetadas = result.rowcount 
        
        if linhas_afetadas == 1: 
            db.session.commit()
            return f"Funcionário {matricula} removido"
        else:
            db.session.rollback()
            return f"Erro: Funcionário não encontrado para deletar"
    except Exception as e:
        return str(e)

