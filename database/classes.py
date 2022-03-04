
class Geometria:

	__dados = []

	def __init__(	self,
					geo_name,
					geo_x,
					geo_y,
					geo_z):

		self.__geo_name	=	geo_name
		self.__geo_x	=	geo_x
		self.__geo_y	=	geo_y
		self.__geo_z	=	geo_z

	@classmethod
	def criar(  cls,
				geo_name,
				geo_x,
				geo_y,
				geo_z):

		geo =  cls(	geo_name,
					geo_x,
					geo_y,
					geo_z)

		erros = Geometria.__validar(geo)
		if len(erros) == 0:
			Geometria.__dados.append(geo)
		return erros

	@classmethod
	def __validar(cls, geo, alteracao=False):
		erros = []
		return erros


class Grupo:
	
	__dados = []

	def __init__(self, group_name, group_time):
		self.group_name = group_name
		self.group_time = group_time
		
	def __str__(self):
		return f'{self.group_name} - {self.group_time}'

	@classmethod
	def alterar(cls, group_name, group_time):
		grupo = cls( group_name, group_time)
		erros = Grupo.__validar(grupo, True)

		if len(erros) == 0:
			original = Grupo.obter(grupo.group_name)
			original.group_name = grupo.group_name
			original.group_time = grupo.group_time

		return erros

	@classmethod
	def criar(cls, group_name, group_time):
		grupo = cls( group_name, group_time,)
		erros = Grupo.__validar(grupo)

		if len(erros) == 0:
			Grupo.__dados.append(grupo)

		return erros

	@classmethod
	def remover(cls, group_name):
		grupo = Grupo.obter(group_name)
		if grupo:
			Grupo.__dados.remove(grupo)

	@classmethod
	def obter(cls, group_name):
		for c in Grupo.__dados:
			if c.group_name.lower() == group_name.lower():
				return c

	@classmethod
	def listar(cls):
		return Grupo.__dados

	@classmethod
	def __validar(cls, grupo, alteracao=False):
		erros = []

		if not grupo.group_name:
			erros.append('group_name do grupo é obrigatória!')
		elif not alteracao and Grupo.obter(grupo.group_name):
			erros.append(f'A group_name {grupo.group_name} já está sendo utilizada!')

		if not grupo.group_time:
			erros.append('group_time do grupo é obrigatório!')

		return erros


class Ferramenta:

	__dados = []

	def __init__(	self,
			tool_tipy,
			tool_name,
            tool_diamiter,
            tool_height,
			tool_angle,
            tool_n_inserts,
            tool_number):

		self.__tool_tipy		=	tool_tipy
		self.__tool_name		=	tool_name
		self.__tool_diamiter	=	tool_diamiter
		self.__tool_height		=	tool_height
		self.__tool_angle		=	tool_angle
		self.__tool_n_inserts	=	tool_n_inserts
		self.__tool_number		=	tool_number

	@property
	def tool_raio(self):
		self.__tool_raio = self.__tool_diamiter / 2
		return self.__tool_raio
	
	@classmethod
	def criar(  cls,
				tool_tipy,
				tool_name,
                tool_diamiter,
                tool_height,
				tool_angle,
                tool_n_inserts,
                tool_number):

		tool =  cls(	tool_tipy,
                		tool_name, 
                		tool_diamiter, 
                		tool_height, 
                		tool_angle,
                		tool_n_inserts, 
                		tool_number)

		erros = Ferramenta.__validar(tool)
		if len(erros) == 0:
			Ferramenta.__dados.append(tool)
		return erros

	@classmethod
	def __validar(cls, tool, alteracao=False):
		erros = []
		return erros

import datetime

