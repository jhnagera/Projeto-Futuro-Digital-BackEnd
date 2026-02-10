from flask import Flask, Blueprint, request, jsonify
from sqlalchemy import text

from conf.database import db

funcionarios_bp = Blueprint('funcionarios', __name__, url_prefix = '/funcionarios') 


@funcionarios_bp.route("/", methods=["POST"])
def criar_funcionarios():
    # 1. Coleta os dados
    nome_front = request.form.get("nome_funcionario")
    email = request.form.get("email")
    matricula = request.form.get("matricula")
    apelido = request.form.get("apelido")
    senha = request.form.get("senha")
    horario_inicio = request.form.get("horario_inicio")
    horario_fim = request.form.get("horario_fim")
    posto_especial = request.form.get("posto_especial", False)

    # 2. Organiza em um dicionário
    dados = {
        "nome_temp": nome_front, 
        "email": email, 
        "matricula": matricula, 
        "apelido": apelido, 
        "senha": senha, 
        "horario_inicio": horario_inicio, 
        "horario_fim": horario_fim, 
            }

    # --- NOVA RESTRIÇÃO: VALIDAÇÃO DE CAMPOS VAZIOS ---
    for campo, valor in dados.items():
        # Verifica se o valor é None ou apenas espaços em branco
        if not valor or str(valor).strip() == "":
            return f"Erro: O campo '{campo}' é obrigatório.", 400 
    # --------------------------------------------------
    #dados não obrigatórios
    dados["posto_especial"] = posto_especial
    #validação de horario
    if horario_inicio >= horario_fim:
        return "Erro: O horário de início deve ser menor que o horário de fim.", 400
    #validação de email
    if "@" not in email:
        return "Erro: O email deve conter @.", 400
    #validação de senha
    if len(senha) < 6:
        return "Erro: A senha deve ter pelo menos 6 caracteres.", 400
    #validação de matricula
    if len(matricula) < 4:
        return "Erro: A matricula deve ter pelo menos 4 caracteres.", 400
    #validação de apelido
    if len(apelido) < 3:
        return "Erro: O apelido deve ter pelo menos 3 caracteres.", 400
    #validação de nome
    if len(nome_front) < 3:
        return "Erro: O nome deve ter pelo menos 3 caracteres.", 400
    #validação de posto especial
    if posto_especial not in [True, False]:
        return "Erro: O posto especial deve ser True ou False.", 400

    # 3. Insere no banco
    # SQL
    sql = text("""
                INSERT INTO funcionarios 
                    (nome_completo, email, matricula, apelido, senha, horario_inicio, horario_fim, posto_especial) 
                VALUES 
                    (:nome_temp, :email, :matricula, :apelido, :senha, :horario_inicio, :horario_fim, :posto_especial)                
                """)

    try:
        db.session.execute(sql, dados)
        db.session.commit()
        
        return dados, 201 # Retorna 201 que significa "Criado com sucesso"

    except Exception as e:
        db.session.rollback() # Desfaz qualquer alteração se der erro
        return f"Erro ao inserir no banco: {e}", 500
# # -------------------- CRUD funcionarios --------------------
# # Criar retornando ID (Insert com Returning)
# @funcionarios_bp.route("/", methods=["POST"])
# def criar_funcionarios():
#     # dados que vieram
#     nome_front = request.form.get("nome_funcionario")
#     email = request.form.get("email")
#     matricula = request.form.get("matricula")
#     apelido = request.form.get("apelido")
#     senha = request.form.get("senha")
#     horario_inicio = request.form.get("horario_inicio")
#     horario_fim = request.form.get("horario_fim")
#     posto_especial = request.form.get("posto_especial")
#     # SQL
#     sql = text("""
#                 INSERT INTO funcionarios 
#                     (nome_completo, email, matricula, apelido, senha, horario_inicio, horario_fim, posto_especial) 
#                 VALUES 
#                     (:nome_temp, :email, :matricula, :apelido, :senha, :horario_inicio, :horario_fim, :posto_especial)                
#                 """)
#     dados = {"nome_temp": nome_front, "email": email, "matricula": matricula, "apelido": apelido, "senha": senha, "horario_inicio": horario_inicio, "horario_fim": horario_fim, "posto_especial": posto_especial}

#     try:
#         # executar consulta
#         result = db.session.execute(sql, dados)
#         db.session.commit()

#         # pega o id
#         #id_gerado = result.fetchone()[0]
#         #dados['id'] = id_gerado
        
#         return dados
#     except Exception as e:
#         return f"Erro: {e}"

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
    horario_inicio = request.form.get("horario_inicio")
    horario_fim = request.form.get("horario_fim")
    posto_especial = request.form.get("posto_especial")
    sql = text("""UPDATE funcionarios SET 
                        nome_completo = :nome_funcionario, email = :email, apelido = :apelido,
                        senha = :senha,
                        matricula = :matricula_nova,
                        horario_inicio = :horario_inicio,
                        horario_fim = :horario_fim,
                        posto_especial = :posto_especial 
                    WHERE matricula = :matricula""")
    
    dados = {   "nome_funcionario": nome, 
                "matricula_nova": matricula_nova, 
                "email": email, "apelido": apelido,
                "senha": senha,
                "matricula": matricula,
                "horario_inicio": horario_inicio,
                "horario_fim": horario_fim,
                "posto_especial": posto_especial   }

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

