
parol="python123"
while True:
    parol2=input("Parol kiriting:")
    result=parol.lower()==parol2.lower()
    if result:
        print("Xush kelibsiz!")
        break
    else:
        print("Xato! Qayta urinib ko‘ring.")