class Operacao():

	__dados = []
                  
	def __init__(	self,
                  	oper_tipy,
                   	oper_name,
					oper_limits_coord,
					oper_mod_select,
					oper_side_tool,
                   	oper_dmt_maior,
                   	oper_dmt_menor,
					oper_z_init,
                   	oper_z_finish,
					oper_pas_add,
                   	oper_side_incr,
					oper_side_estoq,
					oper_z_incr,
					oper_thread_pitch,
					oper_engate,
					oper_retrair,
                   	oper_z_sob,
					oper_z_transf,
                   	oper_speed_spindle,
                   	oper_speed_cutting):

		self.__oper_tipy		=	oper_tipy
		self.__oper_name		=	oper_name
		self.__oper_limits_coord=	oper_limits_coord
		self.__oper_mod_select	=	oper_mod_select
		self.__oper_side_tool	=	oper_side_tool
		self.__oper_dmt_maior	=	self.__oper_limits_coord[3] * 2
		self.__oper_dmt_menor	=	oper_dmt_menor
		self.__oper_z_init		=	oper_z_init
		self.__oper_z_finish	=	oper_z_finish
		self.__oper_pas_add		=	oper_pas_add
		self.__oper_side_incr	=	oper_side_incr
		self.__oper_side_estoq	=	oper_side_estoq
		self.__oper_z_incr		=	oper_z_incr
		self.__oper_thread_pitch=	oper_thread_pitch
		self.__oper_engate		=	oper_engate
		self.__oper_retrair		=	oper_retrair
		self.__oper_z_sob		=	oper_z_sob
		self.__oper_z_transf	=	oper_z_transf
		self.__oper_speed_spindle=	oper_speed_spindle
		self.__oper_speed_cutting=	oper_speed_cutting
		self.__lista			=	[]
		self.__data_hora		=	datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S ')

	@property
	def oper_rpm(self):
		self.__oper_rpm = self.__oper_speed_spindle * 318 / super().tool_diamiter
		return self.__oper_rpm
           
	@property
	def oper_feed(self):
		self.__oper_feed = self.__oper_rpm * self.__oper_speed_cutting * super().tool_n_inserts
		return self.__oper_feed

	@property
	def oper_x_pnt_cnt(self):
		self.__oper_x_pnt_cnt = self.__oper_limits_coord[0]
		return self.__oper_x_pnt_cnt

	@property
	def oper_y_pnt_cnt(self):
		self.__oper_y_pnt_cnt = self.__oper_limits_coord[1]
		return self.__oper_y_pnt_cnt

	@property
	def oper_raio_dmt_maior(self):
		self.__oper_raio_dmt_maior = self.__oper_dmt_maior / 2
		return self.__oper_raio_dmt_maior

	@property
	def oper_raio_dmt_menor(self):
		self.__oper_raio_dmt_menor = self.__oper_dmt_menor / 2
		return self.__oper_raio_dmt_menor

	@property
	def oper_raio_diferenca(self):
		self.__oper_raio_diferenca = self.__oper_raio_dmt_maior - self.__oper_raio_dmt_menor
		return self.__oper_raio_diferenca

	@property
	def oper_x_retract(self):
		self.__oper_x_retract = self.__oper_x_pnt_cnt
		return self.__oper_x_retract

	@property
	def oper_x_engate(self):
		self.__oper_x_engate = self.__oper_raio_dmt_menor + self.__oper_x_pnt_cnt
		return self.__oper_x_engate

	@property
	def oper_i_engate_arc(self):
		self.__oper_i_engate_arc = ( self.__oper_x_engate - self.__oper_x_retract ) / 2
		return self.__oper_i_engate_arc

	@property
	def lista(self):
		return self.__lista

	@classmethod
	def criar(  cls,
                oper_tipy,
                oper_name,
				oper_limits_coord,
				oper_mod_select,
				oper_side_tool,
                oper_dmt_maior,
                oper_dmt_menor,
				oper_z_init,
                oper_z_finish,
				oper_pas_add,
                oper_side_incr,
				oper_side_estoq,
				oper_z_incr,
				oper_thread_pitch,
				oper_engate,
				oper_retrair,
                oper_z_sob,
				oper_z_transf,
                oper_speed_spindle,
                oper_speed_cutting):

		oper =  cls(	oper_tipy,
		                oper_name,
						oper_limits_coord,
						oper_mod_select,
						oper_side_tool,
                		oper_dmt_maior,
                		oper_dmt_menor,
						oper_z_init,
                		oper_z_finish,
						oper_pas_add,
                		oper_side_incr,
						oper_side_estoq,
						oper_z_incr,
						oper_thread_pitch,
						oper_engate,
						oper_retrair,
                		oper_z_sob,
						oper_z_transf,
                		oper_speed_spindle,
                		oper_speed_cutting)

		erros = Operacao.__validar(oper)

		if len(erros) == 0:
			Operacao.__dados.append(oper)
		return erros

	@classmethod
	def __validar(cls, oper, alteracao=False):
		erros = []
		return erros