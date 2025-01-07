#include <stdio.h>

// Definicion de variables de estado Para una
// sola maquina de estados:

void (*Estado_Presente_Maquina_1)(void);

// forward declaration, para poder referenciar
// todas las funciones de estados dentro de si
// mismas:

void Maquina_1(void);
void Maquina_1_Estado_1(void);
void Maquina_1_Estado_2(void);
void Maquina_1_Estado_3(void);
void Maquina_1_Estado_4(void);

// Partes de la maquina de estados:
// 1. Corazon de la maquina

void Maquina_1(void){
    (*Estado_Presente_Maquina_1)();
}

// 2. Estados de la maquina:

void Maquina_1_Estado_1(void){
    printf("M1, E1, para E3\n");
    Estado_Presente_Maquina_1 = &Maquina_1_Estado_3;
}

void Maquina_1_Estado_2(void){
    printf("M1, E2, para E4\n");
    Estado_Presente_Maquina_1 = &Maquina_1_Estado_4;
}

void Maquina_1_Estado_3(void){
    printf("M1, E3, para E2\n");
    Estado_Presente_Maquina_1 = &Maquina_1_Estado_2;
}

void Maquina_1_Estado_4(void){
    printf("M1, E4, para E1\n");
    Estado_Presente_Maquina_1 = &Maquina_1_Estado_1;
}



int main(){
    
    Estado_Presente_Maquina_1 = &Maquina_1_Estado_1;

    for (int i = 0; i<=10; i++){
        Maquina_1();
    }
    
}


