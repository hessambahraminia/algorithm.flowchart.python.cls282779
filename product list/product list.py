import os

product_list = []

while True:
    os.system("cls")
    print("1) add product")
    print("2) print all product")
    print("3) find by name")
    print("4) print sum of products")
    print("0) exit")

    option = int(input("enter option :"))
    os.system("cls")

    if option == 1:
        print("add")
        name = input("enter product_name : ")
        price = int(input("enter price : "))
        products = [name, price]
        product_list.append(products)
        print("product saved")

    elif option == 2:
        print("print all\n")
        for p in product_list:
            print("name :", p[0])
            print("price :", p[1])
            print("=" * 50)

    elif option == 3:
        print("find by name\n")
        names = input("enter name to search :")
        found = False
        for p in product_list:
            if p[0].lower() == names.lower():
                print("name :", p[0])
                print("price  :", p[1])
                print("=" * 50)
                found = True
        if not found:
            print("no record")

    elif option == 4:
        print(" sum of products\n")
        sm = 0
        for p in product_list:
            print("name :", p[0])
            print("price  :", p[1])
            sm = sm + p[1]
            print("=" * 50)
        print("\nsum of all products:", sm)

    elif option == 0:
        if (input("are you sure (y/n ?") == "y"):
            print("exit")
            break
    else:
        print("invalid")

    input("\npress enter to continue")