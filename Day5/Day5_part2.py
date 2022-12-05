import re
from collections import Counter
from itertools import permutations



with open('input.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n',"") for x in lines]

i=0
for line in lines:
    if(line[1]=='1'):
        break
    i=i+1

n = max([int(x) for x in lines[i].split("  ")])
a = [[]*x for x in range(n+1)]


for j in range(i):
    line = lines[j]
    for x in range(len(line)):
        if(x%4==1 and line[x]!=' '):
            idx = x//4
            a[idx+1].append(line[x])


for j in range(len(a)):
    a[j].reverse()

aa = a.copy()


a2 = []
for line in lines[i+2:]:
    
    line = line.replace(" from ",",")
    line = line.replace(" to ",",")
    line = line.replace("move ","")
    b = line.split(",")
    
    a2.append(b)




for b in a2:
    #print(b)
    i1 = int(b[0])
    i2 = int(b[1])
    i3 = int(b[2])
    curr = aa[i2][len(aa[i2])-i1:len(aa[i2])]
    del aa[i2][len(aa[i2])-i1:len(aa[i2])]
    aa[i3] = aa[i3] + curr
    

print("".join([x[len(x)-1] if len(x)>0 else "" for x in aa]))