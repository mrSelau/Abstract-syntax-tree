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
#Esta execução é um exemplo de do

z = Estado([])

vxb = ValorBool(True)
vyb = ValorBool(False)
vxi = ValorInt(0)
vyi = ValorInt(3)
vzi = ValorInt(1)


z.adicionar("xb",vxb)
z.adicionar("yb",vyb)
z.adicionar("xi",vxi)
z.adicionar("yi",vyi)
z.adicionar("zi",vzi)

z.print_estado()

o1 = Op("+","xi","zi")#13

a = Atrib("xi", ":=", o1)

rop = Rop("==","yi","xi")
nop = Nop("!",rop)

d = Do("do",a,nop)

p = Prog(d,z)
p.prog()

z.print_estado()