import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

plt.figure(1)
vals = np.random.normal(0, 0.5, 10000)

plt.hist(vals, 50) 

plt.show()

# percentil
np.percentile(vals, 50) # bem próximo ao 0 por ser o meio da dist. normal
np.percentile(vals, 90)
np.percentile(vals, 20)
np.percentile(vals, 10) 

# moments
np.mean(vals) # média
np.var(vals) # variância
sp.skew(vals) # assimetria
sp.kurtosis(vals) # curtose

