# Naive algorithm for problem solving
import random
import string
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter 

def match(pattern,trials,arr):
    for i in range(trials):
        scores=[]
        A_sequence=len(pattern[0])
        random_string=32 
        listo=[]
        option=['H','T']
        for i in range(1):
            listo.append(''.join([random.choice(option) for n in range(32)]))
          
    
        for position in range(len(listo)):
            for i in range(len(pattern)):
                for indexA in range(random_string-A_sequence+1):
                    j=0
                    while j<A_sequence:
                        
                            
                        if listo[position][indexA+j]!=pattern[i][j]:
                            break
                     
                        j+=1
                     
                    if j==A_sequence:
                        #print('pattern1 found at index',indexA)
                        
                        scores.append(indexA)
                        break
                    elif  j>len(listo):
                        indexA=32
                        scores.append(indexA)
                        break
                                   
        #print(listo)          
        print(scores)
        match.winner=scores.index(min(scores))+1
        arr.append(match.winner)
       
        print('player',match.winner,'wins')
    print(arr)
   

supreme=[]

players=[]
n=int(input('How many player?'))
for i in range(n):
    pattern_n=input('input player:')
    players.append(pattern_n)

num=int(input('how many rounds?'))

match(players,num,supreme)

labels = [i for i in range(1,n+1)]
values=[]
for i in labels:
    d=Counter(supreme)
    match=d[i]
    values.append(match)
plt.figure(figsize=(9, 3))
plt.bar(labels, values)
plt.show()
    
