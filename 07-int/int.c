#include <stdio.h>

int main() {
    unsigned int a, b;

    // Entrée utilisateur
    printf("Entrez deux nombres entiers non signés (séparés par un espace) : ");
    scanf("%u %u", &a, &b);

    unsigned int result = a + b;

    if (result < a || result < b) {
        printf("Trésor obtenu!\n");
    } else {
        printf("Pas de trésor ici!\n");
    }

    return 0;
}



