from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = np.loadtxt('11hz.txt')
sns.set(font_scale=1.2)
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
# finding index number of array value
ind = np.where(freqs == 12)
print(ind)
indx = np.where(freqs == 5)
print(indx)
##### limiting array length#######
freq1 = freqs[20:48]
psd1 = psd[20:48]
# highest peak
maxy = max(psd1)
# index of highest peak#
indhig = np.where(psd1 == maxy)
# get frequency of highest peakk #
print("This wave is of Frequency of:", freq1[indhig])
# Plot the power spectrum
sns.set(font_scale=1.2, style='white')
plt.figure(figsize=(8, 4))
plt.plot(freq1, psd1, color='k', lw=2)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power spectral density (V^2 / Hz)')
plt.ylim([0, 30])
plt.title("Welch's periodogram")
plt.xlim([5, 12])
sns.despine()
plt.show()
