print("Act 9 clases v3")
print("Balderrama Karla  Mat: 22308051281149")
#zona clases
class operadores1149():
    # Zona de funciones
    def suma1149(self,K,B):
        s1149=K +B
        print(f"La suma de {K} + {B} = {s1149}")
    def resta1149(self,K, B):
        r1149= K-B
        print(f"La resta de {K} - {B} = {r1149}")
    def multi1149(self, K,B):
        m1149= K*B
        print(f"La multiplicacion de {K} * {B} = {m1149}")
    def divi1149(self, K, B):
        d1149= K/B
        print(f"La division de {K} / {B} = {d1149}")
    def mod1149(self, K,B):
        mod1149= K%B
        print(f"El modulo de {K} % {B} = {mod1149}")
    def exponente1149(self, K, B):
        expo1149= K**B
        print(f"El exponente de {K} ** {B} = {expo1149}")
    def cociente1149(self, K,B):
        coci1149= K//B
        print(f"El cociente de {K} // {B} = {coci1149}")
        
# creacion del objeto
operabalderrama = operadores1149()

#Zona de uso de objetos
print("Funcion suma ")
operabalderrama.suma1149(5,6)
print("Funcion resta")
operabalderrama.resta1149(6,4)
print("Funcion Multiplicacion ")
operabalderrama.multi1149(3,3)
print("Funcion Division")
operabalderrama.divi1149(12,3)
print("Funcion Modulo")
operabalderrama.mod1149(5,4)
print("Funcion Exponente")
operabalderrama.exponente1149(3,2)
print("Funcion Cociente")
operabalderrama.cociente1149(6,3)