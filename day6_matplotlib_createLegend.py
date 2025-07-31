import numpy as np
import matplotlib.pyplot as plt

"""
	1. Membuat data
	2. Membuat plot
	3. Menampilkan plott
"""

# 1. Membuat data (sin(2wt + theta))
# camel case
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
	t = np.arange(0,tAkhir,0.1)
	y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
	return t,y

t1,y1 = sinusGenerator(1,1,4,0)
t2,y2 = sinusGenerator(1,1,4,90)

#. 2 Membuat plot

plt.plot(t1,y1, label='sin(0)')
plt.plot(t2,y2, label='sin(90)')
plt.legend(loc = 'upper center')#setting posisi legend

# 3. show plot

plt.show()