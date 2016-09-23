"""
cryptography.py
Author: Liam S
Credit: none

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
request = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
if request == "e":
    print("encrypt")
elif request == "d":
    print("decrypt")
elif request == "q":
    print("quit")
else:
    print("Did not understand command, try again.")
    
