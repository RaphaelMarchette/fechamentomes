import json
import os
from database.classes import Geometria, Grupo, Ferramenta, Operacao

def carregar_dados(base_dir):
	with open(os.path.join(base_dir, 'dados.json')) as json_arq:
		dados = json.load(json_arq)
		carregar_groups(dados['groups'])
		carregar_geos(dados['geos'])
		carregar_tools(dados['tools'])
		carregar_opers(dados['opers'])

def carregar_groups(groups):
	for group in groups:
		Grupo.criar(	group['group_name'],
						group['group_time'])

	print(f'Carregados {len(groups)} grupos com sucesso!')

def carregar_geos(geos):
	for geo in geos:
		Geometria.criar(	geo['geo_name'],
							geo['geo_x'],
							geo['geo_y'],
							geo['geo_z'])

	print(f'Carregados {len(geos)} geometria com sucesso!')

def carregar_tools(tools):
	for tool in tools:
		Ferramenta.criar(	tool['tool_tipy'],
				tool['tool_name'],
				tool['tool_diamiter'],
				tool['tool_height'],
				tool['tool_angle'],
				tool['tool_n_inserts'],
				tool['tool_number'])

	print(f'Carregados {len(tools)} ferramenta com sucesso!')

def carregar_opers(opers):
	for oper in opers:
		Operacao.criar(	oper['oper_tipy'],
                   		oper['oper_name'],
						oper['oper_limits_coord'],
						oper['oper_mod_select'],
						oper['oper_side_tool'],
                   		oper['oper_dmt_maior'],
                   		oper['oper_dmt_menor'],
						oper['oper_z_init'],
                   		oper['oper_z_finish'],
						oper['oper_pas_add'],
                   		oper['oper_side_incr'],
						oper['oper_side_estoq'],
						oper['oper_z_incr'],
						oper['oper_thread_pitch'],
						oper['oper_engate'],
						oper['oper_retrair'],
                   		oper['oper_z_sob'],
						oper['oper_z_transf'],
                   		oper['oper_speed_spindle'],
                   		oper['oper_speed_cutting'])

	print(f'Carregados {len(opers)} operacao com sucesso!')