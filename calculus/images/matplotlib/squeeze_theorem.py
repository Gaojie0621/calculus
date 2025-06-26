import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

x = np.linspace(-np.pi/2, np.pi/2, 100)
f = -x**2 +1
g = np.sin(x)/x  # g(x) we want to find limit of
h = x**2 +1

plt.figure(figsize=(10, 5))
plt.plot(x, f, 'r--', label='$f(x)=-x^2 + 1$')
plt.plot(x, g, 'b-', label='$g(x)=\\frac{\\sin x}{x}$')
plt.plot(x, h, 'g--', label='$h(x)=x^2 + 1$')
plt.axhline(y=1, color='k', linestyle=':')
plt.title('Squeeze Theorem Example: $\\lim_{x\\to 0}\\frac{\\sin x}{x}=1$')
plt.legend()
plt.grid(True)

# Save image
output_path = Path(__file__).parent.parent / "squeeze_theorem.png"
output_path.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(output_path, dpi=300)