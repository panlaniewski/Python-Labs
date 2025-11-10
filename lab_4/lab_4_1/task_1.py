import numpy as np
import matplotlib.pyplot as plt

x_degs = np.linspace(-360, 360, 200)
x_radians = np.radians(x_degs)
y_1 = np.exp(np.cos(x_radians)) + np.log(np.cos(0.6 * x_radians) ** 2 + 1) * np.sin(x_radians)
y_2 = -np.log((np.cos(x_radians) + np.sin(x_radians)) ** 2 + 2.5) + 10

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 5), layout='constrained', sharex=True)

ax1.plot(x_degs, y_1, label="f(x)", c="orange", linewidth=3, alpha=0.8)
ax1.set_ylabel("y")
ax1.set_title("Graph of functions f(x) and h(x)")
ax1.grid()
ax1.legend()
ax1.set_xlim([-360, 360])

ax2.plot(x_degs, y_2, label="h(x)", c="green", linewidth=3, alpha=0.8)
ax2.set_xlabel("x, degrees")
ax2.set_ylabel("y")
ax2.grid()
ax2.legend()
ax2.set_xticks(np.arange(-360, 361, 60))

plt.show()