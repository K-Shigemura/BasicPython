a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
while True:
    q = a // b
    r = a % b
    if r == 0:
        print(f"最大公約数は{b}です")
        break
    else:
        a = b
        b = r