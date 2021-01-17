import matplotlib.pyplot as plt
import numpy as np
import random

list_randint = []
for i in range(1000):
    list_randint.append(random.randint(0, 101))
#print(list_randint)
array_normal = np.random.normal(50, 15, 1000) #평균 50, 표준편차 15
#print(array_normal)
array_randint = np.array(list_randint)
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax1.hist(array_randint, bins = 20, color = 'red', alpha = 0.3)
ax1.set_title('with random.randint')
ax2 = fig.add_subplot(2, 2, 2)
ax2.hist(array_normal, bins = 20, color = 'blue', alpha = 0.3)
ax2.set_title('with np.random.normal')
plt.plot(1.5, 3.5, -2, 1.6)
plt.show()
