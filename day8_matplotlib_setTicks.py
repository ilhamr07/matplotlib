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

#. 2 Membuat plot

plt.plot(t1,y1, label='sin(0)')
plt.plot(t2,y2, label='sin(90)')
#membuat legend
plt.legend()

#men set ticks 
plt.yticks([-1,0,1])
plt.xticks([0,1,2,3,4])

#membuat label
judul = 'sin con tan'
plt.title(judul)

plt.ylabel('magnitudo')
plt.xlabel('waktu(detik)')

#membuat text
plt.text(3,-1,r'$ y = \mathcal{A}.sin(2 \omega t)$',color='r')

# 3. show plot

plt.show()