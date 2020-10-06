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
# Este é um exemplo de arvore

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

o1 = Op("-","xi",2)#3
rop1 = Rop("<",o1,5)#True
ax11 = BoolE(rop1)
ax1 = BoolE(ax11)

nop1 = Nop("!",ax1)#False
bop1 = Bop("&&",nop1,"xb")#True
ax2 = BoolE(bop1)

bop2 = Bop("&&",ax2,ax11)
ax3 = BoolE(bop2)

print(ax1.arv(z))
print(ax2.arv(z))
print(ax3.arv(z))

z.print_estado()
