#menggeser axis

import numpy as np
import matplotlib.pyplot as plt

#membuat data
sudut = np.arange(0,360,1)
y = np.sin(np.deg2rad(sudut))

#membuat plot
plt.plot(sudut,y,label='sin(0)',color='b')
plt.legend(loc='lower left')

#setting axis panjang dan lebar dari plot nya
#plt.axis([0,360,-1,1])#xMin,xMax,yMin,yMax

#men set ticks
plt.yticks([-1,-0.5,0,0.5,1])
plt.xticks([0,90,180,270,360])

#membuat label
judul = '_Grafik sinusoidal_'
plt.title(judul)
plt.text(189,1,'magnitudo')
plt.text(355,0.05,'sudut')

#menggeser axis
ax=plt.gca()
ax.spines['left'].set_position(('data',180))
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color(('none'))
ax.spines['top'].set_color(('none'))

#menampilkan plot
plt.show()