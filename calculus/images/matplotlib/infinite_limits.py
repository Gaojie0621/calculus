import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set up the figure
plt.figure(figsize=(12, 7))


# Define function with infinite limit at x=2
def f(x):
    return 1/((x-2)**2)


# Generate data
x_left = np.linspace(1, 1.999, 200)
x_right = np.linspace(2.001, 3, 200)

# Plot the function
plt.plot(x_left, f(x_left), 'b-', label='As $x \\to 2^-$')
plt.plot(x_right, f(x_right), 'r-', label='As $x \\to 2^+$')
plt.axvline(x=2, color='k', linestyle='--', alpha=0.5)

# Formatting
plt.title('$\\lim_{x\\to 2}f(x) = \\infty$\n$f(x) \\to \\infty$ as $x \\to 2$', 
          pad=20, fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.ylim(0, 100)
plt.xlim(1, 3)
plt.grid(True, alpha=0.3)
plt.legend()

# Save the image
output_path = Path(__file__).parent.parent / "infinite_limit.png"
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()  # Close the figure to free memory