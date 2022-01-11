Vectors

#2
import matplotlib.pyplot as plt
import numpy as np

# This code draws the x and y axis as lines.

# plt.axhline(0, c='black', lw=0.5)
# plt.axvline(0, c='black', lw=0.5)
# plt.xlim(-3,3)
# plt.ylim(-4,4)
plt.axhline(0, c='black', lw=0.5)
plt.axvline(0, c='black', lw=0.5)
plt.xlim(-3,3)
plt.ylim(-4,4)

plt.quiver(0, 0, 2, 3, angles='xy', scale_units='xy', scale=1, color='blue')
plt.quiver(0, 0, -2, -3, angles='xy', scale_units='xy', scale=1, color='blue')
plt.quiver(0, 0, 1, 1, angles='xy', scale_units='xy', scale=1, color='gold')
plt.quiver(0, 0, 2, 2, angles='xy', scale_units='xy', scale=1, color='gold')
plt.show()
#3
# This code draws the x and y axis as lines.

# plt.axhline(0, c='black', lw=0.5)
# plt.axvline(0, c='black', lw=0.5)
# plt.xlim(-4,4)
# plt.ylim(-1,4)
plt.axhline(0, c='black', lw=0.5)
plt.axvline(0, c='black', lw=0.5)
plt.xlim(-4,4)
plt.ylim(-1,4)

plt.quiver(0, 0, 3, 0, angles='xy', scale_units='xy', scale=1)
plt.quiver(3, 0, 0, 3, angles='xy', scale_units='xy', scale=1)
plt.quiver(0, 0, 3, 3, angles='xy', scale_units='xy', scale=1, color='green')
plt.show()