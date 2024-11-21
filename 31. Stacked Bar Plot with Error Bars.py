import numpy as np
import matplotlib.pyplot as plt

means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]
std_dev_men = [4, 3, 4, 1, 5]
std_dev_women = [3, 5, 2, 3, 3]

x = np.arange(len(means_men))
plt.bar(x, means_men, yerr=std_dev_men, label='Men')
plt.bar(x, means_women, yerr=std_dev_women, bottom=means_men, label='Women')
plt.xticks(x, ['G1', 'G2', 'G3', 'G4', 'G5'])
plt.legend()
plt.show()
