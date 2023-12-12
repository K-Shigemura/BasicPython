a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# TODO
for x in (a, b):
    if x == 1:
        print(f"{x}は素数ではありません")
    elif x == 2:
        print(f"{x}は素数です")
    else:
        for i in range (2, x):
            if x % i == 0:
                print(f"{x}は素数ではありません")
                break
            else:
                if i == x - 1:
                    print(f"{x}は素数です")
    