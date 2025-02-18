import hashlib
import ecdsa
import secrets

# Generate ECDSA key pair
sk = ecdsa.SigningKey.generate(curve=ecdsa.NIST256p)
vk = sk.get_verifying_key()

# ECDSA signing function 
def ecdsa_sign(message, k):
    hash_message = int.from_bytes(hashlib.sha256(message).digest(), byteorder='big')
    
    G = ecdsa.NIST256p.generator
    n = G.order()
    
    r = (G * k).x() % n  # Compute r
    s = ((hash_message + r * sk.privkey.secret_multiplier) * pow(k, -1, n)) % n

    # Encode as signature
    sig = ecdsa.util.sigencode_string(r, s, n)  
    return sig

# Generate multiple signature
messages = [b"Challenge 1", b"Challenge 2"]
signatures = []

for msg in messages:
    sig = ecdsa_sign(msg, secrets.randbelow(2**32))
    print(f"Signed message: {msg}")
    signatures.append((msg, sig))

# Save public key and signatures
with open("public_key.pem", "wb") as f:
    f.write(vk.to_pem())

with open("signatures.txt", "w") as f:
    for msg, sig in signatures:
        f.write(f"{msg.hex()} {sig.hex()}\n")

print("🔐 Crypto Challenge: Recover the private key from the signatures!")

