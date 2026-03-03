#somente para testes
import random
from datetime import datetime, timedelta
from sqlalchemy import text
from app import app
from conf.database import db

def get_funcionarios():
    sql = text("SELECT matricula, nome_completo, apelido, horario_inicio, horario_fim, posto_especial FROM funcionarios")
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

def gerar_escala(central_mat_manha, central_mat_tarde, data_escala):
    print(f"\n--- Gerando Escala para {data_escala} ---")
    print(f"Funcionários na Central: Manhã={central_mat_manha}, Tarde={central_mat_tarde}")

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
        # Misturar os disponíveis para garantir aleatoriedade inicial
        random.shuffle(disponiveis)
        
        alocados_neste_horario = set()
        escala_horario_atual = [] # Lista temporária para ordenar os postos deste horário
        
        # Ponto de virada definido como 13:30 (exemplo)
        ponto_virada = datetime.strptime("13:30", "%H:%M").time()
        
        #Help function for scoring
        def score_candidato(func, posto_alvo_id):
            # Garantir comparação de strings para evitar falhas de tipos (int vs str)
            ultimo = str(ultimo_posto_funcionario.get(str(func['matricula']), ""))
            if ultimo == str(posto_alvo_id):
                return 1000 
            return 0

        # Identificar IDs de todos os postos para facilitar a busca
        id_ronda_p1 = next((p['id'] for p in postos if 'Ronda P1' in p['nome']), None)
        id_delta4 = next((p['id'] for p in postos if 'Delta 4' in p['nome']), None)
        id_ronda_p2_p3 = next((p['id'] for p in postos if 'Ronda P2 e P3' in p['nome']), None)

        def alocar_posto(posto_id, nome_exibicao):
            candidatos = [f for f in disponiveis if f['matricula'] not in alocados_neste_horario]
            random.shuffle(candidatos)
            candidatos_ordenados = sorted(candidatos, key=lambda f: score_candidato(f, posto_id))
            
            if candidatos_ordenados:
                escolhido = candidatos_ordenados[0]
                res = {
                    'horario': time_str,
                    'data': data_escala,
                    'matricula': escolhido['matricula'],
                    'posto_id': posto_id,
                    'apelido': escolhido['apelido'],
                    'posto_nome': nome_exibicao
                }
                alocados_neste_horario.add(escolhido['matricula'])
                ultimo_posto_funcionario[str(escolhido['matricula'])] = str(posto_id)
                return res
            return None

        # --- 1. Alocar na ordem solicitada ---
        
        # Alfa 2
        p_alfa2 = alocar_posto(id_alfa2, 'Alfa 2')
        if p_alfa2: escala_horario_atual.append(p_alfa2)
        
        # Ronda P1
        p_ronda1 = alocar_posto(id_ronda_p1, 'Ronda P1')
        if p_ronda1: escala_horario_atual.append(p_ronda1)
        
        # Delta 4
        p_delta4 = alocar_posto(id_delta4, 'Delta 4')
        if p_delta4: escala_horario_atual.append(p_delta4)

        # Alfa 3
        p_alfa3 = alocar_posto(id_alfa3, 'Alfa 3')
        if p_alfa3: escala_horario_atual.append(p_alfa3)

        # Ronda P2 e P3
        p_ronda23 = alocar_posto(id_ronda_p2_p3, 'Ronda P2 e P3')
        if p_ronda23: escala_horario_atual.append(p_ronda23)

        # Central (Seleção Manual)
        central_da_vez = central_mat_manha if current_time < ponto_virada else central_mat_tarde
        func_central = next((f for f in disponiveis if str(f['matricula']) == str(central_da_vez)), None)
        
        if func_central and func_central['matricula'] not in alocados_neste_horario:
            p_central = {
                'horario': time_str,
                'data': data_escala,
                'matricula': func_central['matricula'],
                'posto_id': id_central,
                'apelido': func_central['apelido'],
                'posto_nome': 'Central'
            }
            escala_horario_atual.append(p_central)
            alocados_neste_horario.add(func_central['matricula'])
            ultimo_posto_funcionario[str(func_central['matricula'])] = str(id_central)

        # Adicionar os registros deste horário na ordem correta
        escala_gerada.extend(escala_horario_atual)

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
        
        central_mat_manha = input("\nDigite a matrícula do funcionário da CENTRAL (MANHÃ): ")
        central_mat_tarde = input("Digite a matrícula do funcionário da CENTRAL (TARDE): ")
        
        data_hj = datetime.now().strftime("%Y-%m-%d")
        data_input = input(f"Digite a data da escala (YYYY-MM-DD) [Enter para {data_hj}]: ")
        if not data_input:
            data_input = data_hj
            
        resultado = gerar_escala(central_mat_manha, central_mat_tarde, data_input)
        
        print(f"\n{'HORARIO':<10} | {'POSTO':<20} | {'FUNCIONARIO':<20}")
        print("-" * 60)
        for row in resultado:
            print(f"{row['horario']:<10} | {row['posto_nome']:<20} | {row['apelido']:<20}")
            
        salvar = input("\nDeseja salvar essa escala no banco de dados? (s/n): ")
        if salvar.lower() == 's':
            salvar_escala_bd(resultado)
