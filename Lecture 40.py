username = input("username : ")
password = input("password : ")
if username == "admin" and password == "1234":
    print("done!")
    print("---shop---")
    print("1.vat Calculator")
    print("2.price Calculator")
    chose = int(input("chose : "))
    if chose == 1:
        price = int(input("price: "))
        vat = 7
        result = price+(price*7/100)
        print(result)
    elif chose == 2:
        price1 = int(input("price : "))
        price2 = int(input("price : "))
        print(price1+price2)
else:
        print("Error")

