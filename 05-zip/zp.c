#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#pragma pack(1) // Empêche l'alignement mémoire

#define ZIP_LOCAL_FILE_HEADER_SIGNATURE 0x04034b50
#define MAX_FILENAME_LEN 256  

// Structure du Local File Header
typedef struct {
    uint32_t signature;        // Signature: 0x04034b50
    uint16_t version;          // Version minimale requise
    uint16_t flags;            // Indicateurs généraux
    uint16_t compression;      // Méthode de compression
    uint16_t mod_time;         // Heure de modification
    uint16_t mod_date;         // Date de modification
    uint32_t crc32;            // CRC-32
    uint32_t compressed_size;  // Taille compressée
    uint32_t uncompressed_size;// Taille non compressée
    uint16_t filename_length;  // Longueur du nom de fichier
    uint16_t extra_length;     // Longueur du champ extra
} LocalFileHeader;

// Fonction qui parse le ZIP et affiche les données du premier fichier
void afficherFichierZIP(const char *zip_filename) {
    FILE *file = fopen(zip_filename, "rb");
    if (!file) {
        perror("Erreur lors de l'ouverture du fichier");
        return;
    }

    LocalFileHeader header;
    fread(&header, sizeof(LocalFileHeader), 1, file);

    // Vérification de la signature du Local File Header
    if (header.signature != ZIP_LOCAL_FILE_HEADER_SIGNATURE) {
        printf("Fichier ZIP invalide !\n");
        fclose(file);
        return;
    }

    printf("===== Local File Header trouvé =====\n");
    printf("Compression : %u\n", header.compression);
    printf("Taille compressée : %u octets\n", header.compressed_size);
    printf("Taille non compressée : %u octets\n", header.uncompressed_size);
    printf("Longueur du nom de fichier : %u\n", header.filename_length);

    char filename[MAX_FILENAME_LEN]; 
    fread(filename, header.filename_length, 1, file);
    filename[header.filename_length] = '\0'; 

    printf("Nom du fichier : %s\n", filename);

    // Lecture des données du fichier
    char *data = (char *)malloc(header.compressed_size + 1);
    if (!data) {
        printf("Erreur d'allocation mémoire\n");
        fclose(file);
        return;
    }

    fread(data, header.compressed_size, 1, file);
    data[header.compressed_size] = '\0';

    printf("Données du fichier :\n%s\n", data);

    free(data);
    fclose(file);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <fichier.zip>\n", argv[0]);
        return 1;
    }

    afficherFichierZIP(argv[1]);
    return 0;
}
