#include <iostream>
#include <math.h>
#include <iomanip>
#include <string>
using namespace std;

int main(){
//Declaracion de los strings
string nombre_jugador,apellido_jugador,nombre_completo_jugador;
//Variables
int opcion_1= 0; //Variable donde se almacenará la opcion elegida

float cant_partidos=0; //Variable donde se almacenará la cantidad de partidos jugados

float cant_goles=0; //Variable donde se almacenará la cantidad de goles convertidos
//Bienvenida
cout<<"Bienvenido a la calculadora de media goleadora\n";
//Bucle
while(true){
    
    //Opcion: Number -> Estado
    //Se ingresará el numero 1 si desea seguir o comenzar a ingresar los datos para la calculadora o 2 si desea cancelar la acción
    //Para mayor simplificación del código, cualquier numero diferente de 1 será acción suficiente para finalizar el programa
    cout<<"\nIngrese 1 si desea continuar o, ingrese 2 si desea cancelar: ";
    cin>>opcion_1;
    if (opcion_1!=1){
        break;
    }
    //nombre_completo_jugador: String String -> String
    //Se conformará el nombre completo del jugador 
    cout<<"\nIngrese el nombre del jugador: "; //Nombre
    cin>> nombre_jugador;
    cout<<"\n Ingrese el apellido del jugador: "; //Apellido
    cin>> apellido_jugador;
    nombre_completo_jugador = nombre_jugador + " " + apellido_jugador; //Formador

    //media_goleadora: Number Number -> Number
    //Se realizará el promedio goleador, dividiendo la cantidad de goles sobre los partidos jugados, obteniendo un dato tipo float
    cout<<"\nIngrese la cantidad de partidos que jugo en el año: "; //Partidos
    cin>>cant_partidos;
    cout<<"\nIngrese la cantidad de goles que logro realizar: "; //Goles
    cin>>cant_goles;
    float media_goleadora = cant_goles /cant_partidos; //Promedio

    cout<<"\nEl jugador "<<nombre_completo_jugador<<" ha ejecutado "<<cant_goles<<" goles en "<<cant_partidos<<", logrando una media goleadora de:"<<media_goleadora<<"\n";
    
    if(media_goleadora <= 0.15){
        cout<<"El rendimiento goleador del jugador en la competición fue malo";
    }
    else if(media_goleadora >0.15 && media_goleadora<=0.35){
        cout<<"El rendimiento goleador del jugador en la competición fue bueno";
    }
    else if(media_goleadora >0.35 && media_goleadora<=1)
        cout<<"El rendimiento goleador del jugador en la competición fue muy bueno";
    else{
        cout<<"El rendimiento goleador del jugador en la competición fue letal";
    }
}
return 0;

}