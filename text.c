#include <stdio.h> 

int main() {
    float valorConta; 
    float percentualGorgeta; 
    float valorGorgeta; 
    float total; 

    
    printf("Digite o valor da conta: ");
    scanf("%f", &valorConta); 

  
    printf("Digite o percentual de gorjeta (por exemplo, 10 para 10%%): ");
    scanf("%f", &percentualGorgeta);

  
    valorGorgeta = (percentualGorgeta / 100) * valorConta;

   
    total = valorConta + valorGorgeta;

 
    printf("Valor da gorjeta: %.2f\n", valorGorgeta);

    printf("Valor total (conta + gorjeta): %.2f\n", total);

    return 0; 
}
