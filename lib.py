from fractions import Fraction
import numpy as np

 
## a%p = n   function to find n such that n is between 0 and p and n is congruent to a modp
def cong(a,p):
    if a%1 != 0 or p%1 != 0:
        return 'Function requires integer input.'
    if a == 0:
        return 0
    n = 0
    for i in range(1,p + 1):
        if (i - a)%p == 0:
            n = n + i
            break
    return n
 
 
## the d invariance function
def d_inv(p,q,i):
    if p%1 != 0 or q%1 != 0 or i%1 != 0:
        return 'Function requires integer input.'
    if p <= 0:
        return 'p must be positive'                            
    if not 0 <= i < (p + q):
        return 'Must have i greater than or equal to zero and less than p+q'
    if q <= 0:
        q = p + q                                              #Using S(p,-q) = S(p,p - q)
    if p == 1:
        return 0
    ans = 0
    count = 0
    while p > 1:
        if q > p:                                                    ## not sure about when p = q
            i = cong(i,p)
            q = cong(q,p)
        if count%2 == 0:
            ans = ans + ((((2*i) + 1 - p - q)**2) - p*q)/(4*p*q)
        else:
            ans = ans - ((((2*i) + 1 - p - q)**2) - p*q)/(4*p*q)
        b = p
        p = q
        q = b
        count = count + 1
    return Fraction(ans).limit_denominator()
   
 
for i in range(9):
    print(d_inv(9,7,i))



def list_invariants(p,q):
    A = np.zeros(p-1).astype('object')
    for i in range(p-1):
        A[i] = (d_inv(p,q,i+1))
    return A



def columns_repeat(A):
    for i in range(A.shape[1]):
        for j in range(A.shape[1]):
            if ((A[:,0] == A[:,1]).any()):
                return False
    return True
    

            
