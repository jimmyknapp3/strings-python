user_input = input("Ange en sträng: ")
count = 0
for tecken in user_input:
    if tecken.lower() in "aeiouyåäö":
        count += 1
print(f"vokaler: {count}")
