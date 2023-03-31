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

    scanf("%c", &c_in);
    while(c_in != EOF){
        cin >> c_in;
        if(c_in == '\n'){
            cout << '\n';
        }else if(c_in != '.'){
            c_w = c_in;
            scanf("%c", &c_in);
            if(c_in == '.'){
                scanf("%c", &c_in);
                if(c_in == '.'){
                    // Si llega aquí, ha encontrado
                    // letra-punto-punto, y se añade la letra
                    cout << c_w;
                }else if(c_in == '\n'){
                    cout << '\n';
                }
            }else if(c_in == '\n'){
                cout << '\n';
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