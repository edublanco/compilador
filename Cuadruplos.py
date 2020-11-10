from TablaFV  import * 
from CuboSemantico import cubo

class  cuad():
    tablaQ = {}
    i = 1 
    sOperadores = []
    sTemp = []
    sTipo = []

    tablas=tablas()

    opDer = 0
    opIzq = 0
    operador = ''
#parentesisIzq=0

    def agregaCons(self,valor):  
        self.sTemp.append(valor)
        
    def agregaOp(self,valor):
        if( len(self.sOperadores) == 0 or self.sOperadores[len(self.sOperadores) -1] == '(' ):
            self.sOperadores.append(valor)
        elif((valor == '+' or valor == '-') and  (self.sOperadores[len(self.sOperadores) -1] == '*' or self.sOperadores[len(self.sOperadores) -1] == '/') ):
        #--------------------------------------------------    
            self.operador = self.sOperadores.pop()
            self.opDer = self.sTemp[len(self.sTemp) -1]
            self.opIzq = self.sTemp[len(self.sTemp) -2]
            self.agregarCuad(self.opIzq, self.opDer, self.operador)
        #--------------------------------------------------
            self.sOperadores.append(valor)
        elif((valor == '+' or valor == '-') and  (self.sOperadores[len(self.sOperadores) -1] == '+' or self.sOperadores[len(self.sOperadores) -1] == '-') ):
        #--------------------------------------------------    
            self.operador = self.sOperadores.pop()
            self.opDer = self.sTemp[len(self.sTemp) -1]
            self.opIzq = self.sTemp[len(self.sTemp) -2]
            self.agregarCuad(self.opIzq, self.opDer, self.operador)
        #--------------------------------------------------
            self.sOperadores.append(valor)

        elif((valor == '*' or valor == '/') and  (self.sOperadores[len(self.sOperadores) -1] == '*' or self.sOperadores[len(self.sOperadores) -1] == '/') ):
         #--------------------------------------------------    
            self.operador = self.sOperadores.pop()
            self.opDer = self.sTemp[len(self.sTemp) -1]
            self.opIzq = self.sTemp[len(self.sTemp) -2]
            self.agregarCuad(self.opIzq, self.opDer, self.operador)
        #--------------------------------------------------
            self.sOperadores.append(valor)
        elif((valor == '*' or valor == '/') ):
            self.sOperadores.append(valor)
        elif(valor == '('):
            self.sOperadores.append(valor)
            #self.parentesisIzq = self.sOperadores[len(self.sOperadores) -1]
        elif(valor == ')' and self.sOperadores[len(self.sOperadores) -1] == ')'):
            self.sOperadores.pop()
        elif(valor == ')'):
            #--------------------------------------------------    
            self.operador = self.sOperadores.pop()
            self.opDer = self.sTemp[len(self.sTemp) -1]
            self.opIzq = self.sTemp[len(self.sTemp) -2]
            self.agregarCuad(self.opIzq, self.opDer, self.operador)
        #--------------------------------------------------
            self.agregaOp(valor)
        elif(valor == '='):
            self.sOperadores.append(valor)
            #--------------------------------------------------    
            self.operador = self.sOperadores.pop()
            self.opDer = self.sTemp[len(self.sTemp) -1]
            self.opIzq = self.sTemp[len(self.sTemp) -2]
            self.agregarCuad(self.opIzq, self.opDer, self.operador)
        #--------------------------------------------------
            self.operador = self.sOperadores.pop()
        

        print("el operador es: ",self.sOperadores)
        #print("el operador[len] es: ",self.sOperadores[len(self.sOperadores)-1])
        

    def agregarTipo(self):
        pass

    def agregarCuad(self, opIzq, opDer, operando):
        #-----------------IMPORTANTE!!!!------------------
        #             checar lo de los ints
        opeNuevo = 0
        if(operando == '+'):
            opeNuevo = int(opIzq) + int(opDer)
        elif(operando == '-'):
            opeNuevo = int(opIzq) - int(opDer)
        elif(operando == '*'):
            opeNuevo = int(opIzq) * int(opDer)
        elif(operando == '/'):
            opeNuevo = int(opIzq) / int(opDer)
        elif (operando == '='):
            tablas.checa(opDer)
            tablas.agregarValor(opDer,int(opIzq) )
        print("opeNuevo es: ", opeNuevo)
        self.sTemp.append(opeNuevo)
        self.tablaQ[self.i] = {
            'operando': operando ,
            'opIzq': opIzq, 
            'opDer': opDer, 
            'opNuevo': opeNuevo    
            }
        print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
        self.i += 1


      
    