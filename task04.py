while True:
    son=float(input("son:"))
    son2=float(input("Son2:"))
    amal=input("Amal:")
    if amal=="+":
        print(son+son2)
    elif amal=="-":
        print(son-son2) 
    elif amal=="*":
        print(son*son2) 
    elif amal=="/":
        if son2!=0:
            print(son/son2) 
        else:
            print("0 ga bo‘lish mumkin emas!")
    else:
        print("Faqat +, -, *, / kiritish mumkin.")             
    davom = input("Davom etasizmi? (ha/yo‘q): ")
    if davom.lower() != "ha":
        print("Dastur tugadi.")
        break    