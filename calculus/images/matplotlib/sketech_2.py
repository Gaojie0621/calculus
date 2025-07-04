import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Define the function and its derivatives
def f(x):
    return x * np.exp(x)

def f_prime(x):
    return (x + 1) * np.exp(x)

def f_double_prime(x):
    return (x + 2) * np.exp(x)

# Set x values for plotting
x_vals = np.linspace(-5, 2.5, 500)
y_vals = f(x_vals)

# Key points
min_x = -1
min_y = f(min_x)
infl_x = -2
infl_y = f(infl_x)

# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label=r'$f(x) = xe^x$', color='blue')
plt.axhline(0, color='black', linewidth=0.7)  # x-axis
plt.axvline(0, color='black', linewidth=0.7)  # y-axis

# Plot local minimum
plt.plot(min_x, min_y, 'ro', label=f'Local Min ≈ ({min_x}, {min_y:.2f})')

# Plot inflection point
plt.plot(infl_x, infl_y, 'go', label=f'Inflection Point ≈ ({infl_x}, {infl_y:.2f})')

# Labels and legend
plt.title(r"Graph of $f(x) = xe^x$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.ylim(-1, 6)
plt.xlim(-5, 2.5)

# Save image
output_path = Path(__file__).parent.parent / "sketch_2.png"
output_path.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(output_path, dpi=300)
