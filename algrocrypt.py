"""
Programa para encriptar mensajes
Matematica discreta
Programado por: Montserrat Gil
Fecha 9/05/2022
"""

# p y q son los dos primos
# si se tiene un valor de e, escribirlo, sino, false
def crearEyD(p,q,e1):
    phi=(p-1)*(q-1)
    if not e1:
        e=2
        while not (mcd(phi,e)==1):
            e+=1
    else: 
        e=e1
    d=inverso2(e,phi)   
    return e,d

def inverso1(num1,num2):
    if num1==0:
        return (num2,0,1)
    else:
        a,b,c = inverso1(num2%num1,num1)
        return (a,c-(num2//num1)*b,b)
    
def inverso2(num,mod):
    a,b,c=inverso1(num,mod)
    if a !=1:
        return False
    return b%mod 

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

def mod(n,p,m):
    if p==0:
        return 1
    if p%2==0:
        return (mod(n,p/2,m)**2)%m
    else:
        return (n*mod(n,(p-1)/2,m)**2)%m

def b(n):
    b=0
    lim="27"
    while int(lim)<n:
        b+=2
        lim+="27"
    return b
            
def encriptar(n,e,string,b):
    letras= {
        " ":"00","a":"01","b":"02","c":"03","d":"04","e":"05","f":"06","g":"07","h":"08","i":"09","j":"10","k":"11","l":"12","m":"13","n":"14","ñ":"15","o":"16","p":"17","q":"18","r":"19","s":"20","t":"21","u":"22","v":"23","w":"24","x":"25","y":"26","z":"27",
    }
    mensajeNum=""
    for s in string.lower():
        mensajeNum+=letras[s]
    while not (len(mensajeNum)%b)==0:
        mensajeNum+="00"
    mensajeEntript=""
    for i in range(int(len(mensajeNum)/b)):
        cr1=int(mensajeNum[b*i:b+i*b])
        c=str(mod(cr1,e,n))
        while len(c)<b:
            c="0"+c
        mensajeEntript+=c+" "
    return mensajeEntript

def desencriptar(d,n,mensaje,b):
    letras=[" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    bloques=mensaje.split()
    final=""
    for bloque in bloques:
        res = str(mod(int(bloque),d,n))
        while len(res)<b:
            res="0"+res
        for i in range(int(b/2)):
            numl=int(res[2*i:2+2*i])
            final+=letras[numl]
    return final  

class Encriptor:
    
    def __init__(self,p,q,e1):
        self.n=p*q
        self.e,self.d=crearEyD(p,q,e1)
        self.b=b(self.n)
    
    def encript(self,string):
        return encriptar(self.n,self.e,string,self.b)
    
    def desencript(self,string):
        return desencriptar(self.d,self.n,string,self.b)

encr=Encriptor(953647,953593,False)
mensEncr=encr.encript("hola como estas maria")
mensajeDesencr=encr.desencript(mensEncr)
print(mensEncr)
print(mensajeDesencr)



