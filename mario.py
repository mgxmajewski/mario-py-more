from cs50 import get_int



while True:
    user_input = get_int("Give number from 1 to 8:")
    if user_input > 1 and user_input < 8:
        break
