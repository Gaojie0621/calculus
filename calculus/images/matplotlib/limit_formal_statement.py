import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def f(x):
    return x**2

a = 1
L = 1
epsilon = 0.2
delta = min(np.sqrt(1 + epsilon) - 1, 1 - np.sqrt(1 - epsilon))

# Create figure with adjusted proportions
plt.figure(figsize=(12, 8))

# Main function plot (zoomed in)
x_vals = np.linspace(a-2*delta, a+2*delta, 400)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, 'b-', linewidth=2.5, label=f'$f(x) = x^2$')

# Create axis spines
ax = plt.gca()
ax.spines['left'].set_position(('data', a-2.1*delta))
ax.spines['bottom'].set_position(('data', L-2.1*epsilon))

# Add epsilon and delta range indicators
plt.axhline(y=L, color='k', linestyle=':', alpha=0.5)
plt.axhline(y=L+epsilon, color='r', linestyle='--', linewidth=1.5)
plt.axhline(y=L-epsilon, color='r', linestyle='--', linewidth=1.5)
plt.axvline(x=a+delta, color='g', linestyle='--', linewidth=1.5)
plt.axvline(x=a-delta, color='g', linestyle='--', linewidth=1.5)

# Fill the epsilon-delta region
plt.fill_between(x_vals, L-epsilon, L+epsilon,
                where=(x_vals > a-delta) & (x_vals < a+delta),
                color='yellow', alpha=0.2)

# Add coordinate markers with values
marker_props = dict(ha='center', va='center', fontsize=10, 
                   bbox=dict(boxstyle='round,pad=0.3', fc='white', alpha=0.8))

plt.text(a-2*delta, L+epsilon, f'$L+ε={L+epsilon:.1f}$', **marker_props)
plt.text(a-2*delta, L-epsilon, f'$L-ε={L-epsilon:.1f}$', **marker_props)
plt.text(a+delta, L-2*epsilon, f'$a+δ={a+delta:.2f}$', **marker_props)
plt.text(a-delta, L-2*epsilon, f'$a-δ={a-delta:.2f}$', **marker_props)

# Add distance arrows with labels
arrow_props = dict(arrowstyle='<->', color='black', linewidth=1.2)

plt.annotate('', xy=(a, L-epsilon), xytext=(a, L+epsilon),
             arrowprops=arrow_props)
plt.text(a+0.05, L, '$2ε$', color='red', ha='left', va='center', fontsize=12)

plt.annotate('', xy=(a-delta, L), xytext=(a+delta, L),
             arrowprops=arrow_props)
plt.text(a, L-0.05, '$2δ$', color='green', ha='center', va='top', fontsize=12)

# Mark important points
plt.scatter([a], [L], color='black', s=100, zorder=5)
plt.text(a, L+0.05, f'$(a,L)=({a},{L})$', ha='center', va='bottom')

# Set axis limits and labels
plt.xlim(a-2*delta, a+2*delta)
plt.ylim(L-2*epsilon, L+2*epsilon)
plt.xlabel('$x$', fontsize=12)
plt.ylabel('$f(x)$', fontsize=12)
plt.title('ε-δ Definition: $\\lim_{x\\to a}f(x)=L$ with $f(x)=x^2$, $a=1$, $L=1$',
          pad=20, fontsize=14)

# Add grid and legend
plt.grid(True, alpha=0.3)
plt.legend(loc='upper left', fontsize=11)

# Save high-quality image
output_path = Path(__file__).parent.parent / "limit_formal_statement.png"
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight', transparent=False)
plt.close()
