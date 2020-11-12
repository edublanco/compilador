

class  tablas():
    tablaF = {}
    i = 0 
    scope = "global"
    tablaV = {}
    j=0
    memoriaF = 0
    memoriaV = 0
    auxMemVarG = 0
    fNoHayGlobal = True

    def agregarF(self, nombre, tipo, valor):  
        self.tablaF[self.i]= {'name': nombre, 'type': tipo, 'value': valor, 'memoria' : self.memoriaF}
        self.i += 1
        

    def checa(self,nombre):
        w = 1
        while(w <= len(self.tablaV)):
            if (self.tablaV[w]['name'] == nombre):
                return True
            w +=1

    def agregarValor(self,nombre, valor):
        w = 1
        while(w <= len(self.tablaV)):
            if (self.tablaV[w]['name'] == nombre):
                #print("valor: ", valor)
                self.tablaV[w]['value'] = valor
                #print("y su valor es: ",self.tablaV[w]['value'])# : valor
            w +=1

    def extraerValor(self, nombre):
        w = 1
        auxTipo =''
        while(w <= len(self.tablaV)):
            if (self.tablaV[w]['name'] == nombre):
                #print("valor: ", valor)
                auxTipo = self.tablaV[w]['value'] 
                #print("y su valor es: ",self.tablaV[w]['value'])# : valor
            w +=1
        return auxTipo

    def agregarV(self, nombre, tipo, valor):
        
        self.j += 1
        # checa si la memoria es global
        # memoria de la variable en en 1, el aux es para cuando vuelva a global
        if(tablas.scope == "global"  and self.memoriaV < 1000):
            self.memoriaV += 1
            self.auxMemVarG += 1
            self.fNoHayGlobal = False
        
        # checa si el scope es otra vez global y le resta a la direccion de memoria de las variables
        # la direccion de memoria de funciones para devolver la direccion memoria a global, y continua el conteo de memoria global
        elif(self.scope == "global" and self.memoriaV >= 1000 ):
            self.memoriaV -= self.memoriaF 
            self.memoriaV = self.auxMemVarG + 1

        elif ( self.fNoHayGlobal ): 
            #self.memoriaV += 1
            self.memoriaV = self.memoriaF +1
        # si sigue en el scope de la misma funcion nomas suma 1 a la direcion de memoria de las variables
         # checa si la direccion memoria es del mismo scope, sino empieza 
         # la direccion de memoria de las variables en en 1 + la direecion de memoria de la funcion
        
        elif (self.scope != self.tablaV[self.j - 1]['scope']  ): 
            #self.memoriaV += 1
            self.memoriaV = self.memoriaF +1
            #self.memoriaV += 1000
        else:
            self.memoriaV += 1
        
        #print("memoriaf: ", self.memoriaF )
        #print("memoriaV: ", self.memoriaV )


        self.tablaV[self.j] = {'name': nombre, 'type': tipo, 'value': valor, 'scope': self.scope, 'memoria' : self.memoriaV}
        #print(self.tablaV)
    
