import numpy as np

f = np.asarray([np.asarray(list(i)) for i in open("day4.txt").read().split("\n")])

total = 0

#left to right and right to left
for i in f:
    s = "".join(i)
    total += s.count("XMAS") + s.count("SAMX")

f = np.rot90(f)

#top to bottom and bottom to top
for i in f:
    s = "".join(i)
    total += s.count("XMAS") + s.count("SAMX")


#get diagonals
diags = [f[::-1,:].diagonal(i) for i in range(-f.shape[0]+1,f.shape[1])]
diags.extend(f.diagonal(i) for i in range(f.shape[1]-1,-f.shape[0],-1))

#diagonals
for i in diags:
    s = "".join(i)
    total += s.count("XMAS") + s.count("SAMX")

print(total)