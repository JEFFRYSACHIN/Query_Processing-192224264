import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.rand(50) * 1000
plt.scatter(x, y, s=sizes, alpha=0.5, color='blue')
plt.title('Scatter Plot with Variable Sizes')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
