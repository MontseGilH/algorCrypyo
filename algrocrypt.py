"""
Programa para encriptar mensajes
Matematica discreta
Programado por: Montserrat Gil
Fecha 9/05/2022
"""

# p y q son los dos primos
# si se tiene un valor de e, escribirlo, sino, false
def llavePublica(p,q,e1):
    n=p*q
    phi=(p-1)*(q-1)
    if not e1:
        
    else: 
        e=e1
    return n,e

def encriptar(n,e,string):
    
