import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#задание 1
df = pd.DataFrame({'zp': [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],\
                   'ks': [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]})

b = (np.mean(df.zp * df.ks) - np.mean(df.zp) * np.mean(df.ks)) / (np.mean(df.zp**2) - np.mean(df.zp) ** 2)
a = np.mean(df.ks) - b * np.mean(df.zp)

print(f'y = {a} + {b}x')

plt.scatter(df.zp, df.ks)
t = np.arange(0, 200, 1)
v = a + b * t

plt.plot(t, v, color='g')
plt.show()

X = df.zp.values.reshape((10, 1))
y = df.ks.values.reshape((10, 1))

print('\n')
print(np.linalg.inv(X.T @ X) @ X.T @ y)

X = df.zp.values.reshape((10, 1))
X = np.hstack([np.ones((10, 1)), X])
y = df.ks.values.reshape((10, 1))

print('\n')
print(np.linalg.inv(X.T @ X) @ X.T @ y)

#задание 2-1

X = df.zp.values
y = df.ks.values

w1 = 0.1
alpha = 1e-6
epsilon = 1
n = X.shape[0]
i = 0

while abs(epsilon) > alpha:
    w_prev = w1
    w1 -= alpha * (2/n) * np.sum((w1 * X - y) * X)
    epsilon = w_prev - w1
    i += 1

print('\n')
print(f'y = {w1} * x. Коэффициент найден за {i} итераций, с точностью {alpha}.')

plt.scatter(df.zp, df.ks)
t = np.arange(0, 200, 1)
v = w1 * t
plt.plot(t, v, color='g')

plt.show()

#задание 2-1

w0 = 442
w1 = 0.1
alpha = 1e-6
epsilon0 = 1
epsilon1 = 1
n = X.shape[0]
i = 0

while abs(epsilon0) > alpha or abs(epsilon1) > alpha:
    w0_prev = w0
    w1_prev = w1
    w1 -= alpha * (2/n) * np.sum((w0 + w1 * X - y) * X)
    w0 -= alpha * (2/n) * np.sum((w0 + w1 * X - y))
    epsilon0 = w0_prev - w0
    epsilon1 = w1_prev - w1
    i += 1

print('\n')
print(f'y = {w0} + {w1} * x. Коэффициент найден за {i} итераций, с точностью {alpha}.')

plt.scatter(df.zp, df.ks)
t = np.arange(0, 200, 1)
v = w0 + w1 * t
plt.plot(t, v, color='g')

plt.show()
