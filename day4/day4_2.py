f = [list(i) for i in open("day4.txt").read().split("\n")]
total = 0

def xMAS(position, data):
    found = False
    x = position[0]
    y = position[1]

    if x - 1 >= 0 and x + 1 < len(data) and y - 1 >= 0 and y + 1 < len(data[0]):
        if data[x-1][y+1] == "M" and data[x+1][y+1] == "M" and data[x-1][y-1] == "S" and data[x+1][y-1] == "S":
            found = True
        elif data[x-1][y+1] == "M" and data[x-1][y-1] == "M" and data[x+1][y-1] == "S" and data[x+1][y+1] == "S":
            found = True
        elif data[x-1][y-1] == "M" and data[x+1][y-1] == "M" and data[x-1][y+1] == "S" and data[x+1][y+1] == "S":
            found = True
        elif data[x+1][y+1] == "M" and data[x+1][y-1] == "M" and data[x-1][y-1] == "S" and data[x-1][y+1] == "S":
            found = True
        return found

for x in range(len(f)):
    for y in range(len(f[0])):
        if f[x][y] == "A":
            if xMAS((x,y),f):
                total+=1
print(total)