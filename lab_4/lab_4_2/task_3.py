import numpy as np

a = np.array([[-2.0, -8.5, -3.4, 3.5],
              [0, 2.4, 0, 8.2],
              [2.5, 1.6, 2.1, 3],
              [0.3, -0.4, -4.8, 4.6]])

a_inv = np.linalg.inv(a)

b = np.array([[-1.88], [-3.28], [-0.5], [-2.83]])

x = (a_inv @ b).round(1)

print("x1 =", x[0][0])
print("x2 =", x[1][0])
print("x3 =", x[2][0])
print("x4 =", x[3][0])