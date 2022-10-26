import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('7hzz.txt')

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=1.2)

from scipy import signal
# Define sampling frequency and time vector
sf = 250
time = np.arange(data.size) / sf

# Plot the signal
fig, ax = plt.subplots(1, 1, figsize=(12, 4))
plt.plot(time, data, lw=1.5, color='k')
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage')
plt.xlim([time.min(), time.max()])
plt.title('N3 sleep EEG data (F3)')

sns.despine()
plt.show()



# Define window length (4 seconds)
win = 4 * sf
freqs, psd = signal.welch(data, sf, nperseg=win)

#### finding index number of array value
ind = np.where(freqs == 20)
print(ind)

##### limiting array length#######
freq1 = freqs[0:80]
print(freq1)

psd1 = psd[0:80]
print(psd1)


maxy = max(psd1)
print(maxy)

ind1 = np.where(psd1 == maxy)
print(ind1)

x=freq1
y=psd1

fig, ax = plt.subplots()
ax.plot(x,y)

def annot_max(x,y, ax=None):
    xmax = x[np.argmax(y)]
    ymax = y.max()
    text= "x={:.3f}, y={:.3f}".format(xmax, ymax)
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmax, ymax), xytext=(0.94,0.96), **kw)

annot_max(x,y)


ax.set_ylim(freq1.max(),psd1.max())
plt.show()