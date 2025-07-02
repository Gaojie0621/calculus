import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Create x values with wider range and avoid division by zero for tan(x)
x = np.linspace(-2*np.pi, 2*np.pi, 1000)
x_tan = np.linspace(-2*np.pi, 2*np.pi, 1000)
x_tan = x_tan[~np.isclose(np.cos(x_tan), 0, atol=1e-8)]  # Remove points near asymptotes

# Plot asymptotes for tan(x) as red dotted lines
asymptote_positions = np.pi/2 + np.pi * np.arange(-3, 4)  # Positions where cos(x)=0
for pos in asymptote_positions:
    plt.axvline(x=pos, color='red', linestyle=':', linewidth=1)  # red dotted lines

plt.figure(figsize=(14, 10))

# Original functions - Top subplot
plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x), 'b-', linewidth=2, label='sin x')
plt.plot(x, np.cos(x), 'g-', linewidth=2, label='cos x')
plt.plot(x_tan, np.tan(x_tan), 'r-', linewidth=2, label='tan x')

# Highlight key points
for n in range(-2, 3):
    plt.axvline(n*np.pi, color='gray', linestyle=':', alpha=0.5)
    plt.plot(n*np.pi, np.sin(n*np.pi), 'bo', markersize=8)
    plt.plot(n*np.pi, np.cos(n*np.pi), 'go', markersize=8)
    
plt.ylim(-4, 4)
plt.title('Trigonometric Functions', pad=20)
plt.xlabel('x')
plt.ylabel('y')
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
           [r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$'])
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right')

# Their derivatives - Bottom subplot
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x), 'b--', linewidth=2, label="d/dx sin x = cos x")
plt.plot(x, -np.sin(x), 'g--', linewidth=2, label="d/dx cos x = -sin x") 
plt.plot(x_tan, 1/np.cos(x_tan)**2, 'r--', linewidth=2, label="d/dx tan x = sec²x")

# Highlight key points and zeros
for n in range(-2, 3):
    plt.axvline(n*np.pi, color='gray', linestyle=':', alpha=0.5)
    plt.plot(n*np.pi, np.cos(n*np.pi), 'bo', markersize=8)
    plt.plot(n*np.pi, -np.sin(n*np.pi), 'go', markersize=8)
    plt.plot((n+0.5)*np.pi, 0, 'ro', markersize=8)  # tan derivative zeros
    
plt.ylim(-4, 4)
plt.title('Derivatives of Trigonometric Functions', pad=20)
plt.xlabel('x')
plt.ylabel("y'")
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
           [r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$'])
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right')

plt.tight_layout()

# Save the image
output_path = Path(__file__).parent.parent / "trig_funcs_and_derivs.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()