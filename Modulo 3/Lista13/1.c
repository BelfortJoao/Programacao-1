#include <stdlib.h>
#include <stdio.h>
int main(void){
    int print(int x);
    int entrada, saida, Controle;
    printf("Escreva um numero:");
    scanf("%d", & entrada);
    saida = print(entrada);
    controle = entrada;
    system("pause");
    return 0;
}
int print(int x){
    int saida;
    if (entrada == 0){
        return;
    } else {
        for (contador = 0; contador <= Controle; contador++){
            printf("* ");
        }
        print(entrada --);
    }
};