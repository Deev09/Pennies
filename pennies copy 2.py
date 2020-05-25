# Naive algorithm for problem solving
import random
import string


def match(pattern):

    scores=[]
    A_sequence=len(pattern[0])
    random_string=32
    scoressum=[]    
  
    for position in range(len(listo)):
        for i in range(len(pattern)):
            for indexA in range(random_string-A_sequence+1):
                j=0
                while j<A_sequence:
                    if listo[position][indexA+j]!=pattern[i][j]:
                        break
                    j+=1
                if j==A_sequence:
                    print('pattern1 found at index',indexA)
                    scores.append(indexA)
                    break
           
    print(scores)
        
    print(scoressum)
    print('player',scores.index(min(scores))+1,'wins')
   
listo=[]
option=['H','T']
for i in range(1):
    listo.append(''.join([random.choice(option) for n in range(32)]))


players=[]
n=int(input())
for i in range(n):
    pattern_n=input()
    players.append(pattern_n)

print(listo)
match(players)

print(listo) 

