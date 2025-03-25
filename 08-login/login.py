import string
import sys
from itertools import product
from IPython import embed

def derive_pwd(input_pwd):
    c = 0x1337
    output = []
    for i in range(len(input_pwd)):
        c = (c * 0x42) & 0xffff
        output.append(chr(ord(input_pwd[i]) - (c % 10)))
    return ''.join(output)

def login():
    password = input("Enter password: ")
    derived = derive_pwd(password)

    if derived == "Ng\x1ad2]g3lZ":
        print("login granted")
    else:
        print("cant login, get away")
        sys.exit(-1)

if __name__ == "__main__":
    login()
    embed()


