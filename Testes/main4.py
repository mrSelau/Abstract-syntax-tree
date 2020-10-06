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
#Esta execução é um exemplo de sequencia e skip

z = Estado([])

vxb = ValorBool(True)
vyb = ValorBool(False)
vxi = ValorInt(5)
vyi = ValorInt(20)


z.adicionar("xb",vxb)
z.adicionar("yb",vyb)
z.adicionar("xi",vxi)
z.adicionar("yi",vyi)
z.atualizar("xi",ValorInt(15))

z.print_estado()

o1 = Op("+","xi",2)#13
o2 = Op("-","xi",2)#13
o3 = Op("*",o2,o1)#13
a = Atrib("xi", ":=", o3)
sk = Skip()
sq = Seq(a,";",sk)

p = Prog(sq,z)
p.prog()

z.print_estado()