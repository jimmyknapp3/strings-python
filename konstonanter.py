def rövarspråk(text):
    konsonanter = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    resultat = ""
    for bokstav in text:
        if bokstav in konsonanter:
            resultat += bokstav + "o" + bokstav
        else:
            resultat += bokstav
    return resultat

text = input("Ange text att omvandla till rövarspråket: ")
print("I rövarspråket blir det: ", rövarspråk(text))
