inventory = []
name = input("Hej vad heter du?")
greeting = "Välkommen till min värld [name]. Du vaknar upp efter en lång natts sömn"
greeting = greeting.replace("[name]", name)
print(greeting)
print("Mystiskt nog finner du dig i en hamsters kropp, där du löper över ängarna i jakt på en gyllene maskros.")
print("Du rycker till och fryser i din tanke, tittar du på [maskrosen], eller din mystiska [hamster]-kropp")
choice = input("vad väljer du").lower()
if "hamster" in choice:
    print("I drömlik slowmotion beundrar du den fantastiska fluffigheten, dina sinnen förnimmer havre och damm")
elif "maskros" in choice:
    print("Du skriker inombords som den maskrosallergiker du är, prosit, du stoppar maskrosen i din hamsterpåse")
    inventory.append("maskros")
else:
    print("stavning är inte din starka gren, du fortsätter...")

print("I panik tänker du hur du ska hinna till skolbussen")
buss = input("Vad gör du? börjar [springa] mot vägen eller samla dina [tankar]?")
if buss == "springa":
    x1