def llavePublica(p,q):
    n=p*q
    phi=(p-1)*(q-1)
    si=False
    e=2
    while not si:
        if phi%e==0:
            e+=1
        else:
            si=True
    return n,e

