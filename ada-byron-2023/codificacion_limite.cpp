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

    // while(c = getchar() != '.') funciona
    // Si encuentra letra - punto - punto imprime la letra, sin '\n'.
    /*string str;
    getline(cin, str);
    cout << str << endl;
    cout << str[2] << endl; // funciona
    */
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
