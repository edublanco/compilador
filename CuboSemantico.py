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