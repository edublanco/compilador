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
            
        opeNuevo = 0
        if(isinstance(opIzq, str)):
            try:
                int(opIzq)
                opIzq = int(opIzq)
            except:
                float(opIzq)
                opIzq = float(opIzq)
            else:
                pass

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
            #print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
            #print("resultado: ", opeNuevo)
            #print("tabla operadores final",self.sOperadores)
            #print("tabla temporales final",self.sTemp)
            #self.i = 1
            #self.tablaQ.clear()

    def agregarCuadAsign(self, opIzq, opDer, operando):
        opeNuevo = 0
        opeNuevo = opDer

        self.tablaQ[self.i] = {
            'operando': operando ,
            'opIzq': opIzq, 
            'opDer': opDer, 
            'opNuevo': opeNuevo    
            }

    
        self.resultado = opeNuevo
        print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
        self.i += 1

    def agregarCuadF(self, exp, funcion):
        opeNuevo = 0
        opeNuevo = exp

        self.tablaQ[self.i] = {
            'operando': funcion ,
            'opIzq': 0, 
            'opDer': 0, 
            'opNuevo': exp    
            }

    
        self.resultado = opeNuevo
        print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
        self.i += 1
       
    def agregarCuadExpresion(self, exp1,exp2, operando):
        opeNuevo = 0
        #opeNuevo = exp

        if(operando == '<'):
            if(exp1 < exp2):
                opeNuevo = 1
            else:
                opeNuevo = 0
        elif(operando == '>'):
            if(exp1 > exp2):
                opeNuevo = 1
            else:
                opeNuevo = 0
        elif(operando == '<>'):
            if(exp1 != exp2):
                opeNuevo = 1
            else:
                opeNuevo = 0
        elif(operando == '<='):
            if(exp1 <= exp2):
                opeNuevo = 1
            else:
                opeNuevo = 0
        elif(operando == '>='):
            if(exp1 >= exp2):
                opeNuevo = 1
            else:
                opeNuevo = 0
        elif(operando == '=='):
            if(exp1 == exp2):
                opeNuevo = 1
            else:
                opeNuevo = 0

        self.tablaQ[self.i] = {
            'operando': operando,
            'opIzq': exp1, 
            'opDer': exp2, 
            'opNuevo': opeNuevo    
            }

    
        self.resultado = opeNuevo
        print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
        self.i += 1

    sJumps = []
    dire = 0
    def agregarCuadIf(self,  goto):
        operando = goto
        
        if(operando == 'gotoF'):
            self.tablaQ[self.i] = {
            'operando': goto ,
            'opIzq': 0, 
            'opDer': 0, 
            'opNuevo': 0    
            }
            self.sJumps.append(self.i)
            print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
            self.i += 1
        
  
        elif(operando == 'gotoFC'):
            dire = self.sJumps.pop()
            self.tablaQ[dire]['opNuevo'] = self.i  +1
            pass
        
        elif(operando == 'gotoFC2'):
            dire = self.sJumps.pop()
            self.tablaQ[dire]['opNuevo'] = self.i  +2
            pass

        elif(operando == 'gotoT'):
            self.tablaQ[self.i] = {
            'operando': goto ,
            'opIzq': 0, 
            'opDer': 0, 
            'opNuevo': 0    
            }
            #false = self.sIfs.pop
            #false = self.sIf.pop()
            self.sJumps.append(self.i)
            #self.tablaQ[false]['opNuevo'] = self.i 
           
            print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
            self.i += 1
        
        elif(operando == 'gotoTC'):
            dire = self.sJumps.pop()
            self.tablaQ[dire]['opNuevo'] = self.i  + 1
            pass
        
        
        



        


      
    