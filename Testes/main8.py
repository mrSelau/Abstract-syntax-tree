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
#Esta execução é um exemplo de either

z = Estado([])

aux0 = ValorInt(0)
aux1 = ValorInt(1)
vxi = ValorInt(3)
vyi = ValorInt(3)
vzi = ValorInt(0)


z.adicionar("aux0",aux0)
z.adicionar("aux1",aux1)
z.adicionar("xi",vxi)
z.adicionar("yi",vyi)
z.adicionar("zi",vzi)

z.print_estado()

a = Atrib("zi", ":=", aux1)
b = Atrib("zi", ":=", 0)

e = Either("either",a,b)



p = Prog(e,z)
p.prog()

z.print_estado()