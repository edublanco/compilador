

from sly import Lexer, Parser
from collections import defaultdict
from TablaFV  import * 
from Cuadruplos  import *
from CuboSemantico import cubo

class CalcLexer(Lexer):
    # Set of token names.   This is always required
    tokens = {  CTEI, CTEF,  ID, CSTRING, MAS, MENOS, INT, 
                ASIGNACION, IF, ELSE,
                RELOP, MUL, DIV, PROGRAMA,
                CHAR, FLOAT, VAR,
                MODULE, VOID, RETURN, PALETA,FOR, WHILE,
                MAIN, TO, DO, WRITE, READ, SIZE, COLOR, CLEAR,
                PENDOWN, PENUP, ARC, CIRCLE, POINT, LINE, THEN, LETRA}

    ignore = ' \t'
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

    def __init__(self):
        self.names = { }
    
    #Programa -----------------------------------------------------
    @_('PROGRAMA ID ":"  programa2')
    def programa(self, p):
        pass

    @_('var ";"  programa2 ', 'programa3')
    def programa2(self, p):
        pass

    @_('function ";" programa3 ', 'main ')
    def programa3(self, p):
        pass

    @_( 'MAIN pn1  "{" estatutos "}" ')
    def main(self, p):
        tablas.scope = "global"
        pass

    @_( '')
    def pn1(self, p):
        tablas.scope = "global"
       
    #function---------------------------------------------------
    @_('fun', 'funVoid', 'size', 'color','clear', 'pendown', 'penup', 'arc', 'circle', 'point', 'line')
    def function(self, p):
        pass 
    
    #funvoid----------------------------------------------------
    auxPn2 = ""
    @_('VOID MODULE   pn2 "(" fun4 ")" fun2 "{" fun3 "}" ')
    def funVoid(self, p):
        tablas.agregarF(self.auxPn2, "void", 0)
        pass

    @_('ID')
    def pn2(self, p):
        self.auxPn2 = p.ID
        tablas.scope = self.auxPn2
        tablas.memoriaV += 1000 
        tablas.memoriaF += 1000 
        
    #fun-----------------------------------------------------------
    auxPn3 = ""
    auxTipo = ""
    @_('tipo  MODULE  pn3 "(" fun4 ")" fun2 "{" fun3  return0 "}"') # hay quedevolver el scope a global en var
    def fun(self, p):
        tablas.agregarF(self.auxPn3,self.auxTipo, 0) # hay que implementar el cubo semantico para que jale el return
        pass

    @_('ID')
    def pn3(self, p):
        self.auxPn3 = p.ID
        tablas.scope = self.auxPn3
        tablas.memoriaV += 1000
        tablas.memoriaF += 1000 

    @_('var', '')
    def fun2(self, p):
        pass

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
            tablas.agregarValor(p[0], cuad.resultado)
            
        else: 
            print("la variable no esta")
        pass
    
    @_('CSTRING ','LETRA') # CHECAR CON STRINGS
    def asignacion2(self,p):
        cuad.resultado = p[0]

    #callvoid---------------------------------------------------
    @_('ID "(" parametros callVoid2 ")" ')
    def callVoid(self,p):
        pass

    @_('"," parametros ', '') #<<<<---------------  checar
    def callVoid2(self,p):
        pass

    #decision---------------------------------------------------
    @_('IF "(" expresion ")" THEN "{" decision2  "}" decision1')
    def decision(self,p):
        pass
    
    @_('ELSE "{" decision2  "}"  ', '')
    def decision1(self,p):
        pass

    @_('estatutos','')
    def decision2(self,p):
        pass
  
    #read -------------------------------------------------------
    @_('READ "(" ID read2 ")" ')
    def read(self,p):
        pass

    @_('"," ID  read2','')
    def read2(self,p):
        pass

    #write-------------------------------------------------------
    @_('WRITE "(" write2 ")" ')
    def write(self,p):
        pass

    @_(' CSTRING  write3 ', 'exp end write3')
    def write2(self,p):
        
        pass

    @_('"," CSTRING write3 ', ' "," exp end write3', '')
    def write3(self,p):
        pass

    #fors----------------------------------------------------
    @_('FOR ID ASIGNACION exp end TO exp end DO "{" for1 "}"')
    def for0(self,p):
        pass

    @_('estatutos ', '')
    def for1(self,p):
        pass

    #while----------------------------------------------------
    @_('WHILE "(" expresion ")" DO "{" while1 "}"')
    def while0(self,p):
        pass

    @_('estatutos', '')
    def while1(self,p):
        pass
    
    #color --------------------------------------------------
    @_('COLOR "(" PALETA ")"')
    def color(self,p):
        pass

    #CLEAR---------------------------------------------------
    @_('CLEAR "(" ")"')
    def clear(self,p):
        pass
    
    #pendow------------------------------------------------
    @_('PENDOWN "(" ")"')
    def pendown(self,p):
        pass
    
    #PENUP----------------------------------------------
    @_('PENUP "(" ")"')
    def penup(self,p):
        pass

    #ARC----------------------------------------------------
    @_('ARC "(" exp end "," exp end ")"')
    def arc(self,p):
        pass

    #CIRCLE-------------------------------------------------
    @_('CIRCLE "(" exp end ")"')
    def circle(self,p):
        pass

    #POINT---------------------------------------------------
    @_('POINT "(" exp end "," exp end ")"')
    def point(self,p):
        pass

    #SIZE-------------------------------------------------
    @_('SIZE "(" exp end ")"')
    def size(self,p):
        pass

    #line--------------------------------------------------
    @_('LINE "(" exp end "," exp end  ")"')
    def line(self,p):
        pass

    #EXPRESION ---------------------------------------------
    @_('exp end RELOP exp end')
    def expresion(self,p):
        pass

    #RETURN------------------------------------------------
    @_('RETURN "(" exp end ")" ')
    def return0(self,p):    
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
        if(tablas.checa(p[0])):
            auxT = tablas.extraerValor(p[0])
            #self.auxValor = auxT
            cuad.agregaCons(auxT)
            
        else: 
            print("la variable no esta")
        pass
        

       

    @_('CTEF', 'CTEI')
    def varnum3(self,p):
        #self.auxValor = p[0]
        cuad.agregaCons(p[0])
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
    cuad = cuad()

    


    while True:
        try:
            text = input('---> ')
            parser.parse(lexer.tokenize(text))
            
            
            count = 1
            count2 = 0
            print("tabla  de variables:")
            for line in range(len(tablas.tablaV)):
                print(count," : ", tablas.tablaV[count])
                count =   count  + 1

            print("tabla funciones:")   
            for line in range(len(tablas.tablaF)):
                print(count2 +1," : ", tablas.tablaF[count2])
                count2 =   count2 +1
          
        except EOFError:
            break

    
    
        
  

    
    


    
    
        
  

    
    
