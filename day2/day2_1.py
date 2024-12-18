def is_safe(report):
    increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

dane=[]
with open("day2.txt", "r") as file:
    for line in file:
        row = line.strip().split(" ")
        int_row = list(map(int, row))
        dane.append(int_row)

safe_reports_count = sum(1 for report in dane if is_safe(report))
print(safe_reports_count)
