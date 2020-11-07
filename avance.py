from sly import Lexer, Parser
from collections import defaultdict



class cubo:
    cuboS = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))

    #suma
    cuboS['int']['int']['+'] ='int'
    cuboS['float']['float']['+'] ='float'
    cuboS['int']['float']['+'] ='float'
    cuboS['float']['int']['+'] ='float'

    #resta
    cuboS['int']['int']['-'] ='int'
    cuboS['float']['float']['-'] ='float'
    cuboS['int']['float']['-'] ='float'
    cuboS['float']['int']['-'] ='float'

    #dividir
    cuboS['int']['int']['/'] ='float'
    cuboS['float']['float']['/'] ='float'
    cuboS['int']['float']['/'] ='float'
    cuboS['float']['int']['/'] ='float'

    #mul
    cuboS['int']['int']['*'] ='int'
    cuboS['float']['float']['*'] ='float'
    cuboS['int']['float']['*'] ='float'
    cuboS['float']['int']['*'] ='float'

    #mayor
    cuboS['int']['int']['>'] ='int'
    cuboS['float']['float']['>'] ='int'
    cuboS['int']['float']['>'] ='int'
    cuboS['float']['int']['>'] ='int'
    
    #menor 
    cuboS['int']['int']['<'] ='int'
    cuboS['float']['float']['<'] ='int'
    cuboS['int']['float']['<'] ='int'
    cuboS['float']['int']['<'] ='int'

    #menor  igual
    cuboS['int']['int']['<='] ='int'
    cuboS['float']['float']['<='] ='int'
    cuboS['int']['float']['<='] ='int'
    cuboS['float']['int']['<='] ='int'

    #mayor  igual
    cuboS['int']['int']['>='] ='int'
    cuboS['float']['float']['>='] ='int'
    cuboS['int']['float']['>='] ='int'
    cuboS['float']['int']['>='] ='int'

    #igual
    cuboS['int']['int']['=='] ='int'
    cuboS['float']['float']['=='] ='int'
    cuboS['int']['float']['=='] ='int'
    cuboS['float']['int']['=='] ='int'

    #diferente
    cuboS['int']['int']['<>'] ='int'
    cuboS['float']['float']['<>'] ='int'
    cuboS['int']['float']['<>'] ='int'
    cuboS['float']['int']['<>'] ='int'

    #asignar 
    cuboS['int']['int']['='] ='int'
    cuboS['float']['float']['='] ='float'
    cuboS['char']['char']['='] ='char'

#------------------------------------------------------------ tablas ----------------------------------
class  Tablas():
    tablaF = {}
    i = 0 
    scope = "global"
    tablaV = {}
    j=0
    memoriaF = 0
    memoriaV = 0
    auxMemVarG = 0

    def agregarF(self, nombre, tipo, valor):  
        self.tablaF[self.i]= {'name': nombre, 'type': tipo, 'value': valor, 'memoria' : self.memoriaF}
        self.i += 1
        #self.memoriaF += 1000;
        print(self.tablaF)

    def agregarV(self, nombre, tipo, valor):
        
        self.j += 1
        # checa si la memoria es global
        # memoria de la variable en en 1, el aux es para cuando vuelva a global
        if(tablas.scope == "global"  and self.memoriaV < 1000):
            self.memoriaV += 1
            self.auxMemVarG += 1
        
        # checa si el scope es otra vez global y le resta a la direccion de memoria de las variables
        # la direccion de memoria de funciones para devolver la direccion memoria a global, y continua el conteo de memoria global
        elif(self.scope == "global" and self.memoriaV >= 1000 ):
            self.memoriaV -= self.memoriaF 
            self.memoriaV = self.auxMemVarG + 1
        # si sigue en el scope de la misma funcion nomas suma 1 a la direcion de memoria de las variables
         # checa si la direccion memoria es del mismo scope, sino empieza 
         # la direccion de memoria de las variables en en 1 + la direecion de memoria de la funcion
        elif (self.scope != self.tablaV[self.j - 1]['scope']): 
            #self.memoriaV += 1
            self.memoriaV = self.memoriaF +1
            #self.memoriaV += 1000
        else:
            self.memoriaV += 1
        
        print(self.memoriaV)
        print(self.memoriaF)


        self.tablaV[self.j] = {'name': nombre, 'type': tipo, 'value': valor, 'scope': self.scope, 'memoria' : self.memoriaV}
        print(self.tablaV)

#------------------------------------------------------------ tablas ----------------------------------
 
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
  
    #@_(r'\d+')
    #def CTEI(self, t):
    #    t.value = int(t.value)
    #    return t
    

