# Naive algorithm for problem solving
import random
import string

def match(pattern,pattern2,arr):
    A_sequence=len(pattern)
    B_sequence=len(pattern2)
    random_string=32
    player_a=0
    player_b=0
    for position in range(len(arr)):
        for indexA in range(random_string-A_sequence+1):
            j=0
            while j<A_sequence:
                if arr[position][indexA+j]!=pattern[j]:
                    break
                j+=1
            if j==A_sequence:
                #print('pattern1 found at index',i)
                break
        for indexB in range(random_string-B_sequence +1):  
            h=0

            while h<B_sequence:
                if arr[position][indexB+h]!=pattern2[h]:
                    break
                h+=1
            if h==B_sequence:
                #print('pattern2 found at index,',m)
                break
        if indexA<indexB:
            player_a+=1
            #print('A wins')  
        else:
            player_b+=1
            #print('B wins')  
    print('Player A wins:',player_a,'PLayer B wins:',player_b)

option=['H','T']
listo=[]
for i in range(10):
    listo.append(''.join([random.choice(option) for n in range(32)]))
pattern=input()
pattern2=input()
match(pattern,pattern2, listo)
print(listo)