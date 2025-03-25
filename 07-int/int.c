/*
 * https://www.linkedin.com/feed/update/urn:li:activity:7308030238104379392/
 * 
 * Sylvain Patureau Mirand
 * 
 * Rien de mieux que la pratique :
 * user@D10:~/Transfert$ gcc -Wall -Wextra -Werror -Wformat -Wformat-security -fstack-protector-strong -fPIE -m64 -Wa,--noexecstack -O3 int.c -o int.exe
 * user@D10:~/Transfert$ ./int.exe
 * Entrez deux nombres entiers non signes (separes par un espace) : -1 1
 * Tresor obtenu!
 * user@D10:~/Transfert$ ./int.exe
 * Entrez deux nombres entiers non signes (separes par un espace) : 4294967295 1
 * Tresor obtenu!
 * 
 * (ce qui est marrant c'est que les options de compilation ne sortent pas la moindre erreur).
 */ 

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



