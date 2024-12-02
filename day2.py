def is_report_safe(report: list[int]):
    if not (report == sorted(report) or report == sorted(report, reverse=True)):
        return 0
    if len(report) != len(set(report)):
        return 0
    too_big_step = False
    for i in range(0, len(report) - 1):
        if abs(report[i] - report[i + 1]) > 3:
            too_big_step = True
            break
    if too_big_step:
        return 0
    return 1


with open("data/day2.txt", 'r') as file:
    data = file.readlines()

data = [[int(item) for item in line.split()] for line in data]

safe = 0
for report in data:
    safe += is_report_safe(report)

safe_damper = 0
for report in data:
    for i in range(len(report)):
        new_report = report.copy()
        new_report.pop(i)
        if is_report_safe(new_report):
            safe_damper += 1
            break

print(safe)
print(safe_damper)
