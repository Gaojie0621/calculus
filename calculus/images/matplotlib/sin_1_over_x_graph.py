import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Define x values avoiding 0 to prevent division by zero
x = np.linspace(-0.1, 0.1, 10000)
x = x[x != 0]  # Remove 0 to avoid division error
y = np.sin(1 / x)

# Create the plot
plt.figure(figsize=(10, 4))
plt.plot(x, y, label=r'$\sin\left(\frac{1}{x}\right)$')
plt.axhline(1, color='gray', linestyle='--', linewidth=0.5)
plt.axhline(-1, color='gray', linestyle='--', linewidth=0.5)
plt.axvline(0, color='black', linestyle='--', linewidth=0.8)
plt.title(r'Graph of $f(x) = \sin\left(\frac{1}{x}\right)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.tight_layout()

# Save image
output_path = Path(__file__).parent.parent / "sin_1_over_x_graph.png"
output_path.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(output_path, dpi=300)