import numpy as np
from scipy.stats import f_oneway

football = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifter = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

football_mean = football.mean()
print("football_mean")
print(football_mean)
print('\n')

hockey_mean = hockey.mean()
print("hockey_mean")
print(hockey_mean)
print('\n')

weightlifter_mean = weightlifter.mean()
print("weightlifter_mean")
print(weightlifter_mean)
print('\n')

Y = np.hstack((football, hockey, weightlifter))
Y_mean = Y.mean()
print("Y_mean")
print(Y_mean)
print('\n')

S2_F = (football_mean - Y_mean)**2 * len(football) + (hockey_mean - Y_mean)**2 * len(hockey) + (weightlifter_mean - Y_mean)**2 * len(weightlifter)
print("S2_F")
print(S2_F)
print('\n')

S2_res = ((football - football_mean)**2).sum() + ((hockey - hockey_mean)**2).sum() + ((weightlifter - weightlifter_mean)**2).sum()
print("S2_res")
print(S2_res)
print('\n')

q2_F = S2_F / (3 - 1)
print("q2_F")
print(q2_F)
print('\n')

q2_res = S2_res / (len(Y) - 3)
print("q2_res")
print(q2_res)
print('\n')

F_H = q2_F / q2_res
print("F_H")
print(F_H)
print('\n')

print(f_oneway(football, hockey, weightlifter))

