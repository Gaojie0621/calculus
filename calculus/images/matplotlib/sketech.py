import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Define the function
def f(x):
    return 2 * x**2 / (x**2 - 1)

# Define x values excluding the vertical asymptotes at x = ±1
x1 = np.linspace(-4, -1.01, 500)
x2 = np.linspace(-0.99, 0.99, 500)
x3 = np.linspace(1.01, 4, 500)

# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(x1, f(x1), 'b', label='$y = \\frac{2x^2}{x^2 - 1}$')
plt.plot(x2, f(x2), 'b')
plt.plot(x3, f(x3), 'b')

# Draw the horizontal asymptote y = 2
plt.axhline(y=2, color='red', linestyle='--', label='Horizontal Asymptote $y=2$')

# Draw the vertical asymptotes x = -1 and x = 1
plt.axvline(x=-1, color='green', linestyle='--', label='Vertical Asymptotes $x=\\pm1$')
plt.axvline(x=1, color='green', linestyle='--')

# Mark the local maximum at (0, 0)
plt.plot(0, 0, 'ro', label='Local Maximum (0, 0)')

# Axis settings
plt.ylim(-10, 10)
plt.xlim(-4, 4)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sketch of $y = \\frac{2x^2}{x^2 - 1}$')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.tight_layout()

# Save image
output_path = Path(__file__).parent.parent / "sketch.png"
output_path.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(output_path, dpi=300)
