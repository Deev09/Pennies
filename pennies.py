# Naive algorithm for problem solving
import random
import string
import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 100, 15

x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Likelihood of winning')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

def match(pattern,pattern2,arr):

    match.player_a=0
    match.player_b=0
    for i in range(8):
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
                
                #print('A wins')  
        else:
            match.player_b+=1
                
                #print('B wins')  
    print('Player A wins:',match.player_a,'PLayer B wins:',match.player_b)
    


    


option=['H','T']
listo=[]


pattern=input()
pattern2=input()

match(pattern,pattern2, listo)



