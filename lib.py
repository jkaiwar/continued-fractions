def list_invariants(p,q):
    A = []
    for i in range(p):
        A.append(ds(p,q,i))
    return A
