#include <stdio.h>
int main() {
    float raio;
    float area;

    printf("Digite o raio: ");
    scanf("%f", &raio);

    area = (raio * raio) * 3.14159;

    printf("A=%0.4f\n", area);

    return 0;
}
