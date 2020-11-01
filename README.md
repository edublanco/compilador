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

# Cuartp avance 
- correccion de errores en las tablas de variables
- las tablas de variables ya guardan variables
- las tablas de funciones ya guardan funciones
- falta corregir scope
- falta ver como implementar bien el tipo 
- falta integrar el cubo semantico


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
