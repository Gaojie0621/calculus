import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Create the figure
plt.figure(figsize=(10, 6))


# Define the function (example with different left and right limits)
def f(x):
    return np.where(x < 1, x**2 + 1, -x + 3)


# Generate data points
x_left = np.linspace(0, 0.999, 100)
x_right = np.linspace(1.001, 2, 100)
x_point = np.array([1])

# Plot the function
plt.plot(x_left, f(x_left), 'b-', label='Left side (x→1⁻)')
plt.plot(x_right, f(x_right), 'r-', label='Right side (x→1⁺)')

# Mark the limit points
plt.plot(1, 2, 'bo', markersize=8, label='Left limit (2)')
plt.plot(1, 2, 'bo', fillstyle='none', markersize=12)
plt.plot(1, 2, 'bo', markersize=8)  # Repeat to make hollow point clearer

plt.plot(1, 2, 'ro', markersize=8, label='Right limit (2)')
plt.plot(1, 2, 'ro', fillstyle='none', markersize=12)

# Add dashed lines to show the approach
plt.vlines(1, 0, 3, colors='gray', linestyles='dashed', alpha=0.5)
plt.hlines(2, 0, 1, colors='blue', linestyles='dashed', alpha=0.5)
plt.hlines(2, 1, 2, colors='red', linestyles='dashed', alpha=0.5)

# Add arrows to show direction
plt.annotate('', xy=(0.7, 1.5), xytext=(0.9, 1.9),
             arrowprops=dict(arrowstyle='->', color='blue'))
plt.annotate('', xy=(1.3, 1.7), xytext=(1.1, 1.9),
             arrowprops=dict(arrowstyle='->', color='red'))

# Add labels and title
plt.title('One-Sided Limits Visualization\n$\lim_{x\\to1^-}f(x)=2$ and $\lim_{x\\to1^+}f(x)=2$', pad=20)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.xlim(0, 2)
plt.ylim(0, 3)

# Save image
output_path = Path(__file__).parent.parent / "one_sided_limits.png"
output_path.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(output_path, dpi=300)