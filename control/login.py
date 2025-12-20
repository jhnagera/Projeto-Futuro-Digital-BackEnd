from flask import Flask, Blueprint, request
from sqlalchemy import text

from conf.database import db

login_bp = Blueprint('login', __name__, url_prefix = '/login') 

# @app.route("/", methods=["POST"])
# def criar_login():
#     nome = request.form.get("nome", " Você deveria enviar um nome")
#     return  f"Seu nome é  {nome.upper()}  e em minusculo {nome.lower()}"

# @app.route("/", <senha>')
# def paginaVariavel(senha):
#     if senha == '1234':
#         return "Isso não deveria ser uma senha"
#     return senha


#feito por IA, não testei ainda!!!!!
# -------------------- LOGIN --------------------
@login_bp.route("/", methods=["POST"])
def login_funcionario():
    # Dados recebidos do frontend
    matricula = request.form.get("matricula")
    senha = request.form.get("senha")
    
    # Validação dos campos obrigatórios
    if not matricula or not senha:
        return {"sucesso": False, "mensagem": "Matrícula e senha são obrigatórios"}, 400
    
    # SQL para buscar funcionário pela matrícula
    sql = text("SELECT * FROM funcionarios WHERE matricula = :matricula")
    dados = {"matricula": matricula}
    
    try:
        result = db.session.execute(sql, dados)
        linhas = result.mappings().all()
        
        # Verifica se o funcionário existe
        if len(linhas) == 0:
            return {"sucesso": False, "mensagem": "Funcionário não encontrado"}, 404
        
        funcionario = dict(linhas[0])
        
        # Verifica se a senha está correta
        if funcionario.get("senha") != senha:
            return {"sucesso": False, "mensagem": "Senha incorreta"}, 401
        
        # Remove a senha do retorno por segurança
        funcionario.pop("senha", None)
        
        return {
            "sucesso": True, 
            "mensagem": "Login realizado com sucesso",
            "funcionario": funcionario
        }, 200
        
    except Exception as e:
        return {"sucesso": False, "mensagem": f"Erro ao realizar login: {str(e)}"}, 500
