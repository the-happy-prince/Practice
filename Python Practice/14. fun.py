def saveContacts(name, phone, country="India"):
    print("MR. " + name, phone, country, sep="|", end="\n")
    return ("Saved")

op = saveContacts("Prince", "+919798073195")
print(op)