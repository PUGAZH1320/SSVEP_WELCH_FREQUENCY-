import pandas as a
df = a.read_csv('o1_1min1.csv',header=None)
t = df[0]
v = df[1]

from matplotlib import pyplot as pit

fig,ax = pit.subplots(figsize=(10,7))
ax.plot(t,v)