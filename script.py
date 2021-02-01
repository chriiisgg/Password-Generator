import string
import random


chs = string.printable

password_length = int(input("Enter password length : "))

password_gen = random.choices(chs, k=password_length)

password_str = "".join(password_gen)

pass_word = "".join(password_str.split())

print(pass_word)