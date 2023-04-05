import numpy as np

M = np.array([[1, 2, 0], [0, 0, 5], [3, -4, 2], [1, 6, 5], [0, 1, 0]])

U, s, W = np.linalg.svd(M)

V = W.T

D = np.zeros_like(M, dtype=float)
D[np.diag_indices(min(M.shape))] = s

print('Матрицы:\n')

print(f'Матрица D:\n{D}')
print(f'Матрица U:\n{U}')
print(f'Матрица V:\n{V}')

ev_norm = max(s)

print(f'Евклидова норма:\n{ev_norm}')

frob_norm = np.linalg.norm(s)

print(f'Норма Фробениуса:\n{frob_norm}')



