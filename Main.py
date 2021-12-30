import math

loop = True

while loop == True :
    loop2 = True

    num1 = float(input("Number:"))

    print("1.+")
    print("2.-")
    print("3.*")
    print("4./")
    print("5.Exponent")
    print("6.Square Root")
    symbol = input("Symbol:")

    if symbol == "6" :
        answer = math.sqrt(num1)

    else:
        num2 = float(input("Number:"))

    if symbol == "1" :
        answer = num1+num2

    elif symbol == "2" :
        answer = num1-num2

    elif symbol == "3" :
        answer = num1*num2

    elif symbol == "4" :
        answer = num1/num2

    elif symbol == "5" :
        answer = num1**num2

    while loop2 == True :

        print("1.+")
        print("2.-")
        print("3.*")
        print("4./")
        print("5.Exponent")
        print("6.Square Root")
        print("7.end")
        symbol = input("Symbol:")

        if symbol == "7":
            print(str(answer))
            loop2 = False

        elif symbol == "6":
            answer = math.sqrt(answer)

        else:
            num3 = float(input("Number:"))

        if symbol == "1":
            answer = answer+num3

        elif symbol == "2":
            answer = answer-num3

        elif symbol == "3":
            answer = answer*num3

        elif symbol == "4":
            answer = answer/num3

        elif symbol == "5":
            answer = answer**num3
