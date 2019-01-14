import numpy as np
import pandas as pd
from scipy.stats import entropy
import math
from math import log,e
import csv
import random
import scipy  
# import scikits.bootstrap as bootstrap  

def sh_entropy(p):
    if p != 0:
        return -p * log(p)
    else:
        pass

# n 은 resampling한 횟수, theta b는 resampling 할 때마다 나온 확률로 계산한 엔트로피, theta mean은 원래의 확률로 계산한 엔트로피

def errsqr(theta, mean): 
    if theta != None:
        a = (theta-mean)**2
        return a
    else:
        return 0
 
path = '/Users/sohee/Documents/research_DATA/Shawshank_Entropy/'
data = pd.read_csv(path+'shawshank_FER_entropy.csv', encoding = 'utf-8')

pb = data.skeet
prob = [float(pb.iloc[11]),float(pb.iloc[12]),float(pb.iloc[13]),float(pb.iloc[14]),float(pb.iloc[15]),float(pb.iloc[16]),float(pb.iloc[17]),float(pb.iloc[18])]
emo_list = ['neutral', 'happy', 'sad', 'surprise', 'fear', 'disgust', 'anger','contempt']
skeet_list = []

for j in range(1000):
    new_list= []
    for i in range(500):
        rand = np.random.choice(emo_list,p=prob)
        new_list.append(rand)
    skeet_list.append(new_list)
    
#for i in range(len(tommy_list)):
#    print(brooks_list[i])

neutral_count = []
happy_count = []
sad_count = []
surprise_count = []
fear_count = []
disgust_count = []
anger_count = []
contempt_count = [] 

# 여기는 bootstrap resampling
for lst in range(len(skeet_list)):
#     print(brooks_list[lst])
    neutral_count.append(skeet_list[lst].count('neutral'))
    happy_count.append(skeet_list[lst].count('happy'))
    sad_count.append(skeet_list[lst].count('sad'))
    surprise_count.append(skeet_list[lst].count('surprise'))
    fear_count.append(skeet_list[lst].count('fear'))
    disgust_count.append(skeet_list[lst].count('disgust'))
    anger_count.append(skeet_list[lst].count('anger'))
    contempt_count.append(skeet_list[lst].count('contempt'))

neutral_p = []
happy_p = []
sad_p = []
surprise_p = []
fear_p = []
disgust_p = []
anger_p = []
contempt_p = [] 

# 여기서부터 각 감정의 sample 내에서의 확률 --> entropy 계산
for count in neutral_count:
    neutral_p.append(sh_entropy(count/500))
for count in happy_count:
    happy_p.append(sh_entropy(count/500))
for count in sad_count:
    sad_p.append(sh_entropy(count/500))
for count in surprise_count:
    surprise_p.append(sh_entropy(count/500))
for count in fear_count:
    fear_p.append(sh_entropy(count/500))
for count in disgust_count:
    disgust_p.append(sh_entropy(count/500))
for count in anger_count:
    anger_p.append(sh_entropy(count/500))
for count in contempt_count:
    contempt_p.append(sh_entropy(count/500))

# 원래의 샘플(detect된 씬) 갯수를 적용했을 때의 entropy 값
neutral_mean = float(pb[0])
happy_mean = float(pb[1])
sad_mean = float(pb[2])
surprise_mean = float(pb[3])
fear_mean = float(pb[4])
disgust_mean = float(pb[5])
anger_mean = float(pb[6])
contempt_mean = float(pb[7])

# 여기서부터는 구한 entropy로부터 standard error 계산
neutral_se = []
happy_se = []
sad_se = []
surprise_se = []
fear_se = []
disgust_se = []
anger_se = []
contempt_se = []

print('\n------------neutral에 대한 entropy 값들----------\n')
for ent in neutral_p:
#     print(ent)
    neutral_se.append(errsqr(ent, neutral_mean))
for ent in happy_p:
    happy_se.append(errsqr(ent, happy_mean))
for ent in sad_p:
    sad_se.append(errsqr(ent, sad_mean))
for ent in surprise_p:
    surprise_se.append(errsqr(ent, surprise_mean))
for ent in fear_p:
    fear_se.append(errsqr(ent, fear_mean))
for ent in disgust_p:
    disgust_se.append(errsqr(ent, disgust_mean))
for ent in anger_p:
    anger_se.append(errsqr(ent, anger_mean))
for ent in contempt_p:
    contempt_se.append(errsqr(ent, contempt_mean))
    
print("\n\n----------오차 제곱-----------\n")
print(neutral_se)
total_neutral = math.sqrt((1/(1000-1))*sum(neutral_se))
total_happy = math.sqrt((1/(1000-1))*sum(happy_se))
total_sad = math.sqrt((1/(1000-1))*sum(sad_se))
total_surprise = math.sqrt((1/(1000-1))*sum(surprise_se))
total_fear = math.sqrt((1/(1000-1))*sum(fear_se))
total_disgust = math.sqrt((1/(1000-1))*sum(disgust_se))
total_anger = math.sqrt((1/(1000-1))*sum(anger_se))
total_contempt = math.sqrt((1/(1000-1))*sum(contempt_se))

print('\n\ntotal standard error is:(오차 제곱 sum해서 1/299 곱하고 sqrt)', total_neutral)
print(total_neutral)
print(total_happy) 
print(total_sad) 
print(total_surprise) 
print(total_fear) 
print(total_disgust) 
print(total_anger)
print(total_contempt)

