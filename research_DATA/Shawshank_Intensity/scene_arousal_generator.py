from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv
import pdb
import os

path = '/Users/sohee/Documents/research_DATA/Shawshank_Intensity/'

scene_number = []
andy_arousal = []

with open(path + 'shawshank_scene_intensity_hand.csv') as data:
    reader = csv.DictReader(data)
    for row in reader:
        print(int(row['scene_number'])
        scene_number.append(row[0])
        andy_arousal.append(float(row[1]))

fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.title("Happy", fontsize=50)
plt.rcParams["figure.figsize"] = (50,10)

ax1.set_xlabel('Scene Number')
ax1.set_ylabel('Emotional Intensity')
ax1.plot(scene_number, andy_arousal, c='red', marker="s", label='andy')


plt.savefig('andy_scene_inten.png')
plt.show()       
