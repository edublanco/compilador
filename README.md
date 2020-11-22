# primer avance
- Se acepta la gramatica establecida por los diagramas hechos previamente.
- Se utilizo python y las librerias de sly.
- se puede probar con 

  programa ejem  : var int : x ; main { color(red) ; clear(); pendown(); if( a > 3 ) then { clear();};}   
  
  en consola y no debe salir ningun error

# segundo avance 
- se agrego un cubo semantico por medio de diccionarios anidados
- se agrego la tabla de variables 
- se agrego la tabla de funciones

# Tercer avance 
- correccion de errores en las reglas gramaticales
- aceptacion de strings
- modificacion de las tablas de variables
- adicion del token letras 

# Cuarto avance 
- correccion de errores en las tablas de variables
- las tablas de variables ya guardan variables
- las tablas de funciones ya guardan funciones
- falta corregir scope
- falta ver como implementar bien el tipo 
- falta integrar el cubo semantico

# Quinto avance 
- adicion de memoria en la tablas de funciones y variables
- la memoria de las variables es ajusta conforme a la memoria de las funciones
- se corrigio el scope en las tablas de variables 
- checar la regla de while do
- implementar que lea desde  un archivo de txt

# Sexto avance
- la tabla registra los tipos de cada variable, parametro y funcion
- se añadieron los parametros a la tabla de variables 
- modificacion en la regla de parametros
- ajuste en la funcion de agregarv
- separacion del codigo en diferentes scripts 

# Septimo avance
- Se implementaron los cuadruplos aritemeticos en el script de pruebas
- Todavia tienen fallas de logica
- ya se puede asignar valores a las variables
- ya reconoce si se quiere asignar algo a una variable inexistente

# Octavo avance
- Se implementaron los cuadruplos aritemeticos en el script de pruebas
- Correccion de errores 
- funcionalidad de asigancion 

# Noveno avance 
- Se implementaron los cuadruplos condicionales 
- Se inlcuyo las expresiones en los cuadruplos asi como los resultados
- Correccion de errores 
- se agrego la funcion write a lso cuadruplos
intentar con el siguiente codigo:
programa m :  var int: a; main{  if(a < 2)then {a =2-8;    if(a<2)then{ a = 9;} else {write("w");};    a = 9 *(2+5);}      ;  }

# Decimo avance 
- Se implementaron los cuadruplos de fors
- Se implementaron los cuadruplos de whiles
- Se corrigieron los cuadruplos aritmeticos para que se almacenara la direccion en vez del resultado
- se implementaron tablas de constantes

# Onceavo avance 
- Se implementaron los cuadruplos de funciones
- Se implementaron los tipos 
- Se corrigieron errores

# doceavo y treceavo avance 
- se implemento la maquina virtual para la aritmetica, ifs,whiles, fors y write
- a todas las direcciones se les asigno respectivamente una direccion simbolica de lo que son:
	- vars locales:
		* float: 1001 - 2000
		* int: 2001 -3000
		* bool: 3001 - 4000
		* char: 4001 -5000
	- constantes:
		* float: 5001 - 6000
		* int: 6001 -7000
		* bool: 7001 - 8000
		* char: 8001 -9000
		* str: 16001 - 17000
	- temps:
		* float: 9001 - 10000
		* int: 10001 -11000
		* bool: 11001 - 12000
	- vars globales:
		* float: 12001 - 13000
		* int: 13001 - 14000
		* bool: 14001 - 15000
		* char: 15001 - 16000
- creacion del ERA y la tabla qe va a mandar toda la info de las funciones (tablaEra)
- creacio de la tabla que le manda la informacion de las variables globales a la maquina virtual (tablaMV)
- creacion de la tabla de temporales para maquina (tempsMF)
- correccion de errores en el for



# Ejemplo del leguaje para ver las tablas:

programa raul : var int : a; var float : b; void module funv (int ejem )var int: d{clear(); var int : c;};float module ejem2 (float r, int javier) var int : j {clear(); var int: e; return(23)}; int module ejem3(char w){var int :s; return(2)};main{ var int :h; var char : l;}

# Ejemplo del leguaje:

programa raul : 
var int : t; 
void module funv (int ejem ){clear();};
float module ejem2 (float r, int javier) 
var int : j {clear(); return(23)}; 
main {
	if(2>=2)then{
		write("ASD");
	};
	for a = 2 to 3 do {
		read(sd);
	}; 
	while(2<4)do{
		sdf(int f);
		clear();
	};
	a=3+9; 
	pendown(); 
	penup(); 
	color(red); 
	arc(3,5); 
	circle(3*4); 
	point(2*3, 9); 
	size(3);
	line(5.6,34); 
	var char : OI; 
	A ='E';
}
