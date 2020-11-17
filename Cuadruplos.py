#from main import *
from TablaFV  import * 
import TablaFV
from CuboSemantico import *

class  cuad():
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

        

    def agregarTipo(self):
        pass

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
           
        
        #if(isinstance(opIzq, str)):
        #    try:
        #        int(opIzq)
        #        opIzq = int(opIzq)
        #    except:
        #        float(opIzq)
        #        opIzq = float(opIzq)
        #    else:
        #        pass

        #if(isinstance(opDer, str)):
        #    try:
        #        int(opDer)
        #        opDer = int(opDer)
        #    except:
        #        float(opDer)
        #        opDer = float(opDer)

        if(operando == '+'):
            #opeNuevo = opIzq + opDer
            tipoFinal = cubo.cuboS[tipoIzq][tipoDer]['+']
            tablas.agregarC( tablas, 0, tipoFinal)
            opeNuevo = TablaFV.memoriaC - 1

        elif(operando == '-'):
            #opeNuevo = opIzq - opDer
            tipoFinal = cubo.cuboS[tipoIzq][tipoDer]['-']
            tablas.agregarC( tablas, 0, tipoFinal)
            opeNuevo = TablaFV.memoriaC - 1
        elif(operando == '*'):
            #opeNuevo = opIzq * opDer
            tipoFinal = cubo.cuboS[tipoIzq][tipoDer]['*']
            tablas.agregarC( tablas, 0, tipoFinal)
            opeNuevo = TablaFV.memoriaC - 1
        elif(operando == '/'):
            #opeNuevo = opIzq / opDer
            tipoFinal = cubo.cuboS[tipoIzq][tipoDer]['/']
            print("el tipo final es: ",tipoFinal)
            tablas.agregarC( tablas, 0, tipoFinal)
            opeNuevo = TablaFV.memoriaC - 1
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

        print("exp1: ", exp1)
        print("exp2: ", exp2)
        if(isinstance(exp1, str)):
            exp1 = tablas.buscarM(tablas, exp1)

        if(isinstance(exp2, str)):
            exp1 = tablas.buscarM(tablas, exp2)     

        print("new exp1: ", exp1)
        print("new exp2: ", exp2)          

        if(operando == '<'):
            tablas.agregarC( tablas, 0, 'bool')
            opeNuevo = TablaFV.memoriaC - 1
            
            #if(exp1 < exp2):
            #    opeNuevo = 1
            #else:
            #    opeNuevo = 0
        elif(operando == '>'):
            tablas.agregarC( tablas, 0, 'bool')
            opeNuevo = TablaFV.memoriaC - 1
            #if(exp1 > exp2):
            #    opeNuevo = 1
            #else:
            #    opeNuevo = 0
        elif(operando == '<>'):
            tablas.agregarC( tablas, 0, 'bool')
            opeNuevo = TablaFV.memoriaC - 1
            #if(exp1 != exp2):
            #    opeNuevo = 1
            #else:
            #    opeNuevo = 0
        elif(operando == '<='):
            tablas.agregarC( tablas, 0, 'bool')
            opeNuevo = TablaFV.memoriaC - 1
            #if(exp1 <= exp2):
            #    opeNuevo = 1
            #else:
            #    opeNuevo = 0
        elif(operando == '>='):
            tablas.agregarC( tablas, 0, 'bool')
            opeNuevo = TablaFV.memoriaC - 1
            #if(exp1 >= exp2):
            #    opeNuevo = 1
            #else:
            #    opeNuevo = 0
        elif(operando == '=='):
            tablas.agregarC( tablas, 0, 'bool')
            opeNuevo = TablaFV.memoriaC - 1
            #if(exp1 == exp2):
            #    opeNuevo = 1
            #else:
            #    opeNuevo = 0

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
        
        
        



        


      
    