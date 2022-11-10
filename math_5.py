import random
import matplotlib.pyplot as plt
import numpy as np
import itertools

# #задание 1

print("крутим рулетку ...")

sector = random.randint(1, 37)

if sector in range(1, 18):
    print("выпадение черного")
elif sector in range(19, 36):
    print("выпадение красного")
else:
    print("выпадение зеро")

# задание 2-1

a = 0
b = 0

p_a = 0.5
p_b = 0.5

n = 1000

for i in range(n):
    k = np.random.uniform(0, 10)
    if k > 5:
        a += 1
    else:
        b += 1

print("вероятность события А - ", a/n)
print("вероятность события B - ", b/n)
print("вероятность события A+B - ", (a+b)/n)
print("вероятность события p(A)+p(B) - ", p_a+p_b)

# #задание 2-2

n = 20

x0 = np.random.randn(n)
x1 = np.random.randn(n)
x2 = np.random.randn(n)
x3 = np.random.randn(n)
x4 = np.random.randn(n)
x5 = np.random.randn(n)
x6 = np.random.randn(n)
x7 = np.random.randn(n)
x8 = np.random.randn(n)
x9 = np.random.randn(n)

sum_p = x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9

plt.hist(sum_p)
plt.show()

# #задание 3-1

n1 = 0
n2 = 1000

a1 = np.random.randint(0, 2, n2)
a2 = np.random.randint(0, 2, n2)
a3 = np.random.randint(0, 2, n2)
a4 = np.random.randint(0, 2, n2)

x = a1 + a2 + a3 + a4

for i in range(0, n2):
    if x[i] == 2:
        n1 = n1 + 1


print(n1, n2, n1/n2)
print("P = ", 6 / 2**4)

# #задание 3-2

n1 = 0
n2 = 1000

a1 = np.random.randint(0, 2, n2)
a2 = np.random.randint(0, 2, n2)
a3 = np.random.randint(0, 2, n2)
a4 = np.random.randint(0, 2, n2)
a5 = np.random.randint(0, 2, n2)

x = a1 + a2 + a3 + a4 + a5

for i in range(0, n2):
    if x[i] == 3:
        n1 = n1 + 1


print(n1, n2, n1/n2)

print("P = ", (5*4*3*2 / (3*2*2)) / 2**5)

#задание 4

for p in itertools.permutations('123', 3):
    print(''.join(str(x) for x in p))

for p in itertools.combinations('12345', 3):
    print(''.join(p))

#задание 5
n = 500
p = 0.9
x = np.random.rand(n)
y = p*x + (1 - p)*np.random.rand(n)

#расчет rx
a = (np.sum(x)*np.sum(y) - n*np.sum(x*y))/(np.sum(x)*np.sum(x) - n*np.sum(x*x))
b = (np.sum(y) - a*np.sum(x))/n

A = np.vstack([x, np.ones(len(x))]).T
a1, b1 = np.linalg.lstsq(A, y)[0]

#линейный коэф корреляции
c = np.corrcoef(x, y)

print(a, b)
print(a1, b1)

print(c)

