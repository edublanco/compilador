from sly import Lexer, Parser
from collections import defaultdict
from TablaFV  import * 
from Cuadruplos  import *
from CuboSemantico import cubo
from MaquinaVT  import *

class CalcLexer(Lexer):
    # Set of token names.   This is always required
    tokens = {  CTEI, CTEF,  ID, CSTRING, MAS, MENOS, INT, 
                ASIGNACION, IF, ELSE,
                RELOP, MUL, DIV, PROGRAMA,
                CHAR, FLOAT, VAR,
                MODULE, VOID, RETURN, PALETA,FOR, WHILE,
                MAIN, TO, DO, WRITE, READ, SIZE, COLOR, CLEAR,
                PENDOWN, PENUP, ARC, CIRCLE, POINT, LINE, THEN, LETRA}

    ignore =' \t'

    literals = { ';', ':', '(', ')', '{', '}',','}

    CTEF    = r'([0-9]+)(\.)([0-9]+)?'
    CTEI    = r'[0-9]+'
    ID      = r'[a-zA-Z]([a-zA-Z]|[0-9_])*'
    CSTRING = r'\".*?\"'
    LETRA  = r'\'[a-zA-Z]\''
    MENOS   = r'[\-]'
    MAS     = r'[\+]'
    MUL     = r'[\*]'
    DIV     = r'[\/]'
    RELOP   = r'(<>)|(==)|(<=)|(>=)|(<)|(>)'
    ASIGNACION  = r'='

    ID['if'] = IF
    ID['else'] = ELSE
    ID['int'] = INT
    ID['float'] = FLOAT
    ID['programa'] = PROGRAMA
    ID['char'] = CHAR
    ID['var'] = VAR
    ID['module'] = MODULE
    ID['void'] = VOID
    ID['return'] = RETURN
    ID['red'] = PALETA
    ID['blue'] = PALETA
    ID['green'] = PALETA
    ID['pink'] = PALETA
    ID['yellow'] = PALETA
    ID['main'] = MAIN
    ID['to'] = TO
    ID['do'] = DO
    ID['write'] = WRITE
    ID['read'] = READ
    ID['size'] = SIZE
    ID['color'] = COLOR
    ID['clear'] = CLEAR
    ID['pendown'] = PENDOWN
    ID['penup'] = PENUP
    ID['arc'] = ARC
    ID['circle'] = CIRCLE
    ID['point'] = POINT
    ID['line'] = LINE
    ID['then'] = THEN
    ID['for'] = FOR
    ID['while'] = WHILE
 
    
