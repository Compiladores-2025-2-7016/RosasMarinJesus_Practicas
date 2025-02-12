#include <stdio.h>

// Directiva 1: #define para definir una constante
#define MAX 5

// Directiva 2: #ifndef y #define para evitar inclusiones múltiples
#ifndef MENSAJE_Hola
#define MENSAJE_Hola
const char *MENSAJE = "Hola, bienvenido al programa!!\n";
#endif

// Directiva 3:
#pragma message("Compilando el programa con 4 directivas del preprocesador")

// Directiva 4: 
#define NUMEROS_O_LETRAS 1
#undef NUMEROS_O_LETRAS
int main(void) {
    printf("%s", MENSAJE);

    #if NUMEROS_O_LETRAS == 1
        printf("Imprimiendo numeros:\n");
        for (int i = 0; i < MAX; i++) {
            printf("%d\n", i);
        }
    #else
        printf("Imprimiendo letras.\n");
        for (int i = 0; i < MAX; i++){
            printf("%c\n",'a'+i);
        }
        
    #endif

        return 0;
}