from valorBool import ValorBool
from ambiente import Estado
from valorInt import ValorInt
from ambiente import Estado
from valorBool import ValorBool
from valorInt import ValorInt
from arv import Arv
from arv import AritE
from arv import Op
from arv import BoolE
from arv import Bop
from arv import Rop
from arv import Nop
from random import randint

class Prog():
	def __init__(self, a, estado):
		self.a = a
		self.estado = estado

	def prog(self):
		self.prog_(self.a, self.estado)

	def prog_(self, x, estado):
		if type(x) == Skip:
			x.skip(estado)
		if type(x) == Atrib:
			x.atrib(estado)
		if type(x) == Seq:
			x.seq(estado)
		if type(x) == While:
			x.while_(estado)
		if type(x) == Do:
			x.do_(estado)
		if type(x) == If:
			x.if_(estado)
		if type(x) == Either:
			x.either_(estado)
########################################################
class Skip(Prog):
	def __init__(self):
		pass

	def skip(self, estado):
		print("Skip")
########################################################
class Atrib(Prog):
	def __init__(self, a, b, c):
		if b == ":=":
			self.a = a
			self.b = b
			self.c = c

	def atrib(self, estado):
		x = self.c
		if (type(x) == ValorInt) or (type(x) == ValorBool):
			nova = x.getValor()
		elif (type(x) == int) or (type(x) == bool):
			nova = x
		else:
			nova = x.arv_(x,estado)
		estado.atualizar(self.a, nova)
		print("Atrib -> ", self.a,self.b, nova)
########################################################
class Seq(Prog):
	def __init__(self, a, b, c):
		if b == ";":
			self.a = a
			self.b = b
			self.c = c

	def seq(self, estado):
		super().prog_(self.a,estado)
		print("SEQ")
		super().prog_(self.c,estado)
########################################################
class While(Prog):
	def __init__(self, a, b, c):
		if a == "while":
			self.a = a
			self.b = b
			self.c = c

	def while_(self,estado):
		x = self.b
		b = True
		if (type(x) == Bop):
			b =  x.confereBop(estado)
		if (type(x) == Rop):
			b = x.confereRop(estado)
		if (type(x) == Nop):
			b = x.confereNop(estado)

		if b == True:	
			super().prog_(self.c,estado)
			self.while_(estado)


########################################################
class Do(Prog):
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def do_(self,estado):		
		super().prog_(self.b,estado)

		x = self.c

		aux = True
		if (type(x) == Bop):
			aux =  x.confereBop(estado)
		if (type(x) == Rop):
			aux = x.confereRop(estado)
		if (type(x) == Nop):
			aux = x.confereNop(estado)

		if aux == True:
			self.do_(estado)
########################################################
class If(Prog):
	def __init__(self, a, b, c, d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d

	def if_(self, estado):
		x = self.b

		aux = True
		if (type(x) == Bop):
			aux =  x.confereBop(estado)
		if (type(x) == Rop):
			aux = x.confereRop(estado)
		if (type(x) == Nop):
			aux = x.confereNop(estado)

		if aux == True:
			super().prog_(self.c,estado)
			return
		super().prog_(self.d,estado)

class Either(Prog):
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def either_(self, estado):
		x = randint(0,1)
		if x == 0:
			super().prog_(self.b,estado)
			return
		super().prog_(self.c,estado)