from flask import Flask, Blueprint, request, jsonify
from sqlalchemy import text
from datetime import datetime

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
    posto_especial = request.form.get("posto_especial", "False").lower() == "true"

    # 2. Organiza em um dicionário para validação inicial
    dados = {
        "nome_temp": nome_front, 
        "email": email, 
        "matricula": matricula, 
        "apelido": apelido, 
        "senha": senha, 
        "horario_inicio": horario_inicio, 
        "horario_fim": horario_fim, 
    }

    # --- VALIDAÇÃO DE CAMPOS VAZIOS ---
    for campo, valor in dados.items():
        if not valor or str(valor).strip() == "":
            return f"Erro: O campo '{campo}' é obrigatório.", 400 

    # --- NOVA VALIDAÇÃO: FORMATO DE HORA (HH:MM) ---
    for campo_hora in ["horario_inicio", "horario_fim"]:
        try:
            # Tenta converter a string para um objeto de hora
            datetime.strptime(dados[campo_hora], "%H:%M")
        except ValueError:
            return f"Erro: O campo '{campo_hora}' deve estar no formato HH:MM (ex: 09:00).", 400

    # --- VALIDAÇÕES DE REGRA DE NEGÓCIO ---
    
    # Validação de lógica de horário (agora que o formato está garantido)
    if horario_inicio >= horario_fim:
        return "Erro: O horário de início deve ser menor que o horário de fim.", 400
    
    if "@" not in email:
        return "Erro: O email deve conter @.", 400
    
    if len(senha) < 6:
        return "Erro: A senha deve ter pelo menos 6 caracteres.", 400
    
    if len(matricula) < 4:
        return "Erro: A matricula deve ter pelo menos 4 caracteres.", 400
    
    if len(apelido) < 3:
        return "Erro: O apelido deve ter pelo menos 3 caracteres.", 400
    
    if len(nome_front) < 3:
        return "Erro: O nome deve ter pelo menos 3 caracteres.", 400

    # Adiciona o campo que não passou pelo loop de strings obrigatórias
    dados["posto_especial"] = posto_especial

    # 3. Insere no banco
    sql = text("""
                INSERT INTO funcionarios 
                    (nome_completo, email, matricula, apelido, senha, horario_inicio, horario_fim, posto_especial) 
                VALUES 
                    (:nome_temp, :email, :matricula, :apelido, :senha, :horario_inicio, :horario_fim, :posto_especial)                
                """)

    try:
        db.session.execute(sql, dados)
        db.session.commit()
        return dados, 201 

    except Exception as e:
        db.session.rollback()
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
    # 1. Coleta dos dados
    dados_requisicao = {
        "nome_funcionario": request.form.get("nome_funcionario"),
        "email": request.form.get("email"),
        "matricula_nova": request.form.get("matricula"),
        "apelido": request.form.get("apelido"),
        "senha": request.form.get("senha"),
        "horario_inicio": request.form.get("horario_inicio"),
        "horario_fim": request.form.get("horario_fim"),
        "posto_especial": request.form.get("posto_especial")
    }

    # 2. Restrição: Validar campos obrigatórios (vazios ou None)
    campos_vazios = [campo for campo, valor in dados_requisicao.items() if not valor or str(valor).strip() == ""]
    if campos_vazios:
        return f"Erro: Preencha todos os campos: {', '.join(campos_vazios)}", 400

    # 3. Restrição: Validar formato de hora (HH:MM)
    for campo in ["horario_inicio", "horario_fim"]:
        valor_hora = dados_requisicao[campo]
        try:
            # Tenta converter a string para o formato de hora
            datetime.strptime(valor_hora, "%H:%M")
        except ValueError:
            return f"Erro: O campo {campo} deve estar no formato HH:MM (ex: 08:00, 17:30)", 400

    # --- Início da execução SQL ---
    sql = text("""UPDATE funcionarios SET 
                        nome_completo = :nome_funcionario, email = :email, apelido = :apelido,
                        senha = :senha, matricula = :matricula_nova,
                        horario_inicio = :horario_inicio, horario_fim = :horario_fim,
                        posto_especial = :posto_especial 
                    WHERE matricula = :matricula""")
    
    dados_requisicao["matricula"] = matricula

    try:
        result = db.session.execute(sql, dados_requisicao)
        if result.rowcount == 1: 
            db.session.commit()
            return f"Funcionário {matricula} atualizado com sucesso", 200
        else:
            db.session.rollback()
            return "Funcionário não encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Erro no banco de dados: {str(e)}", 500
# Atualizar (Update)
# @funcionarios_bp.route("/<matricula>", methods=["PUT"])
# def atualizar_funcionarios(matricula):
#     # dados que vieram
#     nome = request.form.get("nome_funcionario")
#     email = request.form.get("email")
#     matricula_nova = request.form.get("matricula", matricula)
#     apelido = request.form.get("apelido")
#     senha = request.form.get("senha")
#     horario_inicio = request.form.get("horario_inicio")
#     horario_fim = request.form.get("horario_fim")
#     posto_especial = request.form.get("posto_especial")

#     #---------------------------------------------------------------------------------------------
#     sql = text("""UPDATE funcionarios SET 
#                         nome_completo = :nome_funcionario, email = :email, apelido = :apelido,
#                         senha = :senha,
#                         matricula = :matricula_nova,
#                         horario_inicio = :horario_inicio,
#                         horario_fim = :horario_fim,
#                         posto_especial = :posto_especial 
#                     WHERE matricula = :matricula""")
    
#     dados = {   "nome_funcionario": nome, 
#                 "matricula_nova": matricula_nova, 
#                 "email": email, "apelido": apelido,
#                 "senha": senha,
#                 "matricula": matricula,
#                 "horario_inicio": horario_inicio,
#                 "horario_fim": horario_fim,
#                 "posto_especial": posto_especial   }

#     try:
#         result = db.session.execute(sql, dados)
#         linhas_afetadas = result.rowcount 
        
#         if linhas_afetadas == 1: 
#             db.session.commit()
#             return f"Funcionário {matricula} atualizado com sucesso"
#         else:
#             db.session.rollback()
#             return f"Funcionário não encontrado ou erro ao atualizar"
#     except Exception as e:
#         return str(e)

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