class CalcParser(Parser):
    # Get the token list from the lexer (required)
    tokens = CalcLexer.tokens
    aux = 0 
    cuad = cuad()
    #tablaEra{}

    def __init__(self):
        self.names = { }
    
    #Programa -----------------------------------------------------
    @_('PROGRAMA pnp ID ":"  programa2')
    def programa(self, p):
        tablas.agregarMV()
        pass

    @_('')
    def pnp(self, p):
        cuad.agregarCuadMain('gotoT')
        pass

    @_('var ";"  programa2 ', 'programa3')
    def programa2(self, p):
        pass

    @_('function ";"  programa2','programa2' ,'main ')
    def programa3(self, p):
        pass

    @_( 'MAIN pnp2 pn1  "{" estatutos "}" ')
    def main(self, p):
        TablaFV.scope = "global"
        cuad.agregarCuadMain('end')
        
        pass

    @_('')
    def pnp2(self, p):
        
        cuad.agregarCuadMain('gotoTC')
        pass

    @_( '')
    def pn1(self, p):
        TablaFV.scope = "global"
       
    #function---------------------------------------------------
    @_('fun', 'funVoid', 'size', 'color','clear', 'pendown', 'penup', 'arc', 'circle', 'point', 'line')
    def function(self, p):
        pass 
    
    #funvoid----------------------------------------------------


    auxPn2 = ""
    @_('VOID MODULE   pn2 "(" fun4 ")"  "{" fun3 "}" ')
    def funVoid(self, p):
        tablas.agregarF(self.auxPn2, "void", 0)
        cuad.agregarCuadCall('return', 0, 0)
        tablas.funFloat = 1000
        tablas.funInt = 2000
        tablas.funBool= 3000
        tablas.funChar = 4000
        cuad.fResult = 9000
        cuad.iResult = 10000
        cuad.bResult = 11000
        cuad.cResult = 12000
        TablaFV.scope = "global" 
        #tablas.tablaV.clear()
        #tablas.tablaEra[self.auxPn2]= {1000 : 0, 2000:0, 3000: 0, 4000:0  ,9000 : 0, 10000 : 0, 11000: 0}

        pass

    @_('ID')
    def pn2(self, p):
        #tablas.tablaV.clear()
        self.auxPn2 = p.ID
        TablaFV.scope = self.auxPn2
        #                      var fl | var int|var bool|var char|temp float|temp int|float bool
        tablas.tablaEra[p.ID]= {1000 : 0, 2000:0, 3000: 0, 4000:0  ,9000 : 0, 10000 : 0, 11000: 0}
        
        
    #fun-----------------------------------------------------------
    auxPn3 = ""
    auxTipo = ""
    rtr = 0
    @_('tipo   MODULE  pn3 "(" fun4 ")" "{" fun3  return0 "}"') # hay quedevolver el scope a global en var
    def fun(self, p):
        tablas.agregarF(self.auxPn3,self.auxTipo, 0) # hay que implementar el cubo semantico para que jale el return
        tablas.funFloat = 1000
        tablas.funInt = 2000
        tablas.funBool= 3000
        tablas.funChar = 4000
        cuad.fResult = 9000
        cuad.iResult = 10000
        cuad.bResult = 11000
        cuad.cResult = 12000
        #tablas.tablaV.clear()#-----
        #tablas.tablaEra[self.auxPn3]= {1000 : 0, 2000:0, 3000: 0, 4000:0  ,9000 : 0, 10000 : 0, 11000: 0}
        #agregar el resultado de return a una variable global
        TablaFV.scope = "global" 
        tablas.agregarV(self.auxPn3,self.auxTipo, self.rtr )
        
        pass


    @_('ID')
    def pn3(self, p):
        self.auxPn3 = p.ID
        TablaFV.scope = self.auxPn3
        #tablas.agregarC(p.ID, self.auxTipo)
        #                      var fl | var int|var bool|var char|temp float|temp int|float bool
        tablas.tablaEra[p.ID]= {1000 : 0, 2000:0, 3000: 0, 4000:0  ,9000 : 0, 10000 : 0, 11000: 0}
        

    #@_('var', '')
    #def fun2(self, p):
    #    pass

    @_('estatutos', '')
    def fun3(self, p):
        pass

    @_('parametros fun5', '')
    def fun4(self, p):
        pass

    @_('"," parametros', '')
    def fun5(self, p):
        pass

    #ESTATUTOS-------------------------------------------------
    @_('estatutos1', 'estatutos2', 'estatutos3', 'estatutos4', 'estatutos5','estatutos6','estatutos7', 'estatutos8','estatutos9','')
    def estatutos(self,p):
        pass

    @_('asignacion ";" estatutos')
    def estatutos1(self,p):
        pass

    @_('callVoid ";" estatutos')
    def estatutos2(self,p):
        pass


    @_('read ";" estatutos')
    def estatutos3(self,p):
        pass

    @_('write ";" estatutos')
    def estatutos4(self,p):
        pass

    @_('decision ";" estatutos')
    def estatutos5(self,p):
        #cuad.agregarCuadIf('gotoFC')
        pass

    @_('for0 ";" estatutos')
    def estatutos6(self,p):
        pass

    @_('while0 ";" estatutos')
    def estatutos7(self,p):
        pass

    @_('especiales ";" estatutos')
    def estatutos8(self,p):
        pass
    @_('var ";" estatutos')
    def estatutos9(self,p):
        pass

    #funciones especiales --------------------------------------------
    @_('size', 'color','clear', 'pendown', 'penup', 'arc', 'circle', 'point', 'line')
    def especiales(self,p):
        pass

   
    #asignacion-----------------------------------------------
    #auxValor = '' # es para asignar el id, char o str----- falta prpgramar
    #--------------!!!!!!-------------------------------
    @_('ID ASIGNACION exp end ', 'ID ASIGNACION asignacion2') # CHECAR CON STRINGS
    def asignacion(self,p):
        if(tablas.checa(p[0])):
            #tablas.agregarValor(p[0], cuad.resultado)
            auxM = tablas.buscarM(p[0]) 
            cuad.agregarCuadAsign(auxM,cuad.resultado, '=') 
        else: 
            print("la variable no esta")
        pass
    
    @_('asignacion5 ','asignacion4', 'asignacion3 ') # CHECAR CON STRINGS
    def asignacion2(self,p):
        pass
        #tablas.agregarC(p[0], 'char')
        #cuad.resultado = tablas.m
    @_('CSTRING ') # CHECAR CON STRINGS
    def asignacion5(self,p):
        tablas.agregarC(p[0], 'string')
        cuad.resultado = tablas.m
        pass

    @_('LETRA') # CHECAR CON STRINGS
    def asignacion4(self,p):
        tablas.agregarC(p[0], 'char')
        cuad.resultado = tablas.m
        pass

    @_('callVoid') # CHECAR CON STRINGS
    def asignacion3(self,p):
        pass

    #callvoid---------------------------------------------------
    auxp = 1
    auxCall = ''
    @_(' pnCall "(" exp end pnParam callVoid2 ")" ', 'pnCall "("  ")" ')
    def callVoid(self,p):
        cuad.agregarCuadCall('gosub', self.auxCall, 0)
        self.auxp = 1
        pass

    @_('ID') #<<<<---------------  checar
    def pnCall(self,p):
        if(tablas.buscarF(p[0])):
            self.auxCall =  p[0]
            cuad.agregarCuadCall('era', p[0], 0)
        else:
            print("no esta")
        pass

    @_('"," exp end pnParam ', '') #<<<<---------------  checar
    def callVoid2(self,p):
        pass

    @_('') #<<<<---------------  checar
    def pnParam(self,p):
        cuad.agregarCuadCall('param', self.auxp,  cuad.resultado)
        self.auxp += 1  
        pass

    #decision---------------------------------------------------
    
    @_('IF "(" expresion ")" THEN gotoF decision2 "}"  auxEl   ')
    def decision(self,p):
        pass

    @_('decision1','gotoFC')
    def auxEl(self,p):
        #cuad.agregarCuadIf('gotoF')
        pass

    @_('"{"')
    def gotoF(self,p):
        cuad.agregarCuadIf('gotoF')
        pass
    
    @_(' ')
    def gotoFC(self,p):
        cuad.agregarCuadIf('gotoFC')
        pass
    
    @_('gotoFC2 ELSE   gotoT  decision2 "}" gotoTC  ')
    def decision1(self,p):
        pass

    @_('')
    def gotoFC2(self,p):
        cuad.agregarCuadIf('gotoFC2')
        pass

    @_('"{"')
    def gotoT(self,p):
        cuad.agregarCuadIf('gotoT')
        pass

    @_('')
    def gotoTC(self,p):
        cuad.agregarCuadIf('gotoTC')
        pass

    @_('estatutos','')
    def decision2(self,p):
        pass
    
    
    #read -------------------------------------------------------
    auxRead = 0
    @_('READ "("  ")" ', 'READ "(" read4  ")" ')# checar que onda
    def read(self,p):
        cuad.agregarCuadF1( cuad.resultado, p[0])
        pass

    @_('read2','read3', 'read5' )# checar que onda
    def read4(self,p):
        #self.auxRead = p[0]
        #cuad.resultado = p[0]
        pass

    @_('exp end' )# checar que onda
    def read3(self,p):
        pass

    @_('LETRA') # CHECAR CON STRINGS
    def read5(self,p):
        tablas.agregarC(p[0], 'char')
        cuad.resultado = tablas.m
        pass

    @_(' CSTRING' )# checar que onda
    def read2(self,p):
        #self.auxRead = p[0]
        tablas.agregarC(p[0], 'string')
        cuad.resultado = tablas.m
        pass

    #write-------------------------------------------------------
    @_('WRITE "(" write2 ")" ','WRITE "(" write3 ")" ' ,'WRITE "(" write4 ")" ')
    def write(self,p):
        cuad.agregarCuadF1(cuad.resultado, 'write')
        pass

    @_('exp end ')
    def write2(self,p):
        pass

    @_(' CSTRING ')
    def write3(self,p):
        tablas.agregarC(p[0], 'string')
        cuad.resultado = tablas.m
        pass

    @_('LETRA') # CHECAR CON STRINGS
    def write4(self,p):
        tablas.agregarC(p[0], 'char')
        cuad.resultado = tablas.m
        pass
    
    


    #fors----------------------------------------------------
    pExp = 0
    sExp = 0
    @_('FOR pnF2  DO pnF4 "{" for1  pnF5 "}" pnF6')
    def for0(self,p):
        pass

    @_('pnF3 pnF1 TO exp end sExp2')
    def pnF2(self,p):
        cuad.agregarCuadExpresion( self.pExp,self.sExp, '==')
        pass

    @_('')
    def pnF3(self,p):
        cuad.agregarCuadFor( 'gotoFC')
        pass

    @_('')
    def pnF4(self,p):
        cuad.agregarCuadFor( 'gotoT')
        pass

    @_('')
    def pnF5(self,p):
        cuad.agregarCuadFor( 'gotoTC')
        pass

    @_('')
    def pnF6(self,p):
        cuad.agregarCuadFor( 'gotoF')
        pass

    @_('ID ASIGNACION exp end pExp1  ')
    def pnF1(self,p):
        #tablas.agregarV(p.ID,self.auxTipo, 0)
        if(tablas.checa(p[0])):
            #tablas.agregarValor(p[0], cuad.resultado)
            auxM = tablas.buscarM(p[0]) 
            self.pExp = auxM
            cuad.agregarCuadAsign(auxM,cuad.resultado, '=') 
        else: 
            print("la variable no esta")
        pass

    @_('')
    def pExp1(self,p):
        #self.pExp = cuad.resultado
        
        pass
    @_('')
    def sExp2(self,p):
        self.sExp = cuad.resultado
        pass

    @_('estatutos ', '')
    def for1(self,p):
        pass

    #while----------------------------------------------------
    @_('WHILE "(" pnw1 expresion ")" DO pnw2 "{" while1 pnw3 "}" pnw4')
    def while0(self,p):
        pass

    @_('estatutos', '')
    def while1(self,p):
        pass

    @_('') # guarda la direccion a donde hay que ir en caso de true 
    def pnw1(self,p):
        cuad.agregarCuadWhile('gotoTC')
        pass

    @_( '')
    def pnw2(self,p):# guarda la direccion a donde hay que ir en caso de true 
        cuad.agregarCuadWhile('gotoF')
        pass
    
    @_( '')
    def pnw3(self,p):
        cuad.agregarCuadWhile('gotoFC')
        pass

    @_( '')
    def pnw4(self,p):
        cuad.agregarCuadWhile('gotoT')
        pass
    
    #color --------------------------------------------------
    @_('COLOR "(" PALETA ")"')
    def color(self,p):
        cuad.agregarCuadF1( p[2], p[0])
        pass

    #CLEAR---------------------------------------------------
    @_('CLEAR "(" ")"')
    def clear(self,p):
        cuad.agregarCuadF1(  p[0])
        pass
    
    #pendow------------------------------------------------
    @_('PENDOWN "(" ")"')
    def pendown(self,p):
        cuad.agregarCuadF0( p[1])
        pass
    
    #PENUP----------------------------------------------
    @_('PENUP "(" ")"')
    def penup(self,p):
        cuad.agregarCuadF0( p[1])
        pass

    #ARC----------------------------------------------------
    arc1=0
    arc2=0
    @_('auxArc ARC "(" exp end "," exp end ")"')
    def arc(self,p):
        cuad.agregarCuadF2(self.arc1, self.arc2, p[1])
        self.arc1 = 0
        self.arc2 = 0
        pass

    @_('')
    def auxArc(self,p):
        self.arc1 = 0
        self.arc2 = 0
        pass

    #CIRCLE-------------------------------------------------
    @_('CIRCLE "(" exp end ")"')
    def circle(self,p):
        cuad.agregarCuadF1( cuad.resultado, p[0])
        pass

    #POINT---------------------------------------------------
    @_('POINT "(" exp end ")" ')
    def point(self,p):
        cuad.agregarCuadF1( cuad.resultado, p[0])
        pass

    #SIZE-------------------------------------------------
    @_('SIZE "(" exp end ")"')
    def size(self,p):
        cuad.agregarCuadF1( cuad.resultado, p[0])
        pass

    #line--------------------------------------------------
    line1 = 0
    line2 = 0
    @_('auxLine LINE "(" exp end "," exp end  ")"')
    def line(self,p):
        cuad.agregarCuadF2(self.line1, self.line2, p[1])
        self.line1 = 0
        self.line2 = 0
        pass


    @_('')
    def auxLine(self,p):
        self.line1 = 0
        self.line2 = 0
        pass

    #EXPRESION ---------------------------------------------
    primeraExp = 0
    segundaExp = 0
    @_('exp end expresion1 RELOP exp end expresion2')
    def expresion(self,p):
        cuad.agregarCuadExpresion( self.primeraExp,self.segundaExp, p.RELOP)
        pass

    @_('')
    def expresion1(self,p):
        self.primeraExp = cuad.resultado
        pass
    @_('')
    def expresion2(self,p):
        self.segundaExp = cuad.resultado
        pass


    #RETURN------------------------------------------------
    @_('RETURN "(" exp end ")" ')
    def return0(self,p):    
        cuad.agregarCuadCall('return', 0, cuad.resultado)
        #self.rtr =  cuad.resultado
        pass


    #EXP---------------------------------------------------
    @_('termino exp2 ')
    def exp(self,p):
        
        pass

    @_('')
    def end(self,p):
        cuad.agregaOp('end')
        pass

    @_('exp3 termino exp2','exp4 termino exp2', '')
    def exp2(self,p):
        #si el anterior no es  *, /, + , * guardar en el stack, si si es hacer la operacion 
        #y guardar el resultado 
        pass

    @_('MAS')
    def exp3(self,p):
        cuad.agregaOp("+")

    @_('MENOS')
    def exp4(self,p):
        cuad.agregaOp("-")

    #TERMINO-------------------------------------------
    @_('factor termino2')
    def termino(self,p):
        pass
    
    @_('termino3 factor termino2', 'termino4 factor termino2','')
    def termino2(self,p):
        #si el anterior no es  * o / guardar en el stack, si si es hacer la operacion 
        #y guardar el resultado 
        pass

    @_('MUL')
    def termino3(self,p):
        cuad.agregaOp("*")

    @_('DIV')
    def termino4(self,p):
        cuad.agregaOp("/")

    #PARAMETROS---------------------------------------
    #auxTipoP=''
    @_('tipo ID ')
    def parametros(self,p):
        tablas.agregarV(p.ID,self.auxTipo, 0)
        
        pass

    #factor --------------------------------------------------
    #@_('"(" expresion ")" ','MAS varnum',  'MENOS varnum', 'varnum')
    @_('factor2 exp factor3', 'varnum', '')
    def factor(self,p):
        pass

    @_('"("')
    def factor2(self,p):
        cuad.agregaOp("(")
    
    @_(' ")" ')
    def factor3(self,p):
        cuad.agregaOp(")")

    #VARNUM-------------------------------------------------
    @_('varnum2', 'varnum3')
    def varnum(self,p):
        pass

    @_('ID')
    def varnum2(self,p):
        if(tablas.checa(p[0]) ):
            self.rtr =  cuad.resultado
            if(self.line1 == 0):
                self.line1 =  cuad.resultado
            elif(self.line2 == 0):
                self.line2 =  cuad.resultado

            if(self.arc1 == 0):
                self.arc1 =  cuad.resultado
            elif(self.arc2 == 0):
                self.arc2 =  cuad.resultado
            cuad.agregaCons(p[0])
        else: 
            print("la variable no esta")
        pass

    @_('varnum5', 'varnum4')
    def varnum3(self,p):
        pass

    @_('CTEI')
    def varnum4(self,p):
        self.rtr =  p[0]
        tablas.agregarC(p[0], 'int')
        cuad.agregaCons(TablaFV.cInt)
        if(self.arc1 == 0):
            self.arc1 =  tablas.m
        elif(self.arc2 == 0):
            self.arc2 =  tablas.m
        if(self.line1 == 0):
            self.line1 =  tablas.m
        elif(self.line2 == 0):
            self.line2 =  tablas.m

        pass

    @_('CTEF')
    def varnum5(self,p):
        self.rtr =  p[0]
        tablas.agregarC(p[0], 'float')
        cuad.agregaCons(TablaFV.cFloat)
        if(self.arc1 == 0):
                #self.arc1 =  p[0]
            self.arc1 =  tablas.m
        elif(self.arc2 == 0):
                #self.arc2 =  p[0]
            self.arc2 =  tablas.m
        if(self.line1 == 0):
            self.line1 =  tablas.m
        elif(self.line2 == 0):
            self.line2 =  tablas.m
        pass

    #VAR --------------------------------------------------
    #auxTipoV =""
    @_('VAR tipo ":" ID ','VAR tipo ":" ID var2 ' )  # checar que onda con tipo 
    def var(self,p):
        tablas.agregarV(p.ID,self.auxTipo, 0)
        pass

    @_('"," pn6 var2' ,'')
    def var2(self,p):
        pass

    @_('ID')
    def pn6(self,p):
        tablas.agregarV(p.ID,self.auxTipo, 0)
        pass

    #tipo -----------------------------------------------

    @_('INT',' FLOAT', 'CHAR')
    def tipo(self,p):
        self.auxTipo = p[0]
        pass

