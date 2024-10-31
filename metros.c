#include <stdio.h>

int main() {
    float metros, decimetros, centimetros, milimetros;

    printf("Digite um valor em metros: ");
    scanf("%f", &metros);

    decimetros = metros * 10;
    centimetros = metros * 100;
    milimetros = metros * 1000;

    printf("\nEquivalente em decímetros: %.2f dm", decimetros);
    printf("\nEquivalente em centímetros: %.2f cm", centimetros);
    printf("\nEquivalente em milímetros: %.2f mm\n", milimetros);

    return 0;
}
