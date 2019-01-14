from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv
from collections import Counter

path = '/Users/sohee/Documents/research_DATA/Shawshank_Intensity/'
f = open(path + 'arousal_andy.csv', 'r')
reader = csv.reader(f)

lines = []
for line in reader:
    lines.append(line)
# print(lines)

scene_profile = pd.read_csv('scene_profiles.csv')
scene_start = scene_profile['scene_start'].tolist()

    
andy_arousal = [[] for i in range(len(scene_start))]
# print(andy_arousal)
for row_line in lines[1:]: # header 제외한 rows에서 row 한줄씩 뽑기
#     print(row_line)
    frame = int(row_line[0][21:26])
#     print(frame)
    
    for i in range(len(scene_start)):
#         print(scene_start[i])
       
        print(len(scene_start))
        if frame >= scene_start[i] and frame < scene_start[i+1]:
#             pdb.set_trace()
#             print(andy_arousal[i])
#             print(row_line[1])
            andy_arousal[i].append(row_line[1])    

    else:
        pass
    
print(andy_arousal)
