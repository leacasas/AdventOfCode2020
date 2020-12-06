# calculate the amount of distinct answers by group
from collections import Counter

lines = open("advofcode6_input.txt", "r").readlines()
#lines = open("advofcode6_example.txt", "r").readlines()
lines.append("\n")

def get_distinct_answers(line):
    return len(Counter(line).keys())

totalsum = 0
templine = ""

for line in lines:
    if line != "\n":
        templine += line.replace("\n","")
    else:
        totalsum += get_distinct_answers(templine)
        templine = ""

print(totalsum)