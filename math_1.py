import numpy as np
import matplotlib.pyplot as plt

k1 = 1
k2 = 4

y = lambda x, k: np.cos(k*x)

fig = plt.subplots()

x = np.linspace(-3, 3, 100)

plt.plot(x, y(x, k1))
plt.plot(x, y(x, k2))

plt.show()
