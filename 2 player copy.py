# Naive algorithm for problem solving
import random
import string
import matplotlib.pyplot as plt
import numpy as np


def match(pattern,pattern2,arr):

    match.player_a=0
    match.player_b=0
    for i in range(10):
        arr.append(''.join([random.choice(option) for n in range(32)]))
    
    A_sequence=len(pattern)
    B_sequence=len(pattern2)
    random_string=32
        

        
       
        
    for position in range(len(arr)):
        for indexA in range(random_string-A_sequence+1):
            j=0
            while j<A_sequence:
                if arr[position][indexA+j]!=pattern[j]:
                    break
                j+=1
            if j==A_sequence:
                print('pattern1 found at index',i)
                break
        for indexB in range(random_string-B_sequence +1):  
            h=0

            while h<B_sequence:
                if arr[position][indexB+h]!=pattern2[h]:
                    break
                h+=1
            if h==B_sequence:
                print('pattern2 found at index,',indexB)
                break
        if indexA<indexB:
            match.player_a+=1
            print('A wins',match.player_a)  
        else:
            match.player_b+=1
            print('B wins',match.player_b)  
    print('Player A wins:',match.player_a,'PLayer B wins:',match.player_b)
    


    


option=['H','T']
listo=[]


pattern=input()
pattern2=input()

match(pattern,pattern2, listo)



players=['player a {}'.format(pattern), 'player b {}'.format(pattern2)]
values=[match.player_a,match.player_b]
plt.figure(figsize=(9, 3))
plt.bar(players, values)
plt.show()