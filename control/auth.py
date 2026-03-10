"""
auth.py — Utilitários de autenticação compartilhados entre os controllers.
Evita importação circular entre funcionarios.py e postos.py.
"""
from flask import request
from sqlalchemy import text
from conf.database import db


def verificar_admin(matricula):
    """Retorna True se o funcionário com a matrícula informada for admin."""
    if not matricula:
        return False
    try:
        result = db.session.execute(
            text("SELECT is_admin FROM funcionarios WHERE matricula = :m"),
            {"m": matricula}
        )
        row = result.fetchone()
        return bool(row and row[0])
    except Exception:
        return False


def exigir_admin():
    """
    Lê o header X-Matricula e retorna 403 se o usuário não for admin.
    Retorna None se a verificação passar.
    """
    matricula = request.headers.get("X-Matricula")
    if not verificar_admin(matricula):
        return {"erro": "Acesso negado. Apenas administradores podem realizar esta ação."}, 403
    return None
