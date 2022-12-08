file = open("input.txt","r")

mat = []
vis = []
for line in file.readlines():
    mat.append(line.strip())
    vis.append([1]*len(mat[0]))

for i in range(len(mat)):
    for j in range(len(mat)):
        d = 1
        # look right
        while j+d<len(mat[i])-1 and mat[i][j+d]<mat[i][j]:
            d+=1
        vis[i][j]*=d
        # look left
        d = 1
        while j-d>0 and mat[i][j-d]<mat[i][j]:
            d+=1
        vis[i][j]*=d
        # look down
        d = 1
        while i+d<len(mat)-1 and mat[i+d][j]<mat[i][j]:
            d+=1
        vis[i][j]*=d
        # look up
        d = 1
        while i-d>0 and mat[i-d][j]<mat[i][j]:
            d+=1
        vis[i][j]*=d

best = 0
for i in range(1, len(mat)-1):
    for j in range(1, len(mat[i])-1):
        if vis[i][j] > best:
            best = vis[i][j]
print(best)