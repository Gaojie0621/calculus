import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


# Define the function
def f(x):
    return 1 - np.sqrt(1 - x**2)


# Create x values in [-1, 1]
x = np.linspace(-1, 1, 500)

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(x, f(x), 'b-', linewidth=2, label=r'$f(x) = 1 - \sqrt{1 - x^2}$')

# Highlight the endpoints
plt.plot(-1, f(-1), 'ro', markersize=8, label='Endpoint at x=-1')
plt.plot(1, f(1), 'ro', markersize=8, label='Endpoint at x=1')

# Add the full circle for reference (dashed line)
theta = np.linspace(0, 2*np.pi, 100)
plt.plot(np.cos(theta), 1 + np.sin(theta), 'k--', alpha=0.3, label='Full circle $x^2 + (y-1)^2=1$')

# Formatting
plt.title('Continuity of $f(x) = 1 - \sqrt{1 - x^2}$ on $[-1, 1]$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.axis('equal')  # Important for circle proportions
plt.legend()
plt.tight_layout()

# Save image
output_path = Path(__file__).parent.parent / "semicircle_function.png"
output_path.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(output_path, dpi=300)