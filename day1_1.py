list_1 = []
list_2 = []
difference = 0
with open("day1.txt","r") as file:
    for line in file:
        row = line.strip().split("   ")
        list_1.append(int(row[0]))
        list_2.append(int(row[1]))

list_1.sort()
list_2.sort()

for i in range(len(list_1)):
    difference += abs(list_1[i] - list_2[i])

print(difference)