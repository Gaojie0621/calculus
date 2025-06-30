import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Set up the figure and subplots
plt.figure(figsize=(12, 10))

# ========================================
# (a) f(x) = (x² - x - 2)/(x - 2)
# ========================================
plt.subplot(2, 2, 1)
x_a = np.linspace(1, 3, 1000)
x_a = x_a[x_a != 2]  # Remove the discontinuity point
y_a = (x_a**2 - x_a - 2)/(x_a - 2)

plt.plot(x_a, y_a, label=r'$f(x)=\frac{x^2-x-2}{x-2}$')
plt.plot(2, 3, 'ro', markersize=8, markerfacecolor='white', markeredgewidth=1.5)
plt.title("(a) Removable Discontinuity at x=2")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

# ========================================
# (b) f(x) = {1/x² if x≠0, 1 if x=0}
# ========================================
plt.subplot(2, 2, 2)
x_b = np.linspace(-1, 1, 1000)
x_b = x_b[x_b != 0]  # Remove x=0
y_b = 1/x_b**2

plt.plot(x_b, y_b, label=r'$f(x)=\frac{1}{x^2}$ (x≠0)')
plt.plot(0, 1, 'ro', markersize=8)
plt.ylim(0, 10)
plt.title("(b) Infinite Discontinuity at x=0")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

# ========================================
# (c) f(x) = {(x²-x-2)/(x-2) if x≠2, 1 if x=2}
# ========================================
plt.subplot(2, 2, 3)
x_c = np.linspace(1, 3, 1000)
x_c = x_c[x_c != 2]  # Remove x=2
y_c = (x_c**2 - x_c - 2)/(x_c - 2)

plt.plot(x_c, y_c, label=r'$f(x)=\frac{x^2-x-2}{x-2}$ (x≠2)')
plt.plot(2, 3, 'ro', markersize=8, markerfacecolor='white', markeredgewidth=1.5)
plt.plot(2, 1, 'bo', markersize=8)
plt.title("(c) Jump Discontinuity at x=2")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

# ========================================
# (d) f(x) = floor(x) (Greatest Integer Function)
# ========================================
plt.subplot(2, 2, 4)
x_d = np.linspace(-3, 3, 1000)
y_d = np.floor(x_d)

# Plot without vertical lines
for n in range(-3, 3):
    mask = (x_d >= n) & (x_d < n+1)
    plt.plot(x_d[mask], y_d[mask], 'b-', label='_nolegend_')
    plt.plot(n+1, n, 'bo', markersize=8, markerfacecolor='white', markeredgewidth=1.5)

plt.plot(-3, -3, 'bo', markersize=8, markerfacecolor='white', markeredgewidth=1.5)  # First point
plt.title("(d) Greatest Integer Function (Floor)")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend([r'$f(x)=\lfloor x \rfloor$'], handlelength=0)

# Save figure
output_path = Path(__file__).parent.parent / "all_discontinuities.png"
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
