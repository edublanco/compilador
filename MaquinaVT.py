from TablaFV  import * 
from Cuadruplos  import *
from turtle import *
class maquina():
    cuad = cuad()
    tablas = tablas()
    direcCall = []
    tempsMF = {}
    varsMF = {}
    varLocales = {}
    tempsLocales = {}
    dirArr = {}
    isFun = False
    par = 1


    #nota: la tabla de ctes empieza en 0
    #nota: la tabla de funciones empieza en 0
    #nota: la tabla de cuadruplos empieza en 1
    # MV = MAIN VARIABLES
    # MF = MEMORIA FINAL

    def iof(self, valor):
        

        if( valor >= 5000 and valor < 6000  ):
            valor = float(tablas.extraerValorC(tablas,valor)) 
        elif(valor >= 9000 and valor < 10000):
            if(self.isFun):
                valor = float(self.tempsLocales[valor])
            else:
                valor = float(self.tempsMF[valor]) 
        elif(valor >= 12000 and valor < 13000):
            
            valor = float(tablas.extraerValorMV(tablas,valor)) 
        elif( valor >= 6000 and valor < 7000 ):
            valorAux =  valor
            valor = tablas.extraerValorC(tablas,valor)
            
            if(valor[0:4] == 'arr-'):
                valor =  int(self.dirArr[valor])
                print("---- antes el valor de dirArr es:", valor)
                valor = self.iof(valor)
                print("---- despues  el valor de dirArr es:", valor)
            else:
                valor = valorAux
                valor = int(tablas.extraerValorC(tablas,valor))
        elif(valor >= 1000 and valor < 2000):
            w = 1
            while(w <= len(self.varLocales)):
                if (self.varLocales[w]['memoria'] == valor):
                    valor = self.varLocales[w]['valor']
                w +=1
            valor = float(valor)
        elif(valor >= 10000 and valor < 11000):
            if(self.isFun): #----------------------------------OJO
                try:
                    valor = int(self.tempsLocales[valor])
                except:
                    valor = int(self.tempsMF[valor]) 

            else:
                valor = int(self.tempsMF[valor]) 
        elif(valor >= 13000 and valor < 14000):
            valor = int(tablas.extraerValorMV(tablas,valor))
        elif(valor >= 2000 and valor < 3000):
            w = 1
            print("entre al 2000", valor)
            while(w <= len(self.varLocales)):
                if (self.varLocales[w]['memoria'] == valor):
                    valor = self.varLocales[w]['valor']
                    print("entre al if del 2000", valor)
                w +=1
            valor = int(valor)
        elif(valor[0:4] == 'arr-'):
            valor =  int(self.dirArr[valor])
            print("---- el valor de dirArr es:", valor)
        else:
            print("---- el valor[4] es:", valor[0:4])
        return valor


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
                izq = self.iof(izq)
                der = self.iof(der)

                resultado = izq + der
                if(self.isFun):
                    print("izq:",izq)
                    print("der:", der)
                    self.tempsLocales[res] = resultado 
                    print("el resultado de temps locales:", self.tempsLocales)
                    print("el resultado de var locales:", self.varLocales)
                else:
                    self.tempsMF[res] = resultado 
        
            elif(op == '-'):
                izq = self.iof(izq)
                der = self.iof(der)

                resultado = izq - der

                
                if(self.isFun):
                    self.tempsLocales[res] = resultado 
                else:
                    self.tempsMF[res] = resultado 

                #print(self.tempsMF)

            elif(op == '*'):
                izq = self.iof(izq)
                der = self.iof(der)

                resultado = izq * der

                if(self.isFun):
                    self.tempsLocales[res] = resultado 
                else:
                    self.tempsMF[res] = resultado 


            elif(op == '/'):
                izq = self.iof(izq)
                der = self.iof(izq)
                resultado = izq / der
                
                if(self.isFun):
                    self.tempsLocales[res] = resultado 
                else:
                    self.tempsMF[res] = resultado 

            elif(op == '='):
                tempM = izq
                #convertir res string y checar si es string
                if (isinstance(res, str)) :
                    if(res[0:4] == 'arr-'):
                        res =  int(self.dirArr[res])
                        print("---- el res de dirArr es:", res)
                        print("---- el izq de dirArr es:", izq)
                        
                if (isinstance(izq, str)) :
                    if(res[0:4] == 'arr-'):
                        res =  int(self.dirArr[res])
                        print("---- antes el res de dirArr es:", res)
                        print("---- despues  el res de dirArr es:", res)
                #aqui extraemos el valor
                if(izq >= 5000 and izq < 9000):
                    izq = tablas.extraerValorC(tablas,izq)
                elif(izq >= 9000 and izq < 12000):
                    if(self.isFun):
                        izq = int(self.tempsLocales[izq])
                    else:
                        izq = int(self.tempsMF[izq]) 
                elif(izq >= 12000 and izq < 16000):
                    izq = tablas.extraerValorMV(tablas,izq)
                elif(izq >= 1000 and izq < 5000):
                    w = 1

                    while(w <= len(self.varLocales)):
                        if (self.varLocales[w]['memoria'] == izq):
                            izq = self.varLocales[w]['valor']
                        w +=1
                   
                
                if((res >= 12000 and res < 13000) and ((tempM >= 9000 and tempM < 10000) or (tempM >= 12000 and tempM < 13000)  or (tempM >= 5000 and tempM < 6000) )):# float 
                    tablas.agregarValorMV(tablas, res, izq)
                elif((res >= 13000 and res < 14000) and ((tempM >= 10000 and tempM < 11000) or (tempM >= 13000 and tempM < 14000)  or (tempM >= 6000 and tempM < 7000) )):# int
                    tablas.agregarValorMV(tablas, res, izq)
                elif((res >= 15000 and res < 16000) and ((tempM >= 8000 and tempM < 9000) or (tempM >= 15000 and tempM < 16000)   )):# char
                    tablas.agregarValorMV(tablas, res, izq)
                # para las vars locales
                elif((res >= 1000 and res < 2000) and ((tempM >= 1000 and tempM < 2000)or (tempM >= 9000 and tempM < 10000) or (tempM >= 12000 and tempM < 13000)  or (tempM >= 5000 and tempM < 6000) )):# float 
                  
                    w = 1
                    while(w <= len(self.varLocales)):
                        if (self.varLocales[w]['memoria'] == res):
                            self.varLocales[w]['valor'] = izq
                        w +=1
                    
                elif((res >= 2000 and res < 3000) and ((tempM >= 2000 and tempM < 3000)or(tempM >= 10000 and tempM < 11000) or (tempM >= 13000 and tempM < 14000)  or (tempM >= 6000 and tempM < 7000) )):# int
                    w = 1
                    while(w <= len(self.varLocales)):
                        if (self.varLocales[w]['memoria'] == res):
                            self.varLocales[w]['valor'] = izq
                        w +=1
                elif((res >= 4000 and res < 5000) and ((tempM >= 4000 and tempM < 5000)or(tempM >= 8000 and tempM < 9000) or (tempM >= 15000 and tempM < 16000)   )):# char
                    w = 1
                    while(w <= len(self.varLocales)):
                        if (self.varLocales[w]['memoria'] == res):
                            self.varLocales[w]['valor'] = izq
                        w +=1
                
                else:
                    print("tipos incorrectos")
                    print("res:" , res)
                    print("temp:" , tempM)
                #---------- cambio nuevo
                #if(self.isFun):
                #    self.tempsLocales[res] = resultado 
                #else:
                #    self.tempsMF[res] = resultado  
            
            elif(op == '>'):    
                izq = self.iof(izq)
                der = self.iof(der)
                if(izq > der):
                    resultado = 1
                else:
                    resultado = 0 

                if(self.isFun):
                    self.tempsLocales[res] = resultado 
                else:
                    self.tempsMF[res] = resultado 

                #print(self.tempsMF)

            elif(op == '<'):
                izq = self.iof(izq)
                der = self.iof(der)

                if(izq < der):
                    resultado = 1
                else:
                    resultado = 0 

                if(self.isFun):
                    self.tempsLocales[res] = resultado 
                else:
                    self.tempsMF[res] = resultado 
                
                #print(self.tempsMF)
            elif(op == '<>'):
                izq = self.iof(izq)
                der = self.iof(der)

                if(izq != der):
                    resultado = 1
                else:
                    resultado = 0 

                if(self.isFun):
                    self.tempsLocales[res] = resultado 
                else:
                    self.tempsMF[res] = resultado 
               
                #print(self.tempsMF)
            elif(op == '>='):
                izq = self.iof(izq)
                der = self.iof(der)

                if(izq >= der):
                    resultado = 1
                else:
                    resultado = 0

                if(self.isFun):
                    self.tempsLocales[res] = resultado 
                else:
                    self.tempsMF[res] = resultado 
               
            
                #print(self.tempsMF)
            elif(op == '<='):
                izq = self.iof(izq)
                der = self.iof(der)

                if(izq <= der):
                    resultado = 1
                else:
                    resultado = 0

                if(self.isFun):
                    self.tempsLocales[res] = resultado 
                else:
                    self.tempsMF[res] = resultado 

            elif(op == '=='):
                izq = self.iof(izq)
                der = self.iof(der)

                if(izq == der):
                    resultado = 1
                else:
                    resultado = 0

                if(self.isFun):
                    self.tempsLocales[res] = resultado 
                else:
                    self.tempsMF[res] = resultado 

            elif(op == 'write'):


                if((res >= 5000 and res < 9000) or (res >= 16000 and res < 17000)):
                    print("---- res en write es:", res)
                    auxRes = res

                    res = tablas.extraerValorC(tablas,res)
                    if(isinstance(res,str)):
                        
                        if(res[0:4] == 'arr-'):
                            res =  int(self.dirArr[res])
                            print(tablas.extraerValorMV(tablas,res))
                        else:
                            res = auxRes
                            print(tablas.extraerValorC(tablas,res))    
                    else:
                        res = auxRes
                        print(tablas.extraerValorC(tablas,res))
        
                elif(res >= 9000 and res < 12000):
                    if(self.isFun):
                        print(self.tempsLocales[res])
                    else:
                        print(self.tempsMF[res]) 
                    #print(self.tempsMF[res])
                elif(res >= 12000 and res < 16000):
                    print(tablas.extraerValorMV(tablas,res))# MV = MAIN VARIABLES
                elif(res >= 1000 and res <  5000):
                    w = 1
                    while(w <= len(self.varLocales)):
                        if (self.varLocales[w]['memoria'] == res):
                            res = self.varLocales[w]['valor']
                        w +=1
                    print(res)
            
            #elif(op == 'era'):
            elif(op =='era'):

                
                self.isFun = True
                floats = tablas.tablaEra[izq][1000] 
                ints = tablas.tablaEra[izq][2000] 
                bools = tablas.tablaEra[izq][3000] 
                chars = tablas.tablaEra[izq][4000] 
                fl = 1
                it = 1
                bl =1 
                ch =1


                j = tablas.tablaEra[izq][1000] + tablas.tablaEra[izq][2000] + tablas.tablaEra[izq][3000] +tablas.tablaEra[izq][4000] 
                w = 1

                while(w <= j):
                    self.varLocales[w] = {
                        'nombre':0,
                        'memoria':0,
                        'valor':0,
                        'scope': izq
                    }
                    if(fl <= floats):
                        self.varLocales[w]['memoria'] = 1000 + fl
                        fl +=1
                    elif(it <= ints):
                        self.varLocales[w]['memoria'] = 2000 + it
                        it  += 1
                    elif(bl <= bools):
                        self.varLocales[w]['memoria'] = 3000 + bl
                        bl += 1
                    elif(ch <= chars):
                        self.varLocales[w]['memoria'] = 4000 + ch
                        ch +=1
                    w += 1
              

            
                #print( self.varLocales)

            elif(op == 'gosub'):
                self.direcCall.append(i)
                #self.isFun = False
                i = res -1
            elif(op == 'return'):
                i = self.direcCall.pop()
                self.isFun = False
             

                #--------------------------------
                funcion = tablas.buscarM(tablas,self.varLocales[1]['scope'])  
                
                if(funcion == ''): # para los casos void
                    funcion =0
                tempM = res
            
                if(res >= 5000 and res < 9000):
                    res = tablas.extraerValorC(tablas,res)
                elif(izq >= 9000 and res < 12000):
                    if(self.isFun):
                        res = int(self.tempsLocales[res])
                    else:
                        res = int(self.tempsMF[res]) 
                elif(res >= 12000 and res < 16000):
                    res = tablas.extraerValorMV(tablas,res)
                elif(res >= 1000 and res < 5000):
                    w = 1
                    while(w <= len(self.varLocales)):
                        if (self.varLocales[w]['memoria'] == res):
                            res = self.varLocales[w]['valor']
                        w +=1
                #-----------------------------------------------------
                print("la funcion es:", funcion)
                print("tempM es: ", tempM)
                if((funcion >= 12000 and funcion < 13000) and ((tempM >= 1000 and tempM < 2000) or(tempM >= 9000 and tempM < 10000) or (tempM >= 12000 and tempM < 13000)  or (tempM >= 5000 and tempM < 6000) )):# float 
                    tablas.agregarValorMV(tablas, funcion, res)
                elif((funcion >= 13000 and funcion < 14000) and ((tempM >= 2000 and tempM < 3000) or(tempM >= 10000 and tempM < 11000) or (tempM >= 13000 and tempM < 14000)  or (tempM >= 6000 and tempM < 7000) )):# int
                    tablas.agregarValorMV(tablas, funcion, res)
                #-----------------------------------------------------
                print(self.varLocales)
                self.varLocales = {}
                self.par =1
              
                # asiganr bien el valordel return

            elif(op == 'param'):
                izq = self.iof(izq)
                 
                self.varLocales[self.par]['valor'] = izq
                self.par += 1
                pass

            elif(op == 'ver'):
                izq = self.iof(izq)
                if(izq > res):
                    print("ERROR: El valor se sale de rango")
                    break

            elif(op == '++'):
                der = self.iof(der)
                self.dirArr[res] = int(izq) + der
                print("------------------------")
                print(self.dirArr[res])
                print("------------------------")

            elif(op == 'gotoT'):
                i = res -1

            elif(op == 'gotoFF'):
                i = res -1

            elif(op == 'gotoTF'):
                if(self.isFun):
                    if(self.tempsLocales[izq] == 1):
                        i = int(res) -1

                elif(self.tempsMF[izq] == 1):
                    i = int(res) -1
                #if(self.tempsMF[izq] == 1):
                #    i = int(res) -1
                
            elif(op == 'gotoF'):
                if(self.isFun):
                    if(self.tempsLocales[izq] == 0):
                        i = int(res) -1
                
                elif(self.tempsMF[izq] == 0):
                    i = int(res) -1
                #break
               

            elif(op == 'size'):
                res = self.iof(res)
                pensize(res)
                pass

            elif(op == 'color'):
                color(res)
                

            elif(op == 'clear'):
                clear()
                pass
            elif(op == 'pendown'):
                pendown()
                pass

            elif(op == 'penup'):
                penup()
                pass

            elif(op == 'done'):
                Screen().exitonclick()
                pass
            
            elif(op == 'speed'):
                res = self.iof(res)
                speed(res)
                pass
            
            elif(op == 'arc'):
                res = self.iof(res)
                #der = self.iof(der)
                circle(res, 180)
                pass
            
            elif(op == 'circle'):
                res = self.iof(res)
                circle(res)
                pass
            
            elif(op == 'point'):
                res = self.iof(res)
                dot(res)
                pass

            elif(op == 'line'):
                
                res = self.iof(res)
                der = self.iof(der)
                setpos(der,res)
                pass

            elif(op == 'read'):
                r =input()
                tablas.agregarC(tablas,r, 'string')
          
                pass
            i +=1 
        print(tablas.tablaMV)
       






