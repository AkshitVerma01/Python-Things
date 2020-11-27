import scipy.stats as st
import math

with open('vermaa26.txt') as f:
    lines = [line.rstrip() for line in f]


lines.pop(0)
less =[]
for i in range(len(lines)):
    lines[i] = lines[i].split(",")
    lines[i][3] = int(lines[i][3]) *0.4536
    if (1200 <= (lines[i][3]) < 1600):
        less.append(lines[i][4])

print(len(less))
print("----")