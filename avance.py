from sly import Lexer, Parser
from collection import defaultdict

class cubo
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
class tablas:
    tablaF = {}
    tablaV = {}
    # row va a ser el numero de linea empezando en 0 para irle sumando y desplazarse por el diccionario
    def agregarF(name, tipo, value, tablaVars, parametros):
        if name not in tablaF.keys(): 
        tablaF{
            'name':name,
            'tipo':tipo,
            'value':value,
            'tablaVars': tablaV,
            'parametros': parametros
        }

  
    def agregarV(name, value, scope):
        if name not in tablaV.keys(): 
        tablaV{
            'name':name,
            'tipo':tipo,
            'value':value,
            'scope':scope
        }


#------------------------------------------------------------ tablas ----------------------------------
 
class CalcLexer(Lexer):
    # Set of token names.   This is always required
    tokens = {  CTEI, CTEF,  ID, STRING, MAS, MENOS, INT, 
                ASIGNACION, IF, ELSE,
                RELOP, MUL, DIV, PROGRAMA,
                CHAR, FLOAT, VAR,
                MODULO, VOID, RETURN, PALETA,FOR, WHILE,
                MAIN, TO, DO, WRITE, READ, SIZE, COLOR, CLEAR,
                PENDOWN, PENUP, ARC, CIRCLE, POINT, LINE, THEN}

    ignore = ' \t'
    literals = { ';', ':', '(', ')', '{', '}',',' }

    
    CTEF    = r'([0-9]+)(\.)([0-9]+)?'
    CTEI    = r'[0-9]+'
    ID      = r'[a-zA-Z]([a-zA-Z]|[0-9_])*'
    STRING = r' [\"] ([a-zA-Z]*)+  [\"]'
    MENOS   = r'[\-]'
    MAS     = r'[\+]'
    MUL  = r'[\*]'
    DIV     = r'[\/]'
    RELOP = r'(<>)|(==)|(<=)|(>=)|(<)|(>)'
    ASIGNACION  = r'='
    

   
    ID['if'] = IF
    ID['else'] = ELSE
    ID['int'] = INT
    ID['float'] = FLOAT
    ID['programa'] = PROGRAMA
    ID['char'] = CHAR
    ID['var'] = VAR
    ID['module'] = MODULO
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

    def __init__(self):
        self.names = { }
    
    #Programa -----------------------------------------------------
    @_('PROGRAMA ID ":"  programa2')
    def programa(self, p):
        pass

    @_('var programa2', 'programa3')
    def programa2(self, p):
        pass

    @_('function programa3', 'MAIN "{" estatutos "}" ')
    def programa3(self, p):
        pass

    #function---------------------------------------------------
    @_('fun', 'funVoid', 'size', 'color','clear', 'pendown', 'penup', 'arc', 'circle', 'point', 'line')
    def function(self, p):
        pass 
    
    #funvoid----------------------------------------------------

    @_('VOID MODULO ID "(" fun4 ")" fun2 "{" fun3 "}" "}" ')
    def funVoid(self, p):
        pass

    #fun-----------------------------------------------------------
    @_('tipo MODULO ID "(" fun4 ")" fun2 "{" fun3 "}" return0 "}" ')
    def fun(self, p):
        pass

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
    @_('ID ASIGNACION exp ', 'ID ASIGNACION ID ', 'ID ASIGNACION STRING ') # CHECAR CON STRINGS
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
    
    @_('ELSE "{" decision2 ";" "}"  ', '')
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

    @_('STRING write3 ', 'expresion write3')
    def write2(self,p):
        pass

    @_('"," STRING write3 ', '"," expresion write3', '')
    def write3(self,p):
        pass

    #fors----------------------------------------------------
    @_('FOR ID ASIGNACION exp TO exp DO "{" for1 ";" "}"')
    def for0(self,p):
        pass

    @_('estatutos', '')
    def for1(self,p):
        pass

    #while----------------------------------------------------
    @_('WHILE "(" expresion ")" DO "{" while1 ";" "}"')
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
    
    @_('"," ID parametros2','')
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
    @_('VAR tipo ":" ID ";"','VAR tipo ":" ID var2 ";"')
    def var(self,p):
        pass

    @_('"," ID var2','')
    def var2(self,p):
        pass

    #tipo -----------------------------------------------
    @_('INT',' FLOAT', 'CHAR')
    def tipo(self,p):
        pass

if __name__ == '__main__':
 
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

    
    
