from cs50 import get_int



while True:
    n = get_int("Give number from 1 to 8:")
    if n >= 1 and n <= 8:
        break

for i in range(1, n + 1):
        print(" " * (n-i) + '#' * i + "  " + '#' * i)