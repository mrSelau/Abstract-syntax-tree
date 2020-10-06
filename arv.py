from valorBool import ValorBool
from ambiente import Estado
from valorInt import ValorInt

class Arv():
	def __init__(self, a,):
		self.a = a
		self.b = ""

	def arv(self, estado):
		return self.arv_(self.a, estado)

	def arv_(self, x, estado):
		if (type(x) == Bop):
			return x.confereBop(estado)
		if (type(x) == Rop):
			return x.confereRop(estado)
		if (type(x) == Nop):
			return x.confereNop(estado)
		if (type(x) == Op):
			return x.confereOp(estado)

		if (type(x) == ValorBool):
			return x.getValor(estado)
		if (type(x) == ValorInt):
			return x.getValor(estado)

		if (type(x) == bool):
			return x
		if (type(x) == int):
			return x

		if (type(x) == str):
			return estado.get_valor_estado(x)

		if (type(x) == AritE):
			return self.arv_(x.get_arv(),estado)	
		if (type(x) == BoolE):
			return self.arv_(x.get_arv(),estado)

	def get_arv(self):
		return self.a
#########################################################
#########################################################
class BoolE(Arv):
	def __init__(self, a):
		self.a = a
		self.b = ""

	def arvBool(self,estado):
		return super().arv_(self.a, estado)

	def get_arv(self):
		return self.a

class AritE(Arv):
	def __init__(self, a):
		self.a = a
		self.b = ""

	def arvArit(self,estado):
		return super().arv_(self.a, estado)

	def get_arv(self):
		return self.a
######################################################################
######################################################################

class Bop(BoolE):

	def __init__(self, bop, a, b):
		self.bop = bop
		self.a = a
		self.b = b

	def confereBop(self,estado):
		if self.bop == "&&":
			return self.conj(estado)
		if self.bop == "||":
			return self.disj(estado)

	def conj(self,estado):
		return super().arv_(self.a,  estado) and super().arv_(self.b, estado)

	def disj(self,estado):
		return super().arv_(self.a, estado) or super().arv_(self.b, estado)


class Rop(BoolE):

	def __init__(self, rop, a, b):
		self.rop = rop
		self.a = a
		self.b = b

	def confereRop(self,estado):
		if self.rop == ">":
			return self.maior(estado)
		if self.rop == "<":
			return self.menor(estado)
		if self.rop == "==":
			return self.igual(estado)

	def maior(self,estado):
		return super().arv_(self.a,  estado) > super().arv_(self.b, estado)

	def menor(self,estado):
		return super().arv_(self.a, estado) < super().arv_(self.b, estado)

	def igual(self,estado):
		return super().arv_(self.a, estado) == super().arv_(self.b, estado)

class Nop(BoolE):

	def __init__(self, nop, a):
		self.nop = nop
		self.a = a
		self.b = ""

	def confereNop(self,estado):
		if self.nop == "!":
			return self.neg(estado)

	def neg(self,estado):
		return not (super().arv_(self.a, estado))

##############################################################################################
class Op(AritE):

	def __init__(self, op, a, b):
		self.op = op
		self.a = a
		self.b = b

	def confereOp(self,estado):
		if self.op == "+":
			return self.soma(estado)
		if self.op == "-":
			return self.subtrai(estado)
		if self.op == "*":
			return self.multiplica(estado)

	def soma(self,estado):
		return super().arv_(self.a,  estado) + super().arv_(self.b, estado)

	def subtrai(self,estado):
		return super().arv_(self.a, estado) - super().arv_(self.b, estado)

	def multiplica(self,estado):
		return super().arv_(self.a, estado) * super().arv_(self.b, estado)



