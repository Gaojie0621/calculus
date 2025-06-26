import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# Set up figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Common parameters
a = 2
delta = 0.3
x = np.linspace(1, 3, 400)
x_excluded = np.linspace(a-delta, a+delta, 100)

# Positive infinity plot (left)
M = 10
ax1.axhline(M, color='r', linestyle='--', label='y = M')
ax1.axvline(a-delta, color='g', linestyle=':')
ax1.axvline(a+delta, color='g', linestyle=':')
ax1.plot(x, 1/(x-a)**2, 'b-')
ax1.set_ylim(0, M*1.2)
ax1.set_title(r'$\lim_{x\to a}f(x) = \infty$')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Negative infinity plot (right)
N = -10
ax2.axhline(N, color='r', linestyle='--', label='y = N')
ax2.axvline(a-delta, color='g', linestyle=':')
ax2.axvline(a+delta, color='g', linestyle=':')
ax2.plot(x, -1/(x-a)**2, 'b-')
ax2.set_ylim(N*1.2, 0)
ax2.set_title(r'$\lim_{x\to a}f(x) = -\infty$')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Save the image
output_path = Path(__file__).parent.parent / "infinite_limits_precise.png"
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()  # Close the figure to free memory