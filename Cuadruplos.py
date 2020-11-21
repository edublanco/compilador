#from main import *
from TablaFV  import * 
import TablaFV
from CuboSemantico import *


class  cuad():

    fResult = 9000
    iResult = 10000
    bResult = 11000
    cResult = 12000
    tempType =''

    tablaQ = {}
    i = 1 
    sOperadores = []
    sTemp = []
    sTipo = []

    variable = ''
    fin = False
    tablas=tablas()
    cubo = cubo()

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

    def agregarCuad(self, opIzq, opDer, operando):  
        opeNuevo = 0
        tipoFinal = ''

        if(isinstance(opIzq, str)):
            opIzq = tablas.buscarM(tablas, opIzq)
            tipoIzq = tablas.buscarTypeV(tablas, opIzq)
        else:   
            tipoIzq = tablas.buscarTypeC(tablas, opIzq)

        if(isinstance(opDer, str)):
            opDer = tablas.buscarM(tablas, opDer)
            tipoDer = tablas.buscarTypeV(tablas, opDer)
        else:
            tipoDer = tablas.buscarTypeC(tablas, opDer)
        
        if(tipoDer == ''):
            tipoDer = self.tempType

        if(tipoIzq == ''):
            tipoIzq = self.tempType

        if(operando == '+'):
            tipoFinal = cubo.cuboS[tipoIzq][tipoDer]['+']
            #tablas.agregarC( tablas, 0, tipoFinal)
            if(tipoFinal == 'int'):
                self.iResult += 1
                opeNuevo = self.iResult
                self.tempType = 'int'
            elif(tipoFinal =='float'):
                self.fResult += 1
                opeNuevo = self.fResult
                self.tempType = 'float'

        elif(operando == '-'):
            tipoFinal = cubo.cuboS[tipoIzq][tipoDer]['-']
            #tablas.agregarC( tablas, 0, tipoFinal)
            if(tipoFinal == 'int'):
                self.iResult += 1
                opeNuevo = self.iResult
                self.tempType = 'int'
            elif(tipoFinal =='float'):
                self.fResult += 1
                opeNuevo = self.fResult
                self.tempType = 'float'

        elif(operando == '*'):
            tipoFinal = cubo.cuboS[tipoIzq][tipoDer]['*']
            #tablas.agregarC( tablas, 0, tipoFinal)
            if(tipoFinal == 'int'):
                self.iResult += 1
                opeNuevo = self.iResult
                self.tempType = 'int'
            elif(tipoFinal =='float'):
                self.fResult += 1
                opeNuevo = self.fResult
                self.tempType = 'float'

        elif(operando == '/'):
            tipoFinal = cubo.cuboS[tipoIzq][tipoDer]['/']
            tablas.agregarC( tablas, 0, tipoFinal)
            if(tipoFinal == 'int'):
                self.iResult += 1
                opeNuevo = self.iResult
                self.tempType = 'int'
            elif(tipoFinal =='float'):
                self.fResult += 1
                opeNuevo = self.fResult
                self.tempType = 'float'

        
        elif (operando == 'end'):
            opeNuevo = opDer


        if(TablaFV.scope != "global" and tipoFinal == 'int' ):
            tablas.tablaEra[TablaFV.scope][10000] +=1
        elif(TablaFV.scope != "global" and tipoFinal == 'float' ):
            tablas.tablaEra[TablaFV.scope][9000] +=1
        
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


    def agregarCuadAsign(self, opIzq, opDer, operando):
        opeNuevo = opIzq
        opIzq =  opDer
        #opeNuevo = opDer
        opDer = 0  

        self.tablaQ[self.i] = {
            'operando': operando ,
            'opIzq': opIzq, 
            'opDer': opDer, 
            'opNuevo': opeNuevo    
            }
        self.resultado = opeNuevo
        print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
        self.i += 1

    def agregarCuadF0(self,  funcion):
        opeNuevo = 0
        opeNuevo = exp

        self.tablaQ[self.i] = {
            'operando': funcion ,
            'opIzq': 0, 
            'opDer': 0, 
            'opNuevo': 0 
            }

        self.resultado = opeNuevo
        print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
        self.i += 1

    def agregarCuadF1(self, exp, funcion):
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

    def agregarCuadF2(self, exp1, exp2, funcion):
        opeNuevo = 0
        opeNuevo = exp2

        self.tablaQ[self.i] = {
            'operando': funcion ,
            'opIzq': 0, 
            'opDer': exp1, 
            'opNuevo': exp2    
            }

        self.resultado = opeNuevo
        print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
        self.i += 1

    
    def agregarCuadExpresion(self, exp1,exp2, operando):
        opeNuevo = 0

        print("exp1: ", exp1)
        print("exp2: ", exp2)
        if(isinstance(exp1, str)):
            exp1 = tablas.buscarM(tablas, exp1)

        if(isinstance(exp2, str)):
            exp1 = tablas.buscarM(tablas, exp2)     

        print("new exp1: ", exp1)
        print("new exp2: ", exp2)          

        if(operando == '<'):
            self.bResult += 1
            opeNuevo = self.bResult
            if(TablaFV.scope != "global"):
                tablas.tablaEra[TablaFV.scope][11000] +=1

        elif(operando == '>'):
            sself.bResult += 1
            opeNuevo = self.bResult
            if(TablaFV.scope != "global"):
                tablas.tablaEra[TablaFV.scope][11000] +=1
   
        elif(operando == '<>'):
            self.bResult += 1
            opeNuevo = self.bResult
            if(TablaFV.scope != "global"):
                tablas.tablaEra[TablaFV.scope][11000] +=1

        elif(operando == '<='):
            self.bResult += 1
            opeNuevo = self.bResult
            if(TablaFV.scope != "global"):
                tablas.tablaEra[TablaFV.scope][11000] +=1
  
        elif(operando == '>='):
            self.bResult += 1
            opeNuevo = self.bResult
            if(TablaFV.scope != "global"):
                tablas.tablaEra[TablaFV.scope][11000] +=1
          
        elif(operando == '=='):
            self.bResult += 1
            opeNuevo = self.bResult
            if(TablaFV.scope != "global"):
                tablas.tablaEra[TablaFV.scope][11000] +=1


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
            'opIzq': self.resultado, 
            'opDer': 0, 
            'opNuevo': 0    
            }
            self.sJumps.append(self.i)
            print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
            self.i += 1
        
  
        elif(operando == 'gotoFC'):
            dire = self.sJumps.pop()
            self.tablaQ[dire]['opNuevo'] = self.i  #+1
            pass
        
        elif(operando == 'gotoFC2'):
            dire = self.sJumps.pop()
            self.tablaQ[dire]['opNuevo'] = self.i  +1 #+2
            pass

        elif(operando == 'gotoT'):
            self.tablaQ[self.i] = {
            'operando': goto ,
            'opIzq': 0, 
            'opDer': 0, 
            'opNuevo': 0    
            }

            self.sJumps.append(self.i)
            print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
            self.i += 1
        
        elif(operando == 'gotoTC'):
            dire = self.sJumps.pop()
            self.tablaQ[dire]['opNuevo'] = self.i  #+ 1
            pass
        

    def agregarCuadWhile(self,  goto):
        operando = goto
        
        if(operando == 'gotoF'):
            self.tablaQ[self.i] = {
            'operando': goto ,
            'opIzq': self.resultado, 
            'opDer': 0, 
            'opNuevo': 0    
            }
            self.sJumps.append(self.i)
            print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
            self.i += 1
    
        elif(operando == 'gotoFC'):
            dire = self.sJumps.pop()
            self.tablaQ[dire]['opNuevo'] = self.i +1
            pass

        elif(operando == 'gotoT'):
            self.tablaQ[self.i] = {
            'operando': goto ,
            'opIzq': 0, 
            'opDer': 0, 
            'opNuevo': self.sJumps.pop()    
            }
            print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
            self.i += 1
        
        elif(operando == 'gotoTC'):
            print("slef i en gotoc del while: ",self.i)  
            self.sJumps.append(self.i)
            pass

    def agregarCuadFor(self,  goto):
        operando = goto
        
        if(operando == 'gotoF'):
            self.tablaQ[self.i] = {
            'operando': goto ,
            'opIzq': 0, 
            'opDer': 0, 
            'opNuevo': self.sJumps.pop()    
            }
            print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
            self.i += 1
        elif(operando == 'gotoFC'):
            print("slef i en gotoc del for: ",self.i)  
            self.sJumps.append(self.i)
            pass
        elif(operando == 'gotoT'):
            self.tablaQ[self.i] = {
            'operando': goto ,
            'opIzq': self.resultado, 
            'opDer': 0, 
            'opNuevo': 0    
            }
            self.sJumps.append(self.i)
            print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
            self.i += 1
        
        elif(operando == 'gotoTC'):
            dire = self.sJumps.pop()
            self.tablaQ[dire]['opNuevo'] = self.i +1
            pass
        
    def agregarCuadMain(self,  goto):
        operando = goto

        if(operando == 'gotoT'):
            self.tablaQ[self.i] = {
            'operando': goto ,
            'opIzq': self.resultado, 
            'opDer': 0, 
            'opNuevo': 0    
            }
            self.sJumps.append(self.i)
            print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
            self.i += 1
        
        elif(operando == 'end'):
            self.tablaQ[self.i] = {
            'operando': goto ,
            'opIzq': 0, 
            'opDer': 0, 
            'opNuevo': 0    
            }
            print("prueba de tipos:")
            i = cubo.cuboS['int']['float']['*']
            print("prueba de tipos es:", i)
            self.sJumps.append(self.i)
            print("tablaQ[",self.i,"]: ",self.tablaQ[self.i])
            self.i += 1

        elif(operando == 'gotoTC'):
            dire = self.sJumps.pop()
            self.tablaQ[dire]['opNuevo'] = self.i  #+1
            pass

    def agregarCuadCall(self,  goto, nombre, valor):
        operando = goto
   

        if(operando == 'era'):
            self.tablaQ[self.i] = {
            'operando': goto ,
            'opIzq': nombre, 
            'opDer': 0, 
            'opNuevo': 0    
            }
            self.i += 1
        
  
        elif(operando == 'return'):
            self.tablaQ[self.i] = {
            'operando': goto ,
            'opIzq': 0, 
            'opDer': 0, 
            'opNuevo': valor    
            }
            self.i += 1
        
        elif(operando == 'param'):
            #tablas.agregarV(p.ID,self.auxTipo, 0)
            
            self.tablaQ[self.i] = {
            'operando': goto ,
            'opIzq': valor, 
            'opDer': 0, 
            'opNuevo': 'param' + str(nombre)  
            }
            self.i += 1
        elif(operando == 'gosub'):
            #tablas.agregarV(p.ID,self.auxTipo, 0)
            self.tablaQ[self.i] = {
            'operando': goto ,
            'opIzq': nombre, 
            'opDer': 0, 
            'opNuevo': 0
            }
            self.i += 1
        
        
        



        


      
    