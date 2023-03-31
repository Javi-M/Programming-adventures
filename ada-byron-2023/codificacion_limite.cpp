// g++ codificacion_limite.cpp

#include <bits/stdc++.h>
#include <iostream>
#include <stdio.h>
#include <string> 

using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false); //Template para prog. competitiva
    cin.tie(NULL); // Template para prog. competitiva
    string line;
    while(getline(cin, line)){
        int n =  line.length();
        for(int i = 0; i < n-2; i++){
            if(line[i] != '.' && line[i+1] == '.' && line[i+2] == '.'){
                cout << line[i];
            }
        }
        cout << '\n'; // '\n' mas rapido que endl
    }
    return 0;
}

/* EXPLICACIÓN
Cuando lee una linea, al encontrar una letra y 2 puntos, esa letra
debe añadirse a la palabra. Al cambiar de línea de input,
empezamos otra palabra.
Como es apreciable, "line" es recorrida 2 veces:
para recibirla con getline y para encontrar las letras y puntos.
Poder recorrer cada linea de input una vez, caracter a caracter,
aumentaría la velocidad.
*/