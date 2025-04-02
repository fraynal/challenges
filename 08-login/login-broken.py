# Résumé des 3 failles principales de derive_pwd()
#
# 1. c % 10 == 0 à certaines positions
# À certaines positions (ex. position 2, 5, 9...), le décalage delta = c % 10 vaut zéro.
# Ce qui signifie : le caractère n’est pas modifié du tout à ces positions.
# ➤ Un attaquant peut reconnaître certains caractères du mot de passe dans la sortie dérivée, tels quels.
# 2. c == 0 après 16 itérations
# À la 17ᵉ position (index 16), le registre c devient 0, et le reste bloqué à 0 pour toutes les itérations suivantes.
# Donc : c % 10 == 0 pour tous les caractères après la 16ᵉ position.
# ➤ Cela signifie que la fin du mot de passe n’est jamais transformée : elle apparaît en clair dans la version dérivée.
# 3. c et c % 10 sont entièrement prévisibles
# c est mis à jour à chaque tour selon une suite fixe :
# c₀ = (0x1337 * 0x42) & 0xffff, puis cᵢ = (cᵢ₋₁ * 0x42) & 0xffff
# Cette suite ne dépend pas du mot de passe, uniquement de la position.
# ➤ L’attaquant peut pré-calculer à l’avance tous les décalages delta[i] = cᵢ % 10, et les utiliser pour reconstruire le mot de passe.


import string
import sys
from itertools import product
from IPython import embed

secret = "Ng\x1ad2]g3lZ"

def calc_coef():
    for i in range(20):
        c = 0x1337
        for _ in range(i):
            c = (c * 0x42) & 0xffff
        print(f"Position {i:2d} → c = {c:5d}, c % 10 = {c % 10}")


def derive_pwd(input_pwd):
    c = 0x1337
    output = []
    for i in range(len(input_pwd)):
        c = (c * 0x42) & 0xffff
        output.append(chr(ord(input_pwd[i]) - (c % 10)))
    return ''.join(output)

def get_offsets(length):
    c = 0x1337
    offsets = []
    for _ in range(length):
        c = (c * 0x42) & 0xffff
        offsets.append(c % 10)
    return offsets

def reverse_guess(derived):
    offsets = get_offsets(len(derived))
    return ''.join(chr(ord(derived[i]) + offsets[i]) for i in range(len(derived)))

def login():
    password = input("Enter password: ")
    derived = derive_pwd(password)

    if derived == secret:
        print("login granted")
    else:
        print("cant login, get away")

if __name__ == "__main__":

    # Attaque par inversion directe
    guess = reverse_guess(secret)
    print(f"[+] Password successfully reversed: {guess}")
    login()
    embed()

