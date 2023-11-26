from math import pi
import random
def euclid(a, b):
    q = a // b
    r = a % b
    if r == 0:
        return b
    else:
        return euclid(b, r)

def muttualy_prime(a, b):
    return euclid(a, b) == 1

a = input("a の値を入力: ")
b = input("b の値を入力: ")
print(euclid(int(a), int(b)))

#エクストラ問題
def random_number():
    return int(1000000 * random.random())

def tuple_random_number():
    tuples = list()
    for x in range(100000):
        a = random_number()
        b = random_number()
        tuples.append((a, b))
    return tuples

tuples = tuple_random_number()
count = 0
for a, b in tuples:
    if muttualy_prime(a, b):
        count += 1
print(count / len(tuples))
print(f"6/π^2との差: {abs(count / len(tuples) - 6 / pi**2)}")
