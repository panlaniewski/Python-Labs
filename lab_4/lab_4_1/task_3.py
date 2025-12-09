import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(8, 5), layout="constrained")

def create_ellipse(x, y, w, h):
    return patches.Ellipse((x, y), w, h, linewidth=2, edgecolor='black', facecolor='orange')

body = create_ellipse(5, 2, 3.2, 2.5)
ax.add_patch(body)

head = create_ellipse(3, 3, 2.3, 1.8)
ax.add_patch(head)

foot = create_ellipse(3.6, 1, 0.8, 0.8)
ax.add_patch(foot)

foot = create_ellipse(6.2, 1, 0.8, 0.8)
ax.add_patch(foot)

ear = create_ellipse(3.9, 3.7, 0.4, 0.4)
ax.add_patch(ear)

eye = patches.Rectangle((3.1, 3.3), 0.2, 0.02, color='black')
ax.add_patch(eye)

nose = patches.Ellipse((1.85, 3), 0.1, 0.3, linewidth=2, edgecolor='black', facecolor='brown')
ax.add_patch(nose)

tail = create_ellipse(6.6, 2.3, 0.4, 0.4)
ax.add_patch(tail)

ax.set_xlim(0, 8)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
ax.axis('off')  # Эта команда убирает оси
plt.title("Capybara", fontsize=16, fontweight='bold')
plt.show()