import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Define the function
def f(x):
    return np.sqrt(2*x**2 + 1) / (3*x - 5)

# Create figure
plt.figure(figsize=(10, 6))

# Generate x values (avoiding the vertical asymptote)
x_left = np.linspace(-10, 5/3 - 0.1, 500)
x_right = np.linspace(5/3 + 0.1, 10, 500)

# Plot the function
plt.plot(x_left, f(x_left), 'b-', label=r'$f(x)=\frac{\sqrt{2x^2+1}}{3x-5}$')
plt.plot(x_right, f(x_right), 'b-')

# Plot asymptotes
plt.axhline(y=np.sqrt(2)/3, color='r', linestyle='--', label=r'$y=\frac{\sqrt{2}}{3}$ (HA)')
plt.axhline(y=-np.sqrt(2)/3, color='r', linestyle='--', label=r'$y=-\frac{\sqrt{2}}{3}$ (HA)')
plt.axvline(x=5/3, color='g', linestyle=':', label=r'$x=\frac{5}{3}$ (VA)')

# Mark special points
plt.plot(0, f(0), 'ko', label=f'f(0)={f(0):.2f}')  # y-intercept

# Formatting
plt.title('Graph of $f(x)=\\frac{\\sqrt{2x^2+1}}{3x-5}$ with Asymptotes')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(-10, 10)
plt.ylim(-2, 2)
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right')

# Save the image
output_path = Path(__file__).parent.parent / "function_with_asymptotes.png"
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()  # Close the figure to free memory