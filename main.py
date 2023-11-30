import time


def ex1():
    n = int(input("Input n: "))
    print(n > 100)
    print("=====================================")


def ex2():
    x = int(input("Input x: "))
    y = int(input("Input y: "))

    if x > y:
        print("x > y")
    elif x < y:
        print("x < y")
    else:
        print("x = y")
    print("=====================================")


def ex3():
    msg = str(input("Input message: "))

    while True:
        if msg == "Spathiphyllum":
            print("Yes - Spathiphyllum is the best plant ever!")
        elif msg == "spathiphyllum":
            print("No, I want a big Spathiphyllum!")
        elif msg == "exit":
            print("=====================================")
            return
        else:
            print(f"Spathiphyllum! Not {msg}")


def ex4():
    coins = float(input("Input coins: "))
    scam = 0

    if coins < 85528:
        scam = (coins * 0.18) + 556.2
    else:
        scam = (coins * 0.32) + 14839.2

    if coins - scam < 0:
        scam = 0

    print(f"Scam: {round(scam, 0)}")
    print("=====================================")


def ex5():
    y = int(input("Input year: "))

    if y < 1982:
        print("Not within the Gregorian calendar period")
    elif y % 4 != 0:
        print("Leap year")
    else:
        print("Common year")

    print("=====================================")


def ex6():
    num = int(input("Input secret number: "))

    while True:
        x = int(input("Input number: "))

        if x == num:
            print("Молодець, магле! Тепер ти вільний")
            return

        print("Ха-ха! Ви застрягли у моїй петлі!")
        print("=====================================")


def ex7():
    for i in range(0, 4, 1):
        print(f"{i} Mississippi")
        time.sleep(1)

    print("Ready or not, here I come!")
    print("=====================================")


def ex8():
    while True:
        msg = str(input("Input msg: "))

        if msg == "chupacabra":
            break

        print("You've successfully left the loop.")
        print("=====================================")


def ex9():
    msg = str(input("Input msg: "))
    msg = msg.upper()

    for i in range(0, len(msg), 1):
        if msg[i] != "A" and msg[i] != "E" and msg[i] != "I" and msg[i] != "O" and msg[i] != "U":
            print(msg[i])

    print("=====================================")


def ex10():
    msg = str(input("Input msg: "))
    msg = msg.upper()
    r = ""

    for i in range(0, len(msg), 1):
        if msg[i] != "A" and msg[i] != "E" and msg[i] != "I" and msg[i] != "O" and msg[i] != "U":
            r += msg[i]

    print(r)
    print("=====================================")


def ex11():
    x = int(input("Input blocks: "))
    sep = 0
    result = 0

    for i in range(1, x, 1):
        if x >= i:
            x -= i
            result += 1

    print(f"The height of the pyramid: {result}")
    print("=====================================")


def ex12():
    c = int(input("Input c: "))
    steps = 0

    while True:
        if c % 2 == 0:
            c /= 2
        else:
            c = 3 * c + 1

        print(c)
        steps += 1

        if c == 1:
            break

    print(f"Steps = {steps}")
    print("=====================================")
