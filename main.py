import math


def square(x):
    return x**2;

def logariphm(x):
    return x * math.log2(x)

list_x = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000]
list_y =list(map(square, list_x))

print(list_x)
print(list_y)

list_x1 =[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000]
list_y1 =list(map(logariphm, list_x))
print(list_x1)
print(list_y1)