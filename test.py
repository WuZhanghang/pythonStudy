import numpy as np
import matplotlib.pyplot as plt

data=np.arange(0,1.1,0.01)
plt.title('line')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim((0,1))
plt.ylim((0,1))
plt.xticks([0,0.2,0.4,0.6,0.8,1])
plt.yticks([0,0.2,0.4,0.6,0.8,1])
plt.plot(data,data**2)
plt.plot(data,data**4)
plt.show()


