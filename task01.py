from random import randint
son=randint(1,20)
while True: 
    taxmin = int(input("1 dan 20 gacha son kiriting: "))

    if taxmin < son:
        print("Katta son")
    elif taxmin > son:
        print("Kichik son")
    else:
        print("Topildi")
        break  