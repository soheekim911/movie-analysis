import numpy as np
import pandas as pd
import math
from math import log,e
import csv
import random
import scipy
import pdb

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
   
# 1.Load the data and make 1000 lists which has 500 emotions each.
path = '/Users/sohee/Documents/research_DATA/Shawshank_Entropy/'
data = pd.read_csv(path+'shawshank_FER_entropy.csv', encoding = 'utf-8')

pb = data.red
prob = [float(pb.iloc[11]),float(pb.iloc[12]),float(pb.iloc[13]),float(pb.iloc[14]),float(pb.iloc[15]),float(pb.iloc[16]),float(pb.iloc[17]),float(pb.iloc[18])]
emo_list = ['neutral', 'happy', 'sad', 'surprise', 'fear', 'disgust', 'anger','contempt']
andy_list = []

for j in range(1000):
    new_list= []
    for i in range(500):
        rand = np.random.choice(emo_list,p=prob)
        new_list.append(rand)
    andy_list.append(new_list)
    
for i in range(len(andy_list)):
    print(andy_list[i])

# 2. Count each emotion type in a list x 1000 lists. result is like [133,97, 129, 139, ... 124] elements are 1000.

neutral_count = []
happy_count = []
sad_count = []
surprise_count = []
fear_count = []
disgust_count = []
anger_count = []
contempt_count = [] 

for lst in range(len(andy_list)):
#     print(andy_list[lst])
    neutral_count.append(andy_list[lst].count('neutral'))
    happy_count.append(andy_list[lst].count('happy'))
    sad_count.append(andy_list[lst].count('sad'))
    surprise_count.append(andy_list[lst].count('surprise'))
    fear_count.append(andy_list[lst].count('fear'))
    disgust_count.append(andy_list[lst].count('disgust'))
    anger_count.append(andy_list[lst].count('anger'))
    contempt_count.append(andy_list[lst].count('contempt'))
pdb.set_trace()

# 3. Calculate probability of each emotion type and turn it into entropy
neutral_p = []
happy_p = []
sad_p = []
surprise_p = []
fear_p = []
disgust_p = []
anger_p = []
contempt_p = [] 

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
pdb.set_trace()

andy_entropy = []
#print(neutral_p)
#print(happy_p)
#print(sad_p)
#print(surprise_p)
#print(fear_p)
#print(anger_p)
for i in range(len(neutral_p)):
#	print(type(neutral_p[i]))
#	print(type(happy_p[i]))
#	if type(neutral_p[i]) == None:
#		print(neutral_p[i]
#	elif type(happy_p[i]) == None:
#		print(happy_p[i])
#	elif type(sad_p[i]) == None:
#		print(sad_p[i]) 
#	else:
#		continue
	try:
		andy_entropy.append(neutral_p[i]+happy_p[i]+sad_p[i]+surprise_p[i]+fear_p[i]+disgust_p[i]+anger_p[i]) # disgust&contempt is filled with 'None's only
	except:
		pass
print(andy_entropy)

# Original sample's entropy
neutral_mean = float(pb[0])
happy_mean = float(pb[1])
sad_mean = float(pb[2])
surprise_mean = float(pb[3])
fear_mean = float(pb[4])
disgust_mean = float(pb[5])
anger_mean = float(pb[6])
contempt_mean = float(pb[7])


# 4. Calculate 'single' standard error from 1000 entropies. 
andy_mean_entropy = 1.189740519

sum_errsqr = 0
count = 0
for entropy in andy_entropy:
	print(entropy)
	count += 1
	sum_errsqr +=  errsqr(entropy, andy_mean_entropy)
pdb.set_trace()
total_SE = math.sqrt((1/(1000-1))*sum_errsqr)

print('total_SE = ', total_SE)

'''
f = open('entropy_per_emotion.csv', 'w', encoding='utf-8')
writer = csv.writer(f)
writer.writerow()
for prob in neutral_p:
'''	