if __name__ == '__main__':

    tablas = tablas()
    lexer = CalcLexer()
    parser = CalcParser()
    maquina = maquina()
    cuad = cuad()

    archivo = input("que archivo?")
    archivo2 = open( archivo, 'r')
    linea = ""

    for s in archivo2:
        linea += s.strip()

    parser.parse(lexer.tokenize(linea))    
    count = 1
    count2 = 0
    count3 = 1
    count4 = 0
    count5 = 1
    print("tabla  de variables:")
    for line in range(len(tablas.tablaV)):
        print(count," : ", tablas.tablaV[count])
        count =   count  + 1

    print("tabla  de constantes:")
    for line in range(len(TablaFV.tablaC)):
        print(count4," : ", TablaFV.tablaC[count4])
        count4 =   count4  + 1

    print("tabla funciones:")   
    for line in range(len(tablas.tablaF)):
        print(count2 +1," : ", tablas.tablaF[count2])
        count2 =   count2 +1

    print("tabla cuadruplos:")   
    for line in range(len(cuad.tablaQ)):
        print(count3 ," : ", cuad.tablaQ[count3])
        count3 =   count3 + 1

    print("tabla  de variables de main:")
    for line in range(len(tablas.tablaMV)):
        print(count5," : ", tablas.tablaMV[count5])
        count5 =   count5  + 1

    print("tabla era:")
    print(tablas.tablaEra)
    archivo2.close()

    maquina.procesos()
        

    
    
        
  

    
    


    
    
        
  

    
    
