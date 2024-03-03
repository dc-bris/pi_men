import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use('tkAgg')


AU = 1.496E11

radius = 6371E3
sun_radius = 696340E3

x = np.linspace(0.001, 2, 400)

fig, ax = plt.subplots()
ax.plot(x, (radius + sun_radius)/(x*AU))
ax.set(xlim=(0, 2), ylim=(0, 0.25), xlabel='Distance from Sun (AU)', ylabel='Probability of transiting')
ax.grid(True, which='major')
ax.grid(True, which='minor')
ax.minorticks_on()
ax.tick_params(axis='y', which='minor', bottom=False)

plt.show()

