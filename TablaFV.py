k = 0
memoriaC = 501
tablaC = {}
scope = "global"
cFloat = 5000
cInt = 6000
cBool = 7000
cChar = 8000  
class  tablas():
    tablaF = {}
    tablaEra = {}
    i = 0 
    #scope = "global"
    tablaV = {}
    tablaC = {}
    j=0
    #k = 0
    memoriaF = 0
    memoriaV = 0
    
    auxMemVarG = 0
    fNoHayGlobal = True

    def agregarF(self, nombre, tipo, valor):  
        self.tablaF[self.i]= {'name': nombre, 'type': tipo, 'value': valor, 'memoria' : self.memoriaF}
        self.i += 1
        
    m = 0
    def agregarC(self, valor, tipo):  
        global k
        global cFloat
        global cInt
        global cBool
        global cChar
        global tablaC 
         
        if(tipo == 'float'):
            cFloat +=1 
            self.m = cFloat
        elif(tipo == 'int'):
            cInt +=1 
            self.m = cInt
        elif(tipo == 'char'):
            cChar +=1 
            self.m = cChar
        elif(tipo == 'bool'):
            cBool +=1 
            self.m = cBool
        
        tablaC[k]= {'type': tipo, 'value': valor, 'memoria' : self.m}
        k = k + 1

    
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

    def buscarM(self, nombre):
        w = 1
        auxMem =''
        while(w <= len(self.tablaV)):
            if (self.tablaV[w]['name'] == nombre):
                #print("valor: ", valor)
                auxMem = self.tablaV[w]['memoria'] 
                #print("y su valor es: ",self.tablaV[w]['value'])# : valor
            w +=1
        return auxMem

    def buscarTypeC(self, nombre):
        w = 0
        auxVal =''
        while(w < len(tablaC)):
            if (tablaC[w]['memoria'] == nombre):
                #print("valor: ", valor)
                auxVal = tablaC[w]['type'] 
                #print("y su valor es: ",self.tablaV[w]['value'])# : valor
            w +=1
            #print("WACHA: ",tablaC)
        return auxVal

    def buscarTypeV(self, nombre):
        w = 1
        auxVal =''
        while(w <= len(self.tablaV)):
            #if (self.tablaV[w]['nombre'] == nombre):
                #print("valor: ", valor)
            try:
                auxVal = self.tablaV[w]['type'] 
                #print("y su valor es: ",self.tablaV[w]['value'])# : valor
            except:
                pass
            w +=1
        return auxVal
    
    def buscarF(self, nombre):
        w = 0
        #auxMem =''
        print("la len es: ", len(self.tablaF))
        
        while(w < len(self.tablaF)):
            print("w es :", w)
            if (self.tablaF[w]['name'] == nombre):
                #print("valor: ", valor)
                return True
                #print("y su valor es: ",self.tablaV[w]['value'])# : valor
            
            w +=1
        return False


    funFloat = 1000
    funInt = 2000
    funBool= 3000
    funChar = 4000
    def agregarV(self, nombre, tipo, valor):
        print("scope", scope)
        self.j += 1

        # si la primera variable es en global
        if(scope == "global"  and self.memoriaV < 1000):
            self.memoriaV += 1
            self.auxMemVarG += 1
            self.fNoHayGlobal = False
        # cuando vuelve a global 
        elif(scope == "global" and self.memoriaV >= 1000 ):
            self.memoriaV = self.auxMemVarG + 1
        # cuando esta dentro de un scope no global
        elif( scope != "global"):
            if(tipo == 'float'):
                self.funFloat += 1 
                self.memoriaV = self.funFloat
                self.tablaEra[scope][1000] +=1
            elif(tipo == 'int'):
                print("entre al int")
                self.funInt += 1 
                self.memoriaV = self.funInt
                self.tablaEra[scope][2000] +=1
            elif(tipo == 'bool'):
                self.funBool += 1 
                self.memoriaV = self.funBool
                self.tablaEra[scope][3000] +=1
            elif(tipo == 'char'):
                self.funChar += 1 
                self.memoriaV = self.funChar
                self.tablaEra[scope][4000] +=1
        else:
            self.memoriaV += 1

        self.tablaV[self.j] = {'name': nombre, 'type': tipo, 'value': valor, 'scope': scope, 'memoria' : self.memoriaV}

    
