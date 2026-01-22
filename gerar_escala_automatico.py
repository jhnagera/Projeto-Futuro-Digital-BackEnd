#somente para testes
import random
from datetime import datetime, timedelta
from sqlalchemy import text
from app import app
from conf.database import db

def get_funcionarios():
    sql = text("SELECT matricula, nome_completo, apelido, horario_inicio, horario_fim FROM funcionarios")
    result = db.session.execute(sql)
    return [dict(row) for row in result.mappings().all()]

def get_postos():
    sql = text("SELECT id, nome FROM postos")
    result = db.session.execute(sql)
    return [dict(row) for row in result.mappings().all()]

def parse_time(time_str):
    if not time_str:
        return None
    try:
        return datetime.strptime(time_str, "%H:%M").time()
    except ValueError:
        try:
            return datetime.strptime(time_str, "%H:%M:%S").time()
        except ValueError:
            return None

def is_available(funcionario, current_time):
    start = parse_time(funcionario['horario_inicio'])
    end = parse_time(funcionario['horario_fim'])
    
    if not start or not end:
        return False
        
    return start <= current_time < end

def gerar_escala(central_matricula, data_escala):
    print(f"\n--- Gerando Escala para {data_escala} ---")
    print(f"Funcionário Fixo na Central: {central_matricula}")

    funcionarios = get_funcionarios()
    postos = get_postos()

    # Identificar IDs dos postos críticos
    id_central = next((p['id'] for p in postos if 'Central' in p['nome']), None)
    id_alfa2 = next((p['id'] for p in postos if 'Alfa 2' in p['nome'] and 'iuhgikyg' not in p['nome']), None)
    id_alfa3 = next((p['id'] for p in postos if 'Alfa 3' in p['nome']), None)
    
    if not id_central: id_central = 13
    if not id_alfa2: id_alfa2 = 5
    if not id_alfa3: id_alfa3 = 8

    print(f"IDs identificados: Central={id_central}, Alfa2={id_alfa2}, Alfa3={id_alfa3}")

    outros_postos_ids = [p['id'] for p in postos if p['id'] not in [id_central, id_alfa2, id_alfa3]]

    start_time = datetime.strptime("08:00", "%H:%M")
    end_time = datetime.strptime("19:30", "%H:%M")
    current_dt = start_time

    escala_gerada = []
    
    # Dict: matricula -> ultimo_posto_id
    ultimo_posto_funcionario = {}

    while current_dt <= end_time:
        current_time = current_dt.time()
        time_str = current_dt.strftime("%H:%M")
        
        disponiveis = [f for f in funcionarios if is_available(f, current_time)]
        random.shuffle(disponiveis)
        
        alocados_neste_horario = set()
        
        # --- 1. Alocar CENTRAL (Fixo) ---
        func_central = next((f for f in disponiveis if str(f['matricula']) == str(central_matricula)), None)
        
        if func_central:
            escala_gerada.append({
                'horario': time_str,
                'data': data_escala,
                'matricula': func_central['matricula'],
                'posto_id': id_central,
                'apelido': func_central['apelido'],
                'posto_nome': 'Central'
            })
            alocados_neste_horario.add(func_central['matricula'])
            ultimo_posto_funcionario[func_central['matricula']] = id_central

        #Help function for scoring
        def score_candidato(func, posto_alvo_id):
            ultimo = ultimo_posto_funcionario.get(func['matricula'])
            if ultimo == posto_alvo_id:
                return 1000 
            return 0

        candidatos_alfas = [f for f in disponiveis if f['matricula'] not in alocados_neste_horario]
        
        # ALFA 2
        candidatos_ordenados = sorted(candidatos_alfas, key=lambda f: score_candidato(f, id_alfa2))
        if candidatos_ordenados:
            escolhido = candidatos_ordenados[0]
            escala_gerada.append({
                'horario': time_str,
                'data': data_escala,
                'matricula': escolhido['matricula'],
                'posto_id': id_alfa2,
                'apelido': escolhido['apelido'],
                'posto_nome': 'Alfa 2'
            })
            alocados_neste_horario.add(escolhido['matricula'])
            ultimo_posto_funcionario[escolhido['matricula']] = id_alfa2
            candidatos_alfas.remove(escolhido)

        # ALFA 3
        candidatos_ordenados = sorted(candidatos_alfas, key=lambda f: score_candidato(f, id_alfa3))
        if candidatos_ordenados:
            escolhido = candidatos_ordenados[0]
            escala_gerada.append({
                'horario': time_str,
                'data': data_escala,
                'matricula': escolhido['matricula'],
                'posto_id': id_alfa3,
                'apelido': escolhido['apelido'],
                'posto_nome': 'Alfa 3'
            })
            alocados_neste_horario.add(escolhido['matricula'])
            ultimo_posto_funcionario[escolhido['matricula']] = id_alfa3
        
        # --- 3. Alocar DEMAIS POSTOS ---
        sobras = [f for f in disponiveis if f['matricula'] not in alocados_neste_horario]
        posts_disponiveis = [pid for pid in outros_postos_ids] 
        random.shuffle(posts_disponiveis)
        
        for pid in posts_disponiveis:
            if not sobras:
                break
            
            sobras_sorted = sorted(sobras, key=lambda f: score_candidato(f, pid))
            escolhido = sobras_sorted[0]
            
            nome_posto = next((p['nome'] for p in postos if p['id'] == pid), "Desconhecido")

            escala_gerada.append({
                'horario': time_str,
                'data': data_escala,
                'matricula': escolhido['matricula'],
                'posto_id': pid,
                'apelido': escolhido['apelido'],
                'posto_nome': nome_posto
            })
            alocados_neste_horario.add(escolhido['matricula'])
            ultimo_posto_funcionario[escolhido['matricula']] = pid
            sobras.remove(escolhido)

        current_dt += timedelta(minutes=30)
    
    return escala_gerada

def salvar_escala_bd(escala_list):
    try:
        query = text("""
            INSERT INTO escala (horario, data, matricula, posto)
            VALUES (:horario, :data, :matricula, :posto)
        """)
        for item in escala_list:
            db.session.execute(query, {
                'horario': item['horario'],
                'data': item['data'],
                'matricula': str(item['apelido']), 
                'posto': str(item['posto_nome']) 
            })
        db.session.commit()
        print("Escala salva no banco de dados com sucesso!")
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao salvar no banco: {e}")

if __name__ == "__main__":
    with app.app_context():
        print("--- Gerador de Escala Automático ---")
        
        print("\nFuncionários disponíveis:")
        try:
            funcs = get_funcionarios()
            for f in funcs:
                print(f" - {f['nome_completo']} (Matrícula: {f['matricula']})")
        except Exception as e:
            print(f"Erro ao ler funcionarios: {e}")
            funcs = []
        
        central_mat = input("\nDigite a matrícula do funcionário fixo da CENTRAL: ")
        
        data_hj = datetime.now().strftime("%Y-%m-%d")
        data_input = input(f"Digite a data da escala (YYYY-MM-DD) [Enter para {data_hj}]: ")
        if not data_input:
            data_input = data_hj
            
        resultado = gerar_escala(central_mat, data_input)
        
        print(f"\n{'HORARIO':<10} | {'POSTO':<20} | {'FUNCIONARIO':<20}")
        print("-" * 60)
        for row in resultado:
            print(f"{row['horario']:<10} | {row['posto_nome']:<20} | {row['apelido']:<20}")
            
        salvar = input("\nDeseja salvar essa escala no banco de dados? (s/n): ")
        if salvar.lower() == 's':
            salvar_escala_bd(resultado)
