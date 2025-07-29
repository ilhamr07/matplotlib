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

# 2. membuat plot
plt.plot(t1,y1)

#membuat label harus di bawah plot
title ='Grafik Sinusoidal\n'
rumus = r'$ \mathcal{y} = A.sin(2 \omega t)$'

plt.title(title + rumus)
plt.xlabel('Waktu(detik)')
plt.ylabel('Magnituda(cm)')


# 3. menampilkan plot
plt.show()