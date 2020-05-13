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



# Recursive d-invariant
def dS(p,q,i):
    # checking input values are positive integers
    if ((not isinstance(p, int)) or (p <= 0)):
        raise Exception('p must be a positive integer. p was {}.'.format(p))
    
    if ((not isinstance(q, int)) or (q <= 0)):
        raise Exception('q must be a positive integer. q was {}.'.format(q))

    if ((not isinstance(i, int)) or (i < 0)):
        raise Exception('i must be a non-negative integer. i was {}.'.format(i))
    
    # checking p and q are coprime
    if (np.gcd(p,q) != 1):
        raise Exception('p and q must be coprime.')

    # we terminate if p = 1
    if (p == 1):
        return Fraction(0,1)

    q = q%p
    i = i%p
    r = Fraction(((((2*i) + 1 - p - q)**2) - p*q),(4*p*q))
    # our recursive step is safe since we have checked for bad input and reduced q and i mod p.
    return r - dS(q,p,i)



def list_invariants(p,q):
    A = np.zeros(p).astype('object')
    for i in range(p):
        A[i] = (dS(p,q,i))
    return A



def columns_repeat(A):
    for i in range(A.shape[1]):
        for j in range(A.shape[1]):
            if ((A[:,0] == A[:,1]).any()):
                return False
    return True
    

            
