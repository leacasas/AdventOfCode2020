# calculate the amount of distinct answers by group
from collections import Counter

lines = open("advofcode6_input.txt", "r").readlines()
#lines = open("advofcode6_example.txt", "r").readlines()
lines.append("\n")

def get_common_answers(line, i):
    total = 0
    appearances = Counter(line).values()
    for app in appearances:
        if app == i:
            total += 1
    return total

totalsum = 0
templine = ""
templinecount = 0

for line in lines:
    if line != "\n":
        templinecount += 1
        templine += line.replace("\n","")
    else:
        totalsum += get_common_answers(templine, templinecount)
        templinecount = 0
        templine = ""

print(totalsum)