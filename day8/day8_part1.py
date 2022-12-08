file = open("input.txt","r")

mat = []
vis = []
for line in file.readlines():
    mat.append(line.strip())
    vis.append([0]*len(mat[0]))

# visible from the left
for i in range(len(mat)):
    top = 0 # tallest of the row
    for j in range(len(mat[i])):
        if int(mat[i][j]) > top:
            # the current tree is the highest => visible
            top = int(mat[i][j])
            vis[i][j] -= 1

# visible from the right
for i in range(len(mat)):
    top = 0 # tallest of the row
    for j in range(len(mat[i])-1, 0, -1):
        if int(mat[i][j]) > top:
            # the current tree is the highest => visible
            top = int(mat[i][j])
            vis[i][j] -= 1

# visible from the top
for j in range(len(mat[0])):
    top = 0 # tallest of the row
    for i in range(len(mat)):
        if int(mat[i][j]) > top:
            # the current tree is the highest => visible
            top = int(mat[i][j])
            vis[i][j] -= 1

# visible from the bottom
for j in range(len(mat[0])):
    top = 0 # tallest of the row
    for i in range(len(mat)-1,0,-1):
        if int(mat[i][j]) > top:
            # the current tree is the highest => visible
            top = int(mat[i][j])
            vis[i][j] -= 1

# 0s on the edges are considered not visible (0>0 = false)

hidden = 0
for i in range(1, len(mat)-1):
    for j in range(1, len(mat[i])-1):
        if vis[i][j] == 0:
            hidden += 1
print(len(mat)**2-hidden)