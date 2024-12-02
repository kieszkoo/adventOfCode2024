def is_increasing(lst):
    return all(lst[i] < lst[i+1] for i in range(len(lst) - 1))

def is_decreasing(lst):
    return all(lst[i] > lst[i+1] for i in range(len(lst) - 1))

dane = []
count = 0
with open("day2.txt", "r") as file:
    for line in file:
        row = line.strip().split(" ")
        int_row = list(map(int, row))
        dane.append(int_row)

print(dane)

for i in dane:
    safe = False
    dif = 0
    if is_increasing(i) or is_decreasing(i):
        for j in range(len(i)-1):
            dif = abs(i[j] - i[j+1])
            if (dif <= 3) and (dif >=1):
                safe = True
            else:
                safe = False
                break
    if safe:
        count+=1

print(count)
