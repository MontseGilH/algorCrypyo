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
        e=2
        while not (mcd(phi,e)==1):
            e+=1
    else: 
        e=e1
    return n,e

def mcd(num1,num2):
    fin=False
    while not fin:
        division = int(num1/num2)
        resto = num1%num2
        if resto==0:
            return num2
        else:
            temp1=num1
            num1=num2
            num2=temp1-(division*num2)
        

def encriptar(n,e,string):
    letras= {
        " ":"00","a":"01","b":"02","c":"03","d":"04","e":"05","f":"06","g":"07","h":"08","i":"09","j":"10","k":"11","l":"12","m":"13","n":"14","ñ":"15","o":"16","p":"17","q":"18","r":"19","s":"20","t":"21","u":"22","v":"23","w":"24","x":"25","y":"26","z":"27",
    }
    mensajeNum=""
    for s in string.lower():
        mensajeNum+=letras[s]
    b=0
    lim="27"
    while int(lim)<n:
        b+=2
        lim+="27"
    while not (len(mensajeNum)%b)==0:
        mensajeNum+="00"
    lista=[]
    start=0
    for i in range(int(len(mensajeNum)/b)):
        lista.append(mensajeNum[start:start+b])
        start=start+b
    for l in range(len(lista)):
        cr1=int(lista[l])
        c=str(mod(cr1,e,n))
        while len(c)<4:
            c="0"+c
        lista[l]=c
    mensajeEntript=""
    for k in lista:
        mensajeEntript+=k+" "
    return mensajeEntript

def mod(n,p,m):
    if p==0:
        return 1
    if p%2==0:
        return (mod(n,p/2,m)**2)%m
    else:
        return (n*mod(n,(p-1)/2,m)**2)%m

print(encriptar(2999,3,"hola"))

def inverso(num1,mod):
    for i in range(mod):
        if (i*num1)%mod==1:
            return i

def decript(mensaje,n,e):
    d=inverso(e,n)
print(inverso(13,2436))
