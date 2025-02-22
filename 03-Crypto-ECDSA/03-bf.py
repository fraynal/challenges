import hashlib
import ecdsa
from binascii import unhexlify
from tqdm import tqdm  # Progress bar for brute-force

# Load the public key
with open("public_key.pem", "rb") as f:
    vk = ecdsa.VerifyingKey.from_pem(f.read())

# Load the signatures (without the nonce `k`)
with open("signatures.txt", "r") as f:
    lines = f.readlines()

signatures = []
for line in lines:
    parts = line.strip().split()
    msg = unhexlify(parts[0])
    sig = unhexlify(parts[1])
    signatures.append((msg, sig))

# ECDSA Brute-Force Attack to Recover `k`
def bruteforce_k(signatures, curve=ecdsa.NIST256p):
    G = curve.generator
    n = G.order()

    (msg1, sig1) = signatures[0]

    r, s1 = ecdsa.util.sigdecode_string(sig1, n)

    # Compute message hashes
    h1 = int.from_bytes(hashlib.sha256(msg1).digest(), byteorder="big")

    print("🔍 Brute-forcing nonce k... (this may take some time)")

    for k1 in tqdm(range(2**32)):  # Brute-force uint32 space (0 to 4,294,967,295)
        # Solve for the private key: d = ((s1 * k1 - h1) * inverse(r, n)) % n
        private_key = ((s1 * k1 - h1) * pow(r, -1, n)) % n

        # Check if the private key is valid by generating its public key and comparing
        candidate_sk = ecdsa.SigningKey.from_secret_exponent(private_key, curve=curve)
        candidate_vk = candidate_sk.verifying_key

        if candidate_vk.to_string() == vk.to_string():
            print(f"🔥 Private Key Recovered: {hex(private_key)}")
            print(f"✅ Correct nonce k found: {k1}")
            return private_key

    print("❌ Brute-force failed. Check assumptions or try a larger range.")
    return None

# Run the attack
private_key = bruteforce_k(signatures)

