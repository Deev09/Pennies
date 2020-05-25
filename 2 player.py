# Naive algorithm for problem solving
import random
import string
import matplotlib.pyplot as plt
import numpy as np

def main():
    trial=0
    while True and trial<3 :
        trial+=1
        match(pattern, pattern2, supreme)
    print(supreme)
def match(pattern,pattern2, listo):
    arr=[]

    match.player_a=0
    match.player_b=0
    option=['H','T']
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
                #print('pattern1 found at index',i)
                break
        for indexB in range(random_string-B_sequence +1):  
            h=0

            while h<B_sequence:
                if arr[position][indexB+h]!=pattern2[h]:
                    break
                h+=1
            if h==B_sequence:
                #print('pattern2 found at index,',indexB)
                break
        if indexA<indexB:
            match.player_a+=1
            #print('A wins',match.player_a)  
        else:
            match.player_b+=1
            #print('B wins',match.player_b)  
    print('Player A wins:',match.player_a,'PLayer B wins:',match.player_b)
    a=[match.player_a, match.player_b]
    supreme.append(a)
    


    



supreme=[]
pattern=input()
pattern2=input()

match(pattern,pattern2,supreme)



players=['player a {}'.format(pattern), 'player b {}'.format(pattern2)]
values=[match.player_a,match.player_b]
plt.figure(figsize=(9, 3))
plt.bar(players, values)
plt.show()
if __name__ == '__main__': main()


labels = ['1', '2', '3', '4']
PlayerA = [supreme[0][0],supreme[1][0], supreme[2][0], supreme[3][0]]
PlayerB = [supreme[0][1],supreme[1][1], supreme[2][1], supreme[3][1]]
x = np.arange(len(labels))  # the label locations
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, PlayerA, width, label='Player a')
rects2 = ax.bar(x + width/2, PlayerB, width, label='Player b')
ax.set_ylabel('Scores')
ax.set_title('Match scores by A and B')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()
