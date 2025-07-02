import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Create figure and axis
plt.figure(figsize=(10, 6))

# Generate x values
x = np.linspace(-2*np.pi, 2*np.pi, 500)

# Plot the function and its derivative
plt.plot(x, np.sin(x), 'b-', linewidth=2, label=r'$y = f(x) = \sin(x)$')
plt.plot(x, np.cos(x), 'r--', linewidth=2, label=r"$y = f'(x) = \cos(x)$")

# Add key features
plt.axhline(0, color='black', linewidth=0.5, alpha=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5, alpha=0.5)  # y-axis

# Mark important points
for n in range(-2, 3):
    plt.axvline(n*np.pi, color='gray', linestyle=':', alpha=0.3)  # π markers
    
# Highlight derivative zeros at sin's extrema
extrema_x = [x0 for x0 in x if abs(np.cos(x0)) < 0.01][::100]
plt.plot(extrema_x, np.sin(extrema_x), 'bo', markersize=8, 
         label="f'(x)=0 at sin(x) extrema")

# Formatting
plt.title("Function and Its Derivative: $f(x) = \sin(x)$ vs $f'(x) = \cos(x)$", pad=20)
plt.xlabel('x')
plt.ylabel('y')
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
           [r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$'])
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right')
plt.tight_layout()

# Save and show
output_path = Path(__file__).parent.parent / "sin_and_derivative.png"
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()