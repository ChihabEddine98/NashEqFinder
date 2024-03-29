import numpy as np
from typing import Final
from fractions import Fraction


"""--------------------------------------
# Constants !
# --------------------------------------
# 1/Shape of Matrix ( Game strategies )
#  Basically  : 2x2 Game
 --------------------------------------"""
DIM: Final = (2, 2)
# Because we have matrix of couples ( payoff for Player 1 & Player 2 )
payoff_type = np.dtype(int, int)


class Solver:
    def __init__(self, payoff):
        self.M = payoff

    # This algo give us the result in linear time o(n) !
    def solve_pure(self):
        possible_nash1 = []
        possible_nash2 = []
        # Best responses for Player 1 against Player 2 strategies
        for j in range(DIM[1]):
            x_max = max(self.M[:, j], key=lambda x: x[0])
            a = [tuple(x) for x in self.M[:, j]]

            if(a[0]==a[1]):
                best_reply1 = [(a[0],(0,j)),(a[1],(1,j))]
            else:
                best_reply1 = [(tuple(x), (a.index(tuple(x)), j)) for x in self.M[:, j] if x[0] == x_max[0]]

            possible_nash1 += best_reply1
        print(possible_nash1)

        # Best responses for Player 2 against Player 1 strategies
        for i in range(DIM[0]):
            y_max = max(self.M[i, :], key=lambda y: y[1])
            a = [tuple(x) for x in self.M[i, :]]
            if(a[0]==a[1]):
                best_reply2 = [(a[0],(i,0)),(a[1],(i,1))]
            else:
                best_reply2 = [(tuple(y), (i, a.index(tuple(y)))) for y in self.M[i, :] if y[1] == y_max[1]]


            # best_reply2 = [tuple(y) for y in self.M[i,:] if y[1] == y_max]
            possible_nash2 += best_reply2
        print(possible_nash2)
        # Intersection of two lists give us the Nash equilibria !
        result = [ x[1] for x in list(set(possible_nash1) & set(possible_nash2))]
        print(result)

        return result
    
    def solve_pure_nxn(self,dim=3):
        pne1 , pne2 = [] , []
        # Best responses for Player 1 against Player 2 strategies 
        # Than those for Player 2 against Player 1
        for i , j in zip(range(dim),range(dim)):
            x_max , y_max = max(self.M[:, j], key=lambda x: x[0]) , max(self.M[i, :], key=lambda y: y[1])
            a , b = [tuple(x) for x in self.M[:, j]] , [tuple(x) for x in self.M[i, :]]
            
            if(a[0] == a[1]):
                best_reply1 = [(a[0],(0,j)),(a[1],(1,j))]
            else:
                best_reply1 = [(tuple(x), (a.index(tuple(x)), j)) for x in self.M[:, j] if x[0] == x_max[0]]
                 
            if(b[0] == b[1]):
                best_reply2 = [(b[0],(i,0)),(b[1],(i,1))]
            else:
                best_reply2 = [(tuple(y), (i, b.index(tuple(y)))) for y in self.M[i, :] if y[1] == y_max[1]]
                
            pne1 += best_reply1
            pne2 += best_reply2
            
        print(f'Best Replies (payoff,position) for Player 1 : {pne1}')
        print(f'Best Replies (payoff,position) for Player 2 : {pne2}')
        
        # Intersection of two lists give us the Nash equilibria !
        res = [x for x in list(set(pne1) & set(pne2))]
        print(f'NE\'s (payoff,position)  : {res}')
        
        result = [x[1] for x in list(set(pne1) & set(pne2))]
        print(result)

        return result
        
    """
        We will try to solve to equations of type : ( find p and q )
        a*p=b
        c*q=d
        ( How we got this a,b,c and d coeiffitiions ? ) 
        for example : 
                      q                  1-q
                      C                   D
             ---------------------------------------------
    p      A        (3,-3)       |        (-2,2)     
             ---------------------------------------------  
    1-p    B        (-1,1)       |         (0,0)
             ---------------------------------------------    

        If we apply the definition of mixed strategy Nash Equ we will get : 
        For Player 1 :
        -3p + 1(1-p) = 2p + 0(1-p)
        For Player 2 : 
        3q + (-2)(1-q) = -1q + 0(1-q)

        So our goal is to solve this linear system ! 
        Lets make it like the format in the start of this example :
        (-3-1-2+0)p = -1 + 0
        (3+2+1+0)q  = +2 + 0

        Cool we have now our a,b,c and d coeiff ! lets do our thing :
        p = 1/6
        q = 1/3
    """
    
    


    # This algo give us the results in constant time ! cool o(1)
    def solve_mixed(self):
        a = (self.M[0, 0][1] - self.M[1, 0][1] - self.M[0, 1][1] + self.M[1, 1][1])
        b = (-self.M[1, 0][1] + self.M[1, 1][1])

        c = (self.M[0, 0][0] - self.M[0, 1][0] - self.M[1, 0][0] + self.M[1, 1][0])
        d = (-self.M[0, 1][0] + self.M[1, 1][0])

        p = b / a if a != 0 else None
        q = d / c if c != 0 else None

        if(p and q):
            p=Fraction(p).limit_denominator()
            q=Fraction(q).limit_denominator()

        print(f'p = {p} \nq = {q}')
        return (p,q)

    # This algo give us the result in linear time o(n) !
    def solve_all(self):
        return (self.solve_pure(),self.solve_mixed())

    def solve(self, pure=1, mixed=1):
        if (pure and mixed):
            return self.solve_all()
        elif (pure and not mixed):
            return self.solve_pure()
        elif (not pure and mixed):
            return self.solve_mixed()
        else:
            return self.solve_pure_nxn()