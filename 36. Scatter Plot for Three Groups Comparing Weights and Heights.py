import numpy as np
import matplotlib.pyplot as plt

group1 = {'weights': np.random.rand(10) * 50 + 50, 'heights': np.random.rand(10) * 30 + 150}
group2 = {'weights': np.random.rand(10) * 50 + 60, 'heights': np.random.rand(10) * 30 + 160}
group3 = {'weights': np.random.rand(10) * 50 + 70, 'heights': np.random.rand(10) * 30 + 170}

plt.scatter(group1['weights'], group1['heights'], label='Group 1', color='red')
plt.scatter(group2['weights'], group2['heights'], label='Group 2', color='blue')
plt.scatter(group3['weights'], group3['heights'], label='Group 3', color='green')
plt.title('Weights vs Heights for Three Groups')
plt.xlabel('Weights')
plt.ylabel('Heights')
plt.legend()
plt.show()
