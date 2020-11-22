from TablaFV  import * 
from Cuadruplos  import *

class maquina():
    cuad = cuad()
    tablas = tablas()
    
    tempsMF = {}
    varsMF = {}

    #nota: la tabla de ctes empieza en 0
    #nota: la tabla de funciones empieza en 0
    #nota: la tabla de cuadruplos empieza en 1
    # MV = MAIN VARIABLES
    # MF = MEMORIA FINAL

    def procesos(self):
        i = 1
        operador = 0 
        izq = 0
        der = 0
        res =0 
        #j = 1

        while(i  <= len(cuad.tablaQ )):
            op = cuad.tablaQ[i]['operando']
            izq = cuad.tablaQ[i]['opIzq']
            der = cuad.tablaQ[i]['opDer']
            res = cuad.tablaQ[i]['opNuevo']
            #print("operador: ", op)
            #print("izquierdo: ", izq)
            #print("derecho: ", der)
            #print("res: ",res)

            #if(op == '+'):

            if(op == '+'):
                if( izq >= 5000 and izq < 6000  ):
                    izq = float(tablas.extraerValorC(tablas,izq)) 
                elif(izq >= 9000 and izq < 10000):
                    izq = float(self.tempsMF[izq])
                elif(izq >= 12000 and izq < 13000):
                    izq = float(tablas.extraerValorMV(tablas,izq)) 
                elif( izq >= 6000 and izq < 7000 ):
                    izq = int(tablas.extraerValorC(tablas,izq))
                elif(izq >= 10000 and izq < 11000):
                    izq = int(self.tempsMF[izq])
                elif(izq >= 13000 and izq < 14000):
                    izq = int(tablas.extraerValorMV(tablas,izq))

                if(der >= 5000 and der < 6000 ):
                    der = float(tablas.extraerValorC(tablas,der)) 
                elif(der >= 9000 and der < 10000):
                    der = float(self.tempsMF[der]) 
                elif(der >= 12000 and der < 13000):
                    der = float(tablas.extraerValorMV(tablas,der))
                elif( (der >= 6000 and der < 7000) ):
                    der = int(tablas.extraerValorC(tablas,der))
                elif(der >= 10000 and der < 11000):
                    der = int(self.tempsMF[der]) 
                elif(der >= 13000 and der < 14000):
                    der = int(tablas.extraerValorMV(tablas,der))

                resultado = izq + der
                self.tempsMF[res] = resultado 
                #print(self.tempsMF)
                

            elif(op == '-'):
                if( izq >= 5000 and izq < 6000  ):
                    izq = float(tablas.extraerValorC(tablas,izq)) 
                elif(izq >= 9000 and izq < 10000):
                    izq = float(self.tempsMF[izq])
                elif(izq >= 12000 and izq < 13000):
                    izq = float(tablas.extraerValorMV(tablas,izq)) 
                elif( izq >= 6000 and izq < 7000 ):
                    izq = int(tablas.extraerValorC(tablas,izq))
                elif(izq >= 10000 and izq < 11000):
                    izq = int(self.tempsMF[izq])
                elif(izq >= 13000 and izq < 14000):
                    izq = int(tablas.extraerValorMV(tablas,izq))

                if(der >= 5000 and der < 6000 ):
                    der = float(tablas.extraerValorC(tablas,der)) 
                elif(der >= 9000 and der < 10000):
                    der = float(self.tempsMF[der]) 
                elif(der >= 12000 and der < 13000):
                    der = float(tablas.extraerValorMV(tablas,der))
                elif( (der >= 6000 and der < 7000) ):
                    der = int(tablas.extraerValorC(tablas,der))
                elif(der >= 10000 and der < 11000):
                    der = int(self.tempsMF[der]) 
                elif(der >= 13000 and der < 14000):
                    der = int(tablas.extraerValorMV(tablas,der)) 

                resultado = izq - der
                self.tempsMF[res] = resultado 
                #print(self.tempsMF)

            elif(op == '*'):
                if( izq >= 5000 and izq < 6000  ):
                    izq = float(tablas.extraerValorC(tablas,izq)) 
                elif(izq >= 9000 and izq < 10000):
                    izq = float(self.tempsMF[izq])
                elif(izq >= 12000 and izq < 13000):
                    izq = float(tablas.extraerValorMV(tablas,izq)) 
                elif( izq >= 6000 and izq < 7000 ):
                    izq = int(tablas.extraerValorC(tablas,izq))
                elif(izq >= 10000 and izq < 11000):
                    izq = int(self.tempsMF[izq])
                elif(izq >= 13000 and izq < 14000):
                    izq = int(tablas.extraerValorMV(tablas,izq))

                if(der >= 5000 and der < 6000 ):
                    der = float(tablas.extraerValorC(tablas,der)) 
                elif(der >= 9000 and der < 10000):
                    der = float(self.tempsMF[der]) 
                elif(der >= 12000 and der < 13000):
                    der = float(tablas.extraerValorMV(tablas,der))
                elif( (der >= 6000 and der < 7000) ):
                    der = int(tablas.extraerValorC(tablas,der))
                elif(der >= 10000 and der < 11000):
                    der = int(self.tempsMF[der]) 
                elif(der >= 13000 and der < 14000):
                    der = int(tablas.extraerValorMV(tablas,der))

                resultado = izq * der
                self.tempsMF[res] = resultado 
                #print(self.tempsMF)

            elif(op == '/'):
                if( izq >= 5000 and izq < 6000  ):
                    izq = float(tablas.extraerValorC(tablas,izq)) 
                elif(izq >= 9000 and izq < 10000):
                    izq = float(self.tempsMF[izq])
                elif(izq >= 12000 and izq < 13000):
                    izq = float(tablas.extraerValorMV(tablas,izq)) 
                elif( izq >= 6000 and izq < 7000 ):
                    izq = int(tablas.extraerValorC(tablas,izq))
                elif(izq >= 10000 and izq < 11000):
                    izq = int(self.tempsMF[izq])
                elif(izq >= 13000 and izq < 14000):
                    izq = int(tablas.extraerValorMV(tablas,izq))

                if(der >= 5000 and der < 6000 ):
                    der = float(tablas.extraerValorC(tablas,der)) 
                elif(der >= 9000 and der < 10000):
                    der = float(self.tempsMF[der]) 
                elif(der >= 12000 and der < 13000):
                    der = float(tablas.extraerValorMV(tablas,der))
                elif( (der >= 6000 and der < 7000) ):
                    der = int(tablas.extraerValorC(tablas,der))
                elif(der >= 10000 and der < 11000):
                    der = int(self.tempsMF[der]) 
                elif(der >= 13000 and der < 14000):
                    der = int(tablas.extraerValorMV(tablas,der))

                resultado = izq / der
                self.tempsMF[res] = resultado 
                #print(self.tempsMF)

            elif(op == '='):
                tempM= izq
                if(izq >= 5000 and izq < 9000):
                    izq = tablas.extraerValorC(tablas,izq)
                elif(izq >= 9000 and izq < 12000):
                    izq = self.tempsMF[izq]
                elif(izq >= 12000 and izq < 16000):
                    izq = tablas.extraerValorMV(tablas,izq)
                
                if((res >= 12000 and res < 13000) and ((tempM >= 9000 and tempM < 10000) or (tempM >= 12000 and tempM < 13000)  or (tempM >= 5000 and tempM < 6000) )):# float 
                    tablas.agregarValorMV(tablas, res, izq)
                elif((res >= 13000 and res < 14000) and ((tempM >= 10000 and tempM < 11000) or (tempM >= 13000 and tempM < 14000)  or (tempM >= 60000 and tempM < 7000) )):# int
                    tablas.agregarValorMV(tablas, res, izq)
                elif((res >= 15000 and res < 16000) and ((tempM >= 8000 and tempM < 9000) or (tempM >= 15000 and tempM < 16000)   )):# char
                    tablas.agregarValorMV(tablas, res, izq)
                else:
                    pass
                    #print("tipos incorrectos")
            
            elif(op == '>'):    
                if( izq >= 5000 and izq < 6000  ):
                    izq = float(tablas.extraerValorC(tablas,izq)) 
                elif(izq >= 9000 and izq < 10000):
                    izq = float(self.tempsMF[izq])
                elif(izq >= 12000 and izq < 13000):
                    izq = float(tablas.extraerValorMV(tablas,izq)) 
                elif( izq >= 6000 and izq < 7000 ):
                    izq = int(tablas.extraerValorC(tablas,izq))
                elif(izq >= 10000 and izq < 11000):
                    izq = int(self.tempsMF[izq])
                elif(izq >= 13000 and izq < 14000):
                    izq = int(tablas.extraerValorMV(tablas,izq))

                if(der >= 5000 and der < 6000 ):
                    der = float(tablas.extraerValorC(tablas,der)) 
                elif(der >= 9000 and der < 10000):
                    der = float(self.tempsMF[der]) 
                elif(der >= 12000 and der < 13000):
                    der = float(tablas.extraerValorMV(tablas,der))
                elif( (der >= 6000 and der < 7000) ):
                    der = int(tablas.extraerValorC(tablas,der))
                elif(der >= 10000 and der < 11000):
                    der = int(self.tempsMF[der]) 
                elif(der >= 13000 and der < 14000):
                    der = int(tablas.extraerValorMV(tablas,der))

                if(izq > der):
                    resultado = 1
                else:
                    resultado = 0 
                self.tempsMF[res] = resultado 
                #print(self.tempsMF)

            elif(op == '<'):
                if( izq >= 5000 and izq < 6000  ):
                    izq = float(tablas.extraerValorC(tablas,izq)) 
                elif(izq >= 9000 and izq < 10000):
                    izq = float(self.tempsMF[izq])
                elif(izq >= 12000 and izq < 13000):
                    izq = float(tablas.extraerValorMV(tablas,izq)) 
                elif( izq >= 6000 and izq < 7000 ):
                    izq = int(tablas.extraerValorC(tablas,izq))
                elif(izq >= 10000 and izq < 11000):
                    izq = int(self.tempsMF[izq])
                elif(izq >= 13000 and izq < 14000):
                    izq = int(tablas.extraerValorMV(tablas,izq))

                if(der >= 5000 and der < 6000 ):
                    der = float(tablas.extraerValorC(tablas,der)) 
                elif(der >= 9000 and der < 10000):
                    der = float(self.tempsMF[der]) 
                elif(der >= 12000 and der < 13000):
                    der = float(tablas.extraerValorMV(tablas,der))
                elif( (der >= 6000 and der < 7000) ):
                    der = int(tablas.extraerValorC(tablas,der))
                elif(der >= 10000 and der < 11000):
                    der = int(self.tempsMF[der]) 
                elif(der >= 13000 and der < 14000):
                    der = int(tablas.extraerValorMV(tablas,der))

                if(izq < der):
                    resultado = 1
                else:
                    resultado = 0 
                self.tempsMF[res] = resultado 
                #print(self.tempsMF)
            elif(op == '<>'):
                if( izq >= 5000 and izq < 6000  ):
                    izq = float(tablas.extraerValorC(tablas,izq)) 
                elif(izq >= 9000 and izq < 10000):
                    izq = float(self.tempsMF[izq])
                elif(izq >= 12000 and izq < 13000):
                    izq = float(tablas.extraerValorMV(tablas,izq)) 
                elif( izq >= 6000 and izq < 7000 ):
                    izq = int(tablas.extraerValorC(tablas,izq))
                elif(izq >= 10000 and izq < 11000):
                    izq = int(self.tempsMF[izq])
                elif(izq >= 13000 and izq < 14000):
                    izq = int(tablas.extraerValorMV(tablas,izq))

                if(der >= 5000 and der < 6000 ):
                    der = float(tablas.extraerValorC(tablas,der)) 
                elif(der >= 9000 and der < 10000):
                    der = float(self.tempsMF[der]) 
                elif(der >= 12000 and der < 13000):
                    der = float(tablas.extraerValorMV(tablas,der))
                elif( (der >= 6000 and der < 7000) ):
                    der = int(tablas.extraerValorC(tablas,der))
                elif(der >= 10000 and der < 11000):
                    der = int(self.tempsMF[der]) 
                elif(der >= 13000 and der < 14000):
                    der = int(tablas.extraerValorMV(tablas,der))

                if(izq != der):
                    resultado = 1
                else:
                    resultado = 0 
                self.tempsMF[res] = resultado 
                #print(self.tempsMF)
            elif(op == '>='):
                if( izq >= 5000 and izq < 6000  ):
                    izq = float(tablas.extraerValorC(tablas,izq)) 
                elif(izq >= 9000 and izq < 10000):
                    izq = float(self.tempsMF[izq])
                elif(izq >= 12000 and izq < 13000):
                    izq = float(tablas.extraerValorMV(tablas,izq)) 
                elif( izq >= 6000 and izq < 7000 ):
                    izq = int(tablas.extraerValorC(tablas,izq))
                elif(izq >= 10000 and izq < 11000):
                    izq = int(self.tempsMF[izq])
                elif(izq >= 13000 and izq < 14000):
                    izq = int(tablas.extraerValorMV(tablas,izq))

                if(der >= 5000 and der < 6000 ):
                    der = float(tablas.extraerValorC(tablas,der)) 
                elif(der >= 9000 and der < 10000):
                    der = float(self.tempsMF[der]) 
                elif(der >= 12000 and der < 13000):
                    der = float(tablas.extraerValorMV(tablas,der))
                elif( (der >= 6000 and der < 7000) ):
                    der = int(tablas.extraerValorC(tablas,der))
                elif(der >= 10000 and der < 11000):
                    der = int(self.tempsMF[der]) 
                elif(der >= 13000 and der < 14000):
                    der = int(tablas.extraerValorMV(tablas,der))

                if(izq >= der):
                    resultado = 1
                else:
                    resultado = 0 
                self.tempsMF[res] = resultado 
                #print(self.tempsMF)
            elif(op == '<='):
                if( izq >= 5000 and izq < 6000  ):
                    izq = float(tablas.extraerValorC(tablas,izq)) 
                elif(izq >= 9000 and izq < 10000):
                    izq = float(self.tempsMF[izq])
                elif(izq >= 12000 and izq < 13000):
                    izq = float(tablas.extraerValorMV(tablas,izq)) 
                elif( izq >= 6000 and izq < 7000 ):
                    izq = int(tablas.extraerValorC(tablas,izq))
                elif(izq >= 10000 and izq < 11000):
                    izq = int(self.tempsMF[izq])
                elif(izq >= 13000 and izq < 14000):
                    izq = int(tablas.extraerValorMV(tablas,izq))

                if(der >= 5000 and der < 6000 ):
                    der = float(tablas.extraerValorC(tablas,der)) 
                elif(der >= 9000 and der < 10000):
                    der = float(self.tempsMF[der]) 
                elif(der >= 12000 and der < 13000):
                    der = float(tablas.extraerValorMV(tablas,der))
                elif( (der >= 6000 and der < 7000) ):
                    der = int(tablas.extraerValorC(tablas,der))
                elif(der >= 10000 and der < 11000):
                    der = int(self.tempsMF[der]) 
                elif(der >= 13000 and der < 14000):
                    der = int(tablas.extraerValorMV(tablas,der))

                if(izq <= der):
                    resultado = 1
                else:
                    resultado = 0 
                self.tempsMF[res] = resultado 
                #print(self.tempsMF)

            elif(op == '=='):
                if( izq >= 5000 and izq < 6000  ):
                    izq = float(tablas.extraerValorC(tablas,izq)) 
                elif(izq >= 9000 and izq < 10000):
                    izq = float(self.tempsMF[izq])
                elif(izq >= 12000 and izq < 13000):
                    izq = float(tablas.extraerValorMV(tablas,izq)) 
                elif( izq >= 6000 and izq < 7000 ):
                    izq = int(tablas.extraerValorC(tablas,izq))
                elif(izq >= 10000 and izq < 11000):
                    izq = int(self.tempsMF[izq])
                elif(izq >= 13000 and izq < 14000):
                    izq = int(tablas.extraerValorMV(tablas,izq))

                if(der >= 5000 and der < 6000 ):
                    der = float(tablas.extraerValorC(tablas,der)) 
                elif(der >= 9000 and der < 10000):
                    der = float(self.tempsMF[der]) 
                elif(der >= 12000 and der < 13000):
                    der = float(tablas.extraerValorMV(tablas,der))
                elif( (der >= 6000 and der < 7000) ):
                    der = int(tablas.extraerValorC(tablas,der))
                elif(der >= 10000 and der < 11000):
                    der = int(self.tempsMF[der]) 
                elif(der >= 13000 and der < 14000):
                    der = int(tablas.extraerValorMV(tablas,der))

                if(izq == der):
                    resultado = 1
                else:
                    resultado = 0 
                self.tempsMF[res] = resultado 
                #print(self.tempsMF)

            elif(op == 'write'):
                if((res >= 5000 and res < 9000) or (res >= 16000 and res < 17000)):
                    print(tablas.extraerValorC(tablas,res))
                elif(res >= 9000 and res < 12000):
                    print(self.tempsMF[res])
                elif(res >= 12000 and res < 16000):
                    print(tablas.extraerValorMV(tablas,res))# MV = MAIN VARIABLES
            
            elif(op == 'gotoT'):
                i = res -1
            elif(op == 'gotoFF'):
                i = res -1

            elif(op == 'gotoTF'):
                if(self.tempsMF[izq] == 1):
                    i = int(res) -1

            elif(op == 'gotoF'):
                #print("este es el derecho",self.tempsMF[izq])
                if(self.tempsMF[izq] == 0):
                    i = int(res) -1
                
                #break
            i +=1    

        print(tablas.tablaMV)






