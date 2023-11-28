# TODO
def prime_number(n):
    try:
        n = int(n)
    except ValueError as e:
        print("整数を入力してください。")
        print(e)
        return
    if n<= 1:
        print("1より大きい整数を入力してください。")
        return
    for i in range(2, n):
        if n % i ==0:
            return False
        else:
            if i == n-1:
                return True

#メインプログラム
n = input("nの値を入力: ")
print(prime_number(n))