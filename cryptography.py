"""
cryptography.py
Author: Liam S
Credit: Vinzent for helping with a loop problem and smartness

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
        newestfinalList = []
        newfinalList = []
        charList = list(message)
        keyList = list(key)
        for b in charList:
            blankList.append(associations.find(b))
        for c in keyList:
            newblankList.append(associations.find(c))
        length = len(blankList)
        length2 = len(newblankList)
        newnewblankList = newblankList
        if length2 < length:
            newnewblankList = newnewblankList+newblankList
        length5 = len(newnewblankList)
        if length5 > length:
            del newnewblankList[length+1:]
        counter = 0
        while counter < length:
            finalList.append(blankList[counter]+newnewblankList[counter])
            counter += 1
        for y in finalList:
            if y > 84:
                y = y - 84
            newestfinalList.append(y)
        for z in newestfinalList:
            newfinalList.append(associations[z])
        print("".join(newfinalList))
        request = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
    elif request == "d":
        answered = True
        message = str(input("Message: "))
        key = str(input("Key: "))
        newblankList = []
        blankList = []
        finalList = []
        newestfinalList = []
        newfinalList = []
        charList = list(message)
        keyList = list(key)
        for b in charList:
            blankList.append(associations.find(b))
        for c in keyList:
            newblankList.append(associations.find(c))
        length = len(blankList)
        length2 = len(newblankList)
        newnewblankList = newblankList
        if length2 < length:
            newnewblankList = newnewblankList+newblankList
        length5 = len(newnewblankList)
        if length5 > length:
            del newnewblankList[length+1:]
        counter = 0
        while counter < length:
            finalList.append(blankList[counter]-newnewblankList[counter])
            counter += 1
        for y in finalList:
            if y > 84:
                y = y - 84
            newestfinalList.append(y)
        for z in newestfinalList:
            newfinalList.append(associations[z])
        print("".join(newfinalList))
        request = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
    elif request == "q":
        print("Goodbye!")
        answered = False
    else:
        print("Did not understand command, try again.")
        request = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))