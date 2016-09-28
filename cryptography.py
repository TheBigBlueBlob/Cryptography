"""
cryptography.py
Author: Liam S
Credit: Vinzent fof helping with a loop problem

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
encrypt = False
decrypt = False
answered = True
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
request = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
while answered == True:
    if request == "e":
        print("encrypt")
        answered = False
        encrypt = True
        message = str(input("Message: "))
        key = str(input("Key: "))
    elif request == "d":
        print("decrypt")
        answered = False
        decrypt = True
        print("Message: " + encodedMessage)
    elif request == "q":
        print("Goodbye!")
        answered = False
    else:
        print("Did not understand command, try again.")
newblankList = []
blankList = []
finalList = []
newfinalList = []
charList = list(message)
keyList = list(key)
for b in charList:
    blankList.append(associations.find(b))
for c in keyList:
    newblankList.append(associations.find(c))
length = len(blankList)
length2 = len(newblankList)
while length2 < length:
    newblankList = newblankList+newblankList
counter = 0
while counter < length:
    finalList.append(blankList[counter]+newblankList[counter])
    counter += 1
for z in finalList:
    newfinalList.append(associations[z])
print("".join(newfinalList))

"""
for b in blankList:
    newblankList.append(associations[b])
print(newblankList)
"""
    
