from valorBool import ValorBool
from valorInt import ValorInt

class Estado(): 	
	def __init__(self, ambiente):
		if ambiente == []:
			self.ambiente = ambiente

	def adicionar(self, var, valor):
		if type(var) != str:
			return
		if ((type(valor) != ValorBool) and (type(valor) != ValorInt)) and ((type(valor) != bool) and (type(valor) != int)):
			return
		if self.contem_var(var):
			return
		self.ambiente.append((var,valor))

	def get_valor_estado(self, var):
		i = self.indice(var)
		a = self.ambiente[i][1]
		if (type(a) == int) or (type(a) == bool):
			return a
		return a.getValor()

	def atualizar(self, var, valor):
		aux = self.indice(var)
		print(aux)
		self.ambiente[aux] = (var,valor)

	def delete(self, var):
		del(self.ambiente[self.indice(var)])


	def indice(self, var):
		for i in range(len(self.ambiente)):
			if var == self.ambiente[i][0]:
				return i

	def contem_var(self, var):
		for i in self.ambiente:
			if i[0] == var:
				return True
		return False

	def estado():
		return self.ambiente

	def print_estado(self):
		a = "["
		for i in self.ambiente:
			if (type(i[1]) == int) or (type(i[1]) == bool):
				a += str(i[0]) + "->" + str(i[1]) + ", "
				continue 
			a += str(i[0]) + "->" + str(i[1].getValor()) + ", "
		print(a[:-2]+"]")