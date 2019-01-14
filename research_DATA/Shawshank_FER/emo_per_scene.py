import numpy as np
import pandas as pd
import csv
import os
import pdb


path = '/Volumes/Seagate Backup Plus Drive/research_DATA/Shawshank_FER/AffectNet_whole_results/'

df = pd.read_csv(path + 'scene_emotion_bogs.csv')
# print(df)
print(df['neutral'])
# pdb.set_trace()

columns = ['scene_number','start_frame','bogs']
df['neutral'].to_csv(path+'happy_per_scene.csv',mode='a',columns='bogs',header=False)
	

    # pdb.set_trace()


# happy = pd.read_csv(path + 'happy_per_scene.csv',error_bad_lines=False)
# print(happy)