class ValorBool: 	

	def __init__(self, valor):
		if type(valor) == bool:
			self.valor = valor

	def getValor(self):
		return self.valor

	def ler(self):
		print(self.valor)
