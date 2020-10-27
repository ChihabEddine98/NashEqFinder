import numpy as np

from algos.Solver import *
from gui.App import *


if __name__ == '__main__':
    m=[[(1,3),(2,5)],[(6,1),(2,2)]]
    m2=[[(1,4),(2,2)],[(0,1),(3,6)]]
    m3=[[(0,1),(4,1),(2,3)],[(4,1),(2,1),(5,5)],[(-1,1),(2,8),(3,5)]]
    m4=[[(3,-3),(-2,2)],[(-1,1),(0,0)]]

    # M=np.array(m4)
    # s=Solver(payoff=M)
    # s.solve(1,1)

    # Gui part !
    app=App()
    app.mainloop()


