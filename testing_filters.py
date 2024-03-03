import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


t = np.linspace(0, 1, 1000, False)  # 1 second
sig_1 = np.sin(2*np.pi*10*t)
sig_2 = np.sin(2*np.pi*20*t)
sig = sig_1 + sig_2
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(t, sig)
ax1.plot(t, sig_1, alpha=0.5)
ax1.plot(t, sig_2, alpha=0.5)
ax1.set_title('10 Hz and 20 Hz sinusoids')
ax1.axis([0, 1, -2, 2])

sos = sp.signal.butter(10, 15, 'lp', fs=1000, output='sos')
filtered = sp.signal.sosfilt(sos, sig)
ax2.plot(t, filtered)
ax2.plot(t, sig_1, alpha=0.5)
# ax2.plot(t, sig_2, alpha=0.5)
ax2.set_title('After 15 Hz low-pass filter')
ax2.axis([0, 1, -2, 2])
ax2.set_xlabel('Time [seconds]')
plt.tight_layout()
plt.show()


sig_noise = sig_1 + np.random.normal(0, 0.5, t.size)

fig, (ax3, ax4) = plt.subplots(2, 1, sharex=True)

ax3.plot(t, sig_noise)
ax3.plot(t, sig_1, alpha=0.5)
ax3.set_title('10 Hz with large amounts of noise')
ax3.axis([0, 1, -2, 2])

sos = sp.signal.butter(10, 15, 'lp', fs=1000, output='sos')
filtered = sp.signal.sosfilt(sos, sig_noise)
ax4.plot(t, filtered)
# ax2.plot(t, sig_2, alpha=0.5)
ax4.set_title('After 15 Hz low-pass filter')
ax4.axis([0, 1, -2, 2])
ax4.set_xlabel('Time [seconds]')
plt.tight_layout()
plt.show()