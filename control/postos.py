from flask import Flask, Blueprint, request
from sqlalchemy import text

from conf.database import db

postos_bp = Blueprint('postos', __name__, url_prefix = '/postos') 


# -------------------- CRUD postos --------------------
# Criar retornando ID (Insert com Returning)
@postos_bp.route("/", methods=["POST"])
def criar_postos():
    # dados que vieram
    horario_front = request.form.get("Horário")
    alfa2 = request.form.get("Alfa 2")
    rondap1 = request.form.get("Ronda P1")
    delta4 = request.form.get("Delta 4")
    alfa3 = request.form.get("Alfa 3")
    rondap2p3 = request.form.get("Ronda P2 e P3")
    galeriaqap = request.form.get("Galeria/QAP")
    central = request.form.get("Central")
    # SQL
    sql = text("""
                INSERT INTO postos 
                    (horario, alfa2, rondap1, delta4, alfa3, rondap2p3, galeriaqap, central) 
                VALUES 
                    (:horario_temp, :alfa2, :rondap1, :delta4, :alfa3, :rondap2p3, :galeriaqap, :central)                
                RETURNING id
                """)
    dados = {"horario_temp": horario_front,
             "alfa2": alfa2, 
             "rondap1": rondap1, 
             "delta4": delta4, 
             "alfa3": alfa3, 
             "rondap2p3": rondap2p3, 
             "galeriaqap": galeriaqap, 
             "central": central}

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

