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
from semantica import Prog
from semantica import Skip
from semantica import Atrib
from semantica import Seq
from semantica import While
from semantica import Do
from semantica import If
from semantica import Either
# Este é um exemplo de expressão Bool 

z = Estado([])

vx = ValorBool(True)
vy = ValorBool(False)
xi = ValorInt(3)

z.adicionar("x",vx)
z.adicionar("y",vy)
z.adicionar("xi",xi)

bop1 = Bop("||","y","x")#True
bop2 = Bop("&&","x","y")#False
bop3 = Bop("&&",bop1,bop2)#False
a1 = BoolE(bop3)#False


o1 = Op("-","xi",2)#1
rop1 = Rop("<",o1,5)#True
ax11 = BoolE(rop1)#False
a2 = BoolE(ax11)#False


bop4 = Bop("&&",a1,a2)
a3 = BoolE(bop4)#

bop5 = Nop("!",a3)
a4 = BoolE(bop5)#

print(a1.arv(z))
print(a2.arv(z))
print(a3.arv(z))
print(a4.arv(z))

z.print_estado()