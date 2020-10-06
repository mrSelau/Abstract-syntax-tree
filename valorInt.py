class ValorInt: 	
	
	def __init__(self, valor):
		if type(valor) == int:
			self.valor = valor

	def getValor(self):
		return self.valor

	def ler(self):
		print(self.valor)
