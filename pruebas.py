


if __name__ == '__main__':
    tablaV = {};
    tablaF = {};
    scope = "global"
    i =0 
    j=0

    def agregarV(nombre, tipo, valor, scope):  
        tablaV[i] = {'name': nombre, 'type': tipo, 'value': valor, 'scope':scope}

    def agregarF(nombre, tipo, valor):
        tablaF[j] = {'name': nombre, 'type': tipo, 'value': valor}
        
    nombre = input("nombre?")
    tipo = input("tipo?")
    valor = input("valor?")
    scope = nombre
    agregarF(nombre, tipo, valor)
    j = j+1

    while(i<2):
        nombre = input("nombre var?")
        tipo = input("tipo?")
        valor = input("valor?")
        agregarV(nombre, tipo, valor, scope)
        i = i+1
    
    nombre = input("nombre de segunda funcion?")
    tipo = input("tipo?")
    valor = input("valor?")
    scope = nombre
    agregarF(nombre, tipo, valor)
    j = j+1

    while(i<4):        
        nombre = input("nombre var?")
        tipo = input("tipo?")
        valor = input("valor?")

        agregarV(nombre, tipo, valor, scope)
        i = i+1


    print(tablaF)
    print(tablaV)

    
    
    
   
        
    