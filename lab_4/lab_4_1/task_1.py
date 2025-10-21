import numpy as np
import matplotlib.pyplot as plt

x_degs = np.linspace(-360, 360, 200)
x_radians = np.radians(x_degs)
y_1 = np.exp(np.cos(x_radians)) + np.log(np.cos(0.6 * x_radians) ** 2 + 1) * np.sin(x_radians)
y_2 = -np.log((np.cos(x_radians) + np.sin(x_radians)) ** 2 + 2.5) + 10

fig, ax = plt.subplots(figsize=(10, 5), layout='constrained')
plt.plot(x_degs, y_1, label="f(x)", c="orange", linewidth=3, alpha=0.8)
plt.plot(x_degs, y_2, label="h(x)", c="green", linewidth=3, alpha=0.8)
plt.xlabel("x, degrees")
plt.ylabel("y")
plt.title("Graph of a function f(x) and h(x)")
plt.grid()
plt.legend()
ax.set_xlim([-360, 360])
ax.set_xticks(np.arange(-360, 361, 60))
plt.show()