class CalcParser(Parser):
    # Get the token list from the lexer (required)

    tokens = CalcLexer.tokens
    aux = 0 

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
        print("scope:")
        print(tablas.scope)
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
        #tablas.scope = p.ID
        #self.auxPn2 = p.ID
        tablas.agregarF(self.auxPn2, "void", 0)
        print("scope:")
        print(tablas.scope)
        pass

    @_('ID')
    def pn2(self, p):
        self.auxPn2 = p.ID
        tablas.scope = self.auxPn2
        tablas.memoriaF += 1000
        
    
    #fun-----------------------------------------------------------
    auxPn3 = ""
    @_('tipo MODULE  pn3 "(" fun4 ")" fun2 "{" fun3  return0 "}"') # hay quedevolver el scope a global en var
    def fun(self, p):
        #aux = p.ID
        #tablas.Scope = p.ID
        tablas.agregarF(self.auxPn3,"pendiente", 0) # hay que implementar el cubo semantico para que jale el return
        print("scope:")
        print(tablas.scope)
        pass
    
    @_('ID')
    def pn3(self, p):
        self.auxPn3 = p.ID
        tablas.scope = self.auxPn3
        tablas.memoriaF += 1000
        
    
    @_('var', '')
    def fun2(self, p):
        pass

    @_('estatutos', '')
    def fun3(self, p):
        pass

    @_('parametros', '')
    def fun4(self, p):
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
    @_('ID ASIGNACION exp ', 'ID ASIGNACION ID ', 'ID ASIGNACION CSTRING ','ID ASIGNACION LETRA') # CHECAR CON STRINGS
    def asignacion(self,p):
        pass

    #callvoid---------------------------------------------------
    @_('ID "(" parametros ")" ')
    def callVoid(self,p):
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

    @_(' CSTRING  write3 ', 'exp write3')
    def write2(self,p):
        pass

    @_('"," CSTRING write3 ', ' "," exp write3', '')
    def write3(self,p):
        pass

    #fors----------------------------------------------------
    @_('FOR ID ASIGNACION exp TO exp DO "{" for1 "}"')
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
    @_('ARC "(" exp "," exp ")"')
    def arc(self,p):
        pass

    #CIRCLE-------------------------------------------------
    @_('CIRCLE "(" exp ")"')
    def circle(self,p):
        pass

    #POINT---------------------------------------------------
    @_('POINT "(" exp "," exp ")"')
    def point(self,p):
        pass

    #SIZE-------------------------------------------------
    @_('SIZE "(" exp ")"')
    def size(self,p):
        pass

    #line--------------------------------------------------
    @_('LINE "(" exp "," exp ")"')
    def line(self,p):
        pass

    #EXPRESION ---------------------------------------------
    @_('exp RELOP exp')
    def expresion(self,p):
        pass

    #RETURN------------------------------------------------
    @_('RETURN "(" exp ")" ')
    def return0(self,p):
        
        pass

    #EXP---------------------------------------------------
    @_('termino exp2')
    def exp(self,p):
        
        pass

    @_('MAS termino exp2','MENOS termino exp2', '')
    def exp2(self,p):
        pass
    #TERMINO-------------------------------------------
    @_('factor termino2')
    def termino(self,p):
        pass
    
    @_('MUL factor termino2', 'DIV factor termino2','')
    def termino2(self,p):
        pass

    #PARAMETROS---------------------------------------
    @_('tipo ID parametros2')
    def parametros(self,p):
        pass
    
    @_('"," ID parametros2','"," tipo ID parametros2','')
    def parametros2(self,p):
        pass

    #factor --------------------------------------------------
    @_('"(" expresion ")" ','MAS varnum',  'MENOS varnum', 'varnum')
    def factor(self,p):
        pass

    #VARNUM-------------------------------------------------
    @_('ID', 'CTEF', 'CTEI')
    def varnum(self,p):
        pass

    #VAR --------------------------------------------------

    @_('VAR tipo ":" ID ','VAR tipo ":" ID var2 ' )  # checar que onda con tipo 
    def var(self,p):
        tablas.agregarV(p.ID,"tipo", 0)
        print("scope:")
        print(tablas.scope)
        pass

    @_('"," ID var2' ,'')
    def var2(self,p):
        pass

    #tipo -----------------------------------------------
    @_('INT',' FLOAT', 'CHAR')
    def tipo(self,p):
        pass

if __name__ == '__main__':
    tablas = Tablas()
    lexer = CalcLexer()
    parser = CalcParser()
    while True:
        try:
            text = input('---> ')
            parser.parse(lexer.tokenize(text))
            #for tok in lexer.tokenize(text):
            #    print(tok)
        except EOFError:
            break
        
            
 #           parser.parse(lexer.tokenize(text))

    
    
