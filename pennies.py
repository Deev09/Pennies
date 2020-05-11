# Naive algorithm for problem solving
import random
import string

def match(pattern,pattern2,arr):
    M=len(pattern)
    O=len(pattern2)
    N=32
    a=0
    b=0
    for position in range(len(arr)):
        for i in range(N-M+1):
            j=0
            while j<M:
                if arr[position][i+j]!=pattern[j]:
                    break
                j+=1
            if j==M:
                #print('pattern1 found at index',i)
                break
        for m in range(N-O +1):  
            h=0

            while h<O:
                if arr[position][m+h]!=pattern2[h]:
                    break
                h+=1
            if h==O:
                #print('pattern2 found at index,',m)
                break
        if i<m:
            a+=1
            #print('A wins')  
        else:
            b+=1
            #print('B wins')  
    print('Player A wins:',a,'PLayer B wins:',b)

option=['H','T']
listo=[]
for i in range(10):
    listo.append(''.join([random.choice(option) for n in range(32)]))
pattern=input()
pattern2=input()
match(pattern,pattern2, listo)
print(listo)