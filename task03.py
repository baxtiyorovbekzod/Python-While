bal=0
while True:
    ishora=input("ishora:")

    if ishora=="+":
        bal+=10
        print(f"Ball: {bal}")
    elif ishora=="stop":
        print(f"Umumiy ball:{bal}")
        break    
    else:
        print("Faqat + yoki stop yozing.")