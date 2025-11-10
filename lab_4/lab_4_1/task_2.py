import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = 5 / (x ** 2 - 9)

fig, ax = plt.subplots(figsize=(10, 5), layout='constrained')
plt.plot(x, y, c="blue", linewidth=2, alpha=0.7)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of a function f(x)")
plt.grid()
ax.set_xlim([-10, 10])
plt.show()