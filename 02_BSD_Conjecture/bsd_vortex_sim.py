import numpy as np
import matplotlib.pyplot as plt

# 1. Define the Elliptic Curve Parameters: y^2 = x^3 + ax + b
# Let's pick a famous one: y^2 = x^3 - x (The congruent number curve)
a, b = -1, 0

def elliptic_curve_field(x, y):
    # This represents the "deviation" from the curve
    # Energy is zero when the point is exactly on the curve
    return np.abs(y**2 - (x**3 + a*x + b))

# 2. Setup the "L-Function" Pressure Grid
res = 400
x_range = np.linspace(-2, 2, res)
y_range = np.linspace(-2, 2, res)
X, Y = np.meshgrid(x_range, y_range)

# 3. Calculate the Potential Field
Z = elliptic_curve_field(X, Y)

# 4. Simulation: Finding "Rational Density"
# We simulate where points "want" to settle
density = np.exp(-Z * 5) # High density where the equation is satisfied

# 5. Visualization
plt.figure(figsize=(12, 8), facecolor='black')

# Plot the "Fluid Flow" around the curve
plt.imshow(np.log(Z + 1), extent=[-2, 2, -2, 2], cmap='magma', origin='lower')

# Overlay the "Rational Points" (Nodes)
# We calculate a few simple rational points manually: (0,0), (1,0), (-1,0)
rational_points = [(0,0), (1,0), (-1,0)]
px, py = zip(*rational_points)
plt.scatter(px, py, color='cyan', s=100, edgecolors='white', label='Rational Nodes')

plt.title("The BSD Landscape: Elliptic Flow and Rational Nodes", color='white', fontsize=15)
plt.xlabel("X (Real Space)", color='white')
plt.ylabel("Y (Imaginary/Flow Space)", color='white')
plt.legend()
plt.axis('off')

print("Mapping the Elliptic Potential...")
plt.show()
