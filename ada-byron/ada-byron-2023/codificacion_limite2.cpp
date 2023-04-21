// En este caso, caracter a caracter

#include <bits/stdc++.h>
#include <iostream>
#include <istream>
#include <stdio.h>
#include <string> 

using namespace std;


// En c++, eof() devuelve End Of File
int main() 
{
    ios_base::sync_with_stdio(false); //Template para prog. competitiva
    cin.tie(NULL); // Template para prog. competitiva

    char c_in; // Caracter leyendo de entrada
    char c_w; // Caracter de la palabra a imprimir
    bool letra = false;
    bool punto = false;
    bool palabra = false;
    // EOF es el valor que toma c_in cuando no hay más entradas
    while((c_in = std::getchar()) != EOF){
        if(c_in == '\n'){
            if(palabra){
                printf("\n");
            }
            letra = palabra = punto = false;
        }else{
            if(c_in == '.'){
                if(letra && punto){
                    printf("%c", c_w);
                    palabra = true;
                    letra = false;
                }else{
                    punto = true;
                }
            }else{
                c_w = c_in;
                letra = true;
                punto = false;
            }
        }
    }
    return 0;
}

/* EXPLICACIÓN
Este es un segundo intento para aumentar la velocidad.
Se intenta leer caracter a caracter en vez de por línea.

El código queda horroroso, por motivos de la competición. Se recompensa
el grano fino al dedillo, en vez de un buen algoritmo.
*/