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
# Este é um exemplo de expressão arit

z = Estado([])

vx = ValorInt(5)
vy = ValorInt(20)


z.adicionar("x",vx)
z.adicionar("y",vy)

o1 = Op("-","x",1,)#4
a1 = AritE(o1)#4

a2 = AritE("y")#20

o2 = Op("*",a1,a2)#80
a3 = AritE(o2)#80

o3= Op("-", a2, a3)#-60
a4 = AritE(o3)#-60

print(a4.arv(z))

z.print_estado()