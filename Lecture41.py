username = input("username : ")
password = input("password : ")
if username == "dome" and password == "123":
    print("done!")
    print("wellcome bro")
    print("We have sell")
    print("1.banana 5 THB")
    print("2.cat 5 THB")
    print("3.alppe 5")
    print("4.hotdog 5 THB")
    print("5.mango 5 THB")
    input1 = int(input("chose : "))
    if input1 == 1:
        print("youchose1.banana")
        numb1 = int(input("how :"))
        print(numb1*5)
    elif input1 == 2:
        print("youchose2.cat")
        numb1 = int(input("how : "))
        print(numb1*5)
    elif input1 == 3:
        print("youchose3.alppe")
        numb1 = int(input("how :"))
        print(numb1 * 5)
    elif input1 == 4:
        print("youchose4.hotdog")
        numb1 = int(input("how :"))
        print(numb1 * 5)
    elif input1 == 5:
        print("Youchose5.mango")
        numb1 = int(input("how :"))
        print(numb1 * 5)
else:
    print("Error")






