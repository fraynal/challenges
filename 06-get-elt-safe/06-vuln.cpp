#include <stdio.h>
#include <iostream>
#include <stdint.h>

#define SIZE 8
#define SIZE2 8

inline uint32_t *get_element_safe(uint32_t *arr, uint32_t index) {
    if(index >= SIZE) {
        return nullptr;
    }
    return arr + index;
}

int main(int argc, char **argv) {
    uint32_t arr[SIZE];
    uint32_t secret[SIZE2];

    for(uint32_t i = 0; i < SIZE; i++) arr[i] = i;

    FILE *fp = fopen("secret.txt", "rb");
    fread(secret, 1, sizeof(secret), fp);
    fclose(fp);

    uint32_t index;
    std::cin >> index;

    uint32_t *element = get_element_safe(arr, index);
    printf("Element: %x\n", *element);

    return 0;
}
