from TablaFV  import * 
from CuboSemantico import cubo

class  cuad():
    tablaQ = {}
    i = 1 
    sOperadores = []
    sTemp = []
    sTipo = []

    variable = ''
    fin = False
    tablas=tablas()

    opDer = 0
    opIzq = 0
    operador = ''
    resultado = 0

    def agregaCons(self,valor):  
        self.sTemp.append(valor)
        
    def agregaOp(self,valor):
        if(  (valor != 'end')and ((len(self.sOperadores) == 0) or (self.sOperadores[len(self.sOperadores) -1] == '(' and valor != ')') )):
            self.sOperadores.append(valor)
        
        elif((valor == '+' or valor == '-') and  (self.sOperadores[len(self.sOperadores) -1] == '*' or self.sOperadores[len(self.sOperadores) -1] == '/' or self.sOperadores[len(self.sOperadores) -1] == '+' or self.sOperadores[len(self.sOperadores) -1] == '-')) :
            self.operador = self.sOperadores.pop()
            self.opDer = self.sTemp[len(self.sTemp) -1]
            self.opIzq = self.sTemp[len(self.sTemp) -2]
            self.sTemp.pop()
            self.sTemp.pop()
            self.agregarCuad(self.opIzq, self.opDer, self.operador)
            self.sOperadores.append(valor)
        
        elif((valor == '*' or valor == '/') and  (self.sOperadores[len(self.sOperadores) -1] == '*' or self.sOperadores[len(self.sOperadores) -1] == '/') ):  
            self.operador = self.sOperadores.pop()
            self.opDer = self.sTemp[len(self.sTemp) -1]
            self.opIzq = self.sTemp[len(self.sTemp) -2]
            self.sTemp.pop()
            self.sTemp.pop()
            self.agregarCuad(self.opIzq, self.opDer, self.operador)
            self.sOperadores.append(valor)
        
        elif(valor == '('):
            self.sOperadores.append(valor)
        elif(valor == ')' and self.sOperadores[len(self.sOperadores) -1] == '('):
            self.sOperadores.pop()
            
        elif(valor == ')'):    
            self.operador = self.sOperadores.pop()
            self.opDer = self.sTemp[len(self.sTemp) -1]
            self.opIzq = self.sTemp[len(self.sTemp) -2]
            self.sTemp.pop()
            self.sTemp.pop()
            self.agregarCuad(self.opIzq, self.opDer, self.operador)
            self.agregaOp(')')

        elif((valor == '*' or valor == '/') ):
            self.sOperadores.append(valor)
        elif((valor == '+' or valor == '-') ):
            self.sOperadores.append(valor)

        elif(len(self.sTemp) == 1):
            self.opDer = self.sTemp.pop()
            self.agregarCuad(0, self.opDer, 'end')
      
        elif(valor == 'end' and (len(self.sTemp) != 1)):
            aux = self.sOperadores.pop()
            aux2= 0
            if((aux == '+' or aux == '-') and (self.sTemp[len(self.sOperadores) -1] =='*' or self.sTemp[len(self.sOperadores) -1] =='/')):
                aux2 = aux 
                aux =  self.sOperadores.pop()
                self.sOperadores.append(aux2)

            self.operador = aux
            self.opDer = self.sTemp[len(self.sTemp) -1]
            self.opIzq = self.sTemp[len(self.sTemp) -2]
            self.sTemp.pop()
            self.sTemp.pop()
            self.agregarCuad(self.opIzq, self.opDer, self.operador)
            self.agregaOp('end') 

        

    def agregarTipo(self):
        pass

    def agregarCuad(self, opIzq, opDer, operando):
        #-----------------IMPORTANTE!!!!------------------
        #             checar lo de los ints
        opeNuevo = 0
        if(isinstance(opIzq, str)):
            try:
                int(opIzq)
                opIzq = int(opIzq)
            except:
                float(opIzq)
                opIzq = float(opIzq)

        if(isinstance(opDer, str)):
            try:
                int(opDer)
                opDer = int(opDer)
            except:
                float(opDer)
                opDer = float(opDer)

        if(operando == '+'):
            opeNuevo = opIzq + opDer
        elif(operando == '-'):
            opeNuevo = opIzq - opDer
        elif(operando == '*'):
            opeNuevo = opIzq * opDer
        elif(operando == '/'):
            opeNuevo = opIzq / opDer
        elif (operando == 'end'):
            opeNuevo = opDer
        
        self.tablaQ[self.i] = {
            'operando': operando ,
            'opIzq': opIzq, 
            'opDer': opDer, 
            'opNuevo': opeNuevo    
            }

        if(operando != 'end') :
            self.sTemp.append(opeNuevo)
            print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
            self.i += 1
        elif(operando == 'end'):
            self.resultado = opeNuevo
            print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
            print("resultado: ", opeNuevo)
            print("tabla operadores final",self.sOperadores)
            print("tabla temporales final",self.sTemp)
            self.i = 1
            self.tablaQ.clear()


        


      
    