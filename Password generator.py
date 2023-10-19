print("     WELCOME TO PASSWORD GENERATOR       ")

import random

PASSWORD="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_=-{}[]:;"

pass_length=int(input("Enter The length of the password :"))

p="".join(random.sample(PASSWORD,pass_length))

print(" The Generated password is ",p)
