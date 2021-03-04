import string
import random


chs = string.printable

while True:
    password_length = input("Enter password length: ")
    try:
        password_length = int(password_length)
        break
    except ValueError:
        print("Invalid length.")

password_gen = random.choices(chs, k=password_length)

password_str = "".join(password_gen)

pass_word = "".join(password_str.split())

print(pass_word)
