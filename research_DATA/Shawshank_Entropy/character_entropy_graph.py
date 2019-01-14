import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import csv

path = '/Users/sohee/Documents/research_DATA/Shawshank_Entropy/'
original_data = pd.read_csv(path + 'shawshank_FER_entropy.csv', header=None).iloc[9:10]
original_entropy = pd.DataFrame(original_data )
# original_entropy.pivot()

entropy_se = pd.read_csv(path +'shawshank_entropy_bootstrap_SE.csv')
# entropy_se = np.genfromtxt(path +'shawshank_entropy_bootstrap_SE.csv', delimiter=',')

print(original_entropy)
print(entropy_se)

x = [5753,3239,1279,889,834,293,282,252,140]
x_label = ['Andy', 'Red', 'Norton', 'Heywood', 'Tommy', 'DA','Bogs', 'Brooks', 'Skeet']
y = original_entropy.iloc[0][1:].tolist()
y = list(map(float, y))
y = [1.298028801,1.189740519,0.848361823,1.636059322,1.026463944,1.319936042,1.539851181,1.527549508,0.979018094]
print(y)

error = np.array(entropy_se['bootstrap_se'].tolist())
error = np.array([0.01123919,0.021863146,0.033749479,0.029958328,0.060970289,0.031086376,0.042651128,0.065093577,0.090626645])
print(error)


fig, ax = plt.subplots()
plt.errorbar(x, y, yerr=1.96*error, fmt='o', capsize=4, color= 'tomato')
plt.xlabel('character', size=15)
plt.ylabel('entropy', size=15)


for i, txt in enumerate(x_label):
    ax.annotate(txt, (x[i], y[i]))


plt.show()