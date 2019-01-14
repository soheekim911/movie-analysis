import csv 
import numpy as np 
import re
import pdb


path = '/Volumes/Seagate Backup Plus Drive/research_DATA/Shawshank_FER/'
f = open(path + 'shawshank_scene_fer.csv', 'r')
reader = csv.reader(f)

lines = []
for line in reader:
	#pdb.set_trace()
	lines.append(line)


scene_start = [int(line[13]) for line in lines[1:158]] 
andy_fer = [[] for i in range(len(scene_start))]
pdb.set_trace()


for row_line in lines[1:]: # header 제외한 rows에서 row 한줄씩 뽑기
	try:
		frame = int(row_line[0][21:26])
		for i in range(len(scene_start)-1):
			if frame >= scene_start[i] and frame < scene_start[i+1]:
				andy_fer[i].append(row_line[2])
				#skeet_sizes[i].append(int(row_line[3]))
				#skeet_sizes[i][0] += int(row_line[26])
				#skeet_sizes[i][1] += 1
	except ValueError:
		pass

# print(andy_fer)
print(len(andy_fer))

with open('scene_fer_andy.txt', 'w') as f:
    for item in andy_fer:
        f.write("%s\n" % item)


'''
skeet_sizes_mean = []
for i in range(len(skeet_sizes)):
	if skeet_sizes[i][1] == 0:
		val = 0
	else:
		val = skeet_sizes[i][0] / skeet_sizes[i][1]
	#val = np.mean(skeet_sizes[i])
	skeet_sizes_mean.append(val)

for start, mean in zip(scene_start, skeet_sizes_mean):
	print('start scene: {}, skeet mean size: {}'.format(start, mean))
for mean in skeet_sizes_mean:
	print('{}'.format(mean))
'''