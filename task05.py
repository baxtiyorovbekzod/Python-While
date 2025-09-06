count = 0 

while True:
    matn = input("So‘z: ")

    if matn.lower() == "stop":
        break
    else:
        count += 1

print(f"Siz {count} marta matn kiritdingiz.")
