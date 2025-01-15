from random import randint
dealer = randint(1, 10)
color = randint(1, 4)

player_card = int(randint(1, 10))
player_color = int(randint(1, 4))

start = input("vill du börja spelet?")
if start == "ja":
    print(f"Du fick", player_card)
    print(f"Huset fick ", dealer)
    continu = input("vill du ta ett till kort eller avsluta?")
