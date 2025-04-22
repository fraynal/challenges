import signal
import sys
import random

SECRET = "BOOM{you_triggered_the_hidden_explosion}"

def handler(signum, frame):
    print("[!] Timeout triggered!")
    print(f"Here’s your secret: {SECRET}")
    sys.exit(0)

signal.signal(signal.SIGALRM, handler)

def is_similar(a, b):
    if len(a) != len(b):
        return False
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

def deep_compare(a, b):
    def compute(n):
        if n <= 1:
            return 1
        return compute(n - 1) + compute(n - 2)

    n = min(len(a), len(b))
    compute(n // 2)

def process(inputs):
    print("Doing complex things with AI....")
    for i in range(len(inputs)):
        for j in range(i + 1, len(inputs)):
            if is_similar(inputs[i], inputs[j]):
                deep_compare(inputs[i], inputs[j])
    print("AI done")
    
    
def main():
    print("Enter your strings (one per line, empty to end):")
    inputs = []
    while True:
        try:
            s = input().strip()
            if not s:
                break
            inputs.append(s)
        except EOFError:
            break

    signal.alarm(3)  # set a timeout
    try:
        process(inputs)
        print("Done processing.")
    finally:
        signal.alarm(0)

if __name__ == "__main__":
    main()
