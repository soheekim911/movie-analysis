import pandas as pd
import csv
import numpy as np

path = '/Users/sohee/Documents/research_DATA/'
face = pd.read_csv(path+'Shawshank_FaceSize/shawshank_scene_facesize.csv')
arousal = pd.read_csv(path+'Shawshank_Intensity/characters_scene_arousal.csv')

andy_face = face['andy_face']
tommy_face = face['tommy_face']
red_face = face['red_face']
norton_face = face['norton_face']
bogs_face = face['bogs_face']
skeet_face = face['skeet_face']

andy_arousal = arousal['andy_arousal']
tommy_arousal = arousal['tommy_arousal']
red_arousal = arousal['red_arousal']
norton_arousal = arousal['norton_arousal']
bogs_arousal = arousal['bogs_arousal']
skeet_arousal = arousal['skeet_arousal']

print(len(andy_face))
print(len(andy_arousal))

andy_corr = andy_face.corr(andy_arousal) 
tommy_corr = tommy_face.corr(tommy_arousal)
red_corr = red_face.corr(red_arousal)
norton_corr = norton_face.corr(norton_arousal)
bogs_corr = bogs_face.corr(bogs_arousal)
skeet_corr = skeet_face.corr(skeet_arousal)

corr_list = [andy_corr, tommy_corr, red_corr, norton_corr, bogs_corr, skeet_corr]
char_list = ['andy', 'tommy', 'red', 'norton', 'bogs', 'skeet']

f = open('correlation_results.txt', 'w', encoding='utf-8')
writer = csv.writer(f)
for char, corr in zip(char_list, corr_list):
	print('Correlation of {} : {}'.format(char, corr))
	writer.writerow('Correlation of {} : {}'.format(char, corr))



