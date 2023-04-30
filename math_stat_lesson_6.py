import numpy as np
import pandas as pd


#Задание 1
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

cov_1 = (zp*ks).mean() - zp.mean()*ks.mean()
print(f'cov1:\n{cov_1}')

cov_2 = np.sum((zp-zp.mean())*(ks-ks.mean())) / 10
print(f'cov2:\n{cov_2}')

print(np.cov(zp, ks, ddof=0)[0][1])

r = cov_1/(zp.std()*ks.std())
print(f'r:\n{cov_2}')

print(np.corrcoef(zp, ks)[0][1])

df = pd.DataFrame({'zp': zp, 'ks': ks})
print(df.corr().loc['zp', 'ks'])

#Задание 2
print("\n")

std = 25**0.5
n = 27
s = 174.2
tl = 1.96

d = tl * std / 27**0.5

print(f'd:\n{d}\n')

print(f'Доверительный интервал: ({s-d:.3f}\t{s+d:.3f})')

