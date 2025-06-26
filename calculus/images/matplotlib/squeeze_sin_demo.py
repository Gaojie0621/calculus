import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Create data points
x = np.linspace(-0.5, 0.5, 1000)
x = x[x != 0]  # Remove x=0
y = x**2 * np.sin(1/x)
upper = x**2
lower = -x**2

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label='$x^2 \sin(1/x)$', alpha=0.7)
plt.plot(x, upper, 'r--', label='$x^2$')
plt.plot(x, lower, 'g--', label='$-x^2$')
plt.scatter(0, 0, color='k', s=50, label='Limit point (0,0)')
plt.title('Squeeze Theorem: $x^2 \sin(1/x)$ bounded by $\pm x^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, alpha=0.3)

# Save figure
output_path = Path(__file__).parent.parent / "squeeze_sin_demo.png"
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()