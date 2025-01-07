#include <stdio.h>

int main () {

    int arr [] = {1,2,3,4,5,6,7,8,9,10};
    int i = 5;
    
    printf("Valor 1 -> %d\n", arr[i]);
    printf("Valor 2 -> %d\n", i[arr]);

    // Razon: 
    printf("Valor 3 -> %d\n", *((arr)+(i)));

    // Mas pruebas:

    int *ptr = arr + i;
    printf("Valor 4 -> %d\n", *((arr)+(i)));
    printf("Valor 5 -> %d\n", *(ptr));

    // Se puede interpretar el * como "el valor
    // contenido en..."
    
    int **ptr2 = &ptr;
    printf("Valor 6 -> %d\n", *(*(ptr2)));
    
    // Hipotesis, se puede interpretar el & como
    // "la direccion del valor en..."

    return 0;
}
