from flask import Flask, Blueprint, request
from sqlalchemy import text

from conf.database import db

login_bp = Blueprint('login', __name__, url_prefix = '/login') 

@app.route("/", methods=["POST"])
def criar_login():
    nome = request.form.get("nome", " Você deveria enviar um nome")
    return  f"Seu nome é  {nome.upper()}  e em minusculo {nome.lower()}"

@app.route("/", <senha>')
def paginaVariavel(senha):
    if senha == '1234':
        return "Isso não deveria ser uma senha"
    return senha


