"""
cryptography.py
Author: Liam S
Credit: Vinzent fof helping with a loop problem

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
answered = True
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
request = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
while answered == True:
    if request == "e":
        answered = True
        message = str(input("Message: "))
        key = str(input("Key: "))
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
            length2 = len(newblankList)
        counter = 0
        while counter < length:
            finalList.append(blankList[counter]+newblankList[counter])
            counter += 1
        for z in finalList:
            newfinalList.append(associations[z])
        print("".join(newfinalList))
        request = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
    elif request == "d":
        message2 = str(input("Message: "))
        key2 = str(input("Key: "))
        newblankList2 = []
        blankList2 = []
        finalList2 = []
        newfinalList2 = []
        charList2 = list(message2)
        keyList2 = list(key2)
        for b in charList2:
            blankList2.append(associations.find(b))
        for c in keyList2:
            newblankList2.append(associations.find(c))
        length4 = len(blankList2)
        length3 = len(newblankList2)
        while length3 < length4:
            newblankList2 = newblankList2+newblankList2
            length3 = len(newblankList2)
        counter2 = 0
        while counter2 < length4:
            finalList2.append(blankList2[counter2]-newblankList2[counter2])
            counter2 += 1
        for z in finalList2:
            newfinalList2.append(associations[z])
        print("".join(newfinalList2))
        request = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
    elif request == "q":
        print("Goodbye!")
        answered = False
    else:
        print("Did not understand command, try again.")
        request = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))