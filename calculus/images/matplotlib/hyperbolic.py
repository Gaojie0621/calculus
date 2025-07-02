import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Create figure with 3 subplots
plt.figure(figsize=(15, 5))
x = np.linspace(-3, 3, 400)

# 1. Plot sinh(x) with asymptotes
plt.subplot(1, 3, 1)
plt.plot(x, np.sinh(x), 'b-', linewidth=2, label='sinh(x)')
plt.plot(x, 0.5*np.exp(x), 'c--', label='y=½eˣ')
plt.plot(x, -0.5*np.exp(-x), 'm--', label='y=-½e⁻ˣ')
plt.title('y = sinh(x) with Asymptotes')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.ylim(-5, 5)

# 2. Plot cosh(x) with asymptotes
plt.subplot(1, 3, 2)
plt.plot(x, np.cosh(x), 'r-', linewidth=2, label='cosh(x)')
plt.plot(x, 0.5*np.exp(x), 'c--', label='y=½eˣ')
plt.plot(x, 0.5*np.exp(-x), 'm--', label='y=½e⁻ˣ')
plt.title('y = cosh(x) with Asymptotes')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.ylim(-0.5, 5)

# 3. Plot tanh(x) with horizontal asymptotes
plt.subplot(1, 3, 3)
plt.plot(x, np.tanh(x), 'g-', linewidth=2, label='tanh(x)')
plt.axhline(1, color='gray', linestyle='--', label='y=1')
plt.axhline(-1, color='gray', linestyle='--', label='y=-1')
plt.title('y = tanh(x) with Asymptotes')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.ylim(-1.5, 1.5)

# Save the image
output_path = Path(__file__).parent.parent / "hyperbolic.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()