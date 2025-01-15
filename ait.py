from datetime import datetime
namn = input("Vad heter du?")
tid = datetime.now()
if 3 > tid.month > 0 or tid.month > 10:
    print("god jul " + namn)
elif 9 > tid.month > 5:
    print("sommar " + namn)
elif 11 > tid.month > 8:
    print("höst " + namn)
else:
    print("vår " + namn)