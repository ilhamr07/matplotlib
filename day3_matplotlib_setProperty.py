import numpy as np
import matplotlib.pyplot as plt

"""
	1. Membuat data
	2. Membuat plot
	3. Menampilkan plot
"""

# 1. Membuat data (sin(2wt + theta))
# camel case
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
	t = np.arange(0,tAkhir,0.1)
	y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
	return t,y

t1,y1 = sinusGenerator(1,1,4,0)
t2,y2 = sinusGenerator(1,1,4,90)
t3,y3 = sinusGenerator(1,1,4,180)

# 2. Membuat plot
dataplot1= plt.plot(t1,y1)
dataplot2 = plt.plot(t2,y2)
dataplot3 = plt.plot(t3,y3)

#disini untuk set properti
plt.setp(dataplot1, color = 'r', linestyle='-', linewidth='0.25')
plt.setp(dataplot2, color = 'y', linestyle='--', linewidth='1')
plt.setp(dataplot3, color = 'b', linestyle='-.', linewidth='2.5')

# 3. Menampilkan plot
plt.show()
