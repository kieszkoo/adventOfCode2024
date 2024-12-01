list_1 = []
list_2 = []
similarity_score = 0
with open("day1.txt", "r") as file:
    for line in file:
        row = line.strip().split("   ")
        list_1.append(int(row[0]))
        list_2.append(int(row[1]))

list_1.sort()
list_2.sort()
for i in list_1:
    count = 0
    for j in list_2:
        if i == j:
            count += 1
    similarity_score += count * i

print(similarity_score)