import numpy as np
from typing import Final


# --------------------------------------
# Contants !
# --------------------------------------
# 1/Shape of Matrix ( Game strategies )
#  Basically  : 2x2 Game
# --------------------------------------
DIM : Final =(2,2)
# Because we have matrix of couples ( payoff for Player 1 & Player 2 )
payoff_type=np.dtype(int,int)




class Solver:
    def __init__(self,payoff):
        self.M=payoff

    def solve_pure(self):
        possible_nash1=[]
        possible_nash2=[]
        # Best responses for Player 1 against Player 2 strategies
        for j in range(DIM[1]):
            best_reply1=max(self.M[:,j],key= lambda x:x[0])
            best_reply2=max(self.M[j,:],key= lambda y:y[1])

            if(np.array_equal(best_reply1,best_reply2)):
                possible_nash1.append([tuple(best_reply1),[j]])
        print(possible_nash1)
        return possible_nash1

    def solve_mixed(self):
        return 2

    def solve_all(self):
        return 3

    def solve(self,pure=1,mixed=1):
        if(pure and mixed):
            return self.solve_all()
        elif(pure and not mixed):
            return self.solve_pure()
        elif(not pure and mixed):
            return self.solve_mixed()
        else:
            return -1





if __name__ == '__main__':
    m=[[(3,3),(0,2)],[(2,0),(1,1)]]
    M=np.array(m)

    s=Solver(payoff=M)
    s.solve(1,0)
