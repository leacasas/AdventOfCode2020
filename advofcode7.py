# how many colors can, eventually, contain at least one shiny gold bag?
# 1.Count number of items that mention "shiny gold", substract one,
#   sum the number to the total and extract the color. Add the extracted color to the list to check.
# 2.Repeat the step before. 

from collections import Counter

#lines = open("advofcode7_input.txt", "r").readlines()
lines = open("advofcode7_example.txt", "r").readlines()

allcolors = []

def count_bags(bagcolors, lines):
    newbagcolors = []
    found = False

    for bagcolor in bagcolors :

        for line in lines :
            if bagcolor.endswith("s") : bagcolor = bagcolor[:-1]
            if line.startswith(bagcolor) or line.find(bagcolor) == -1: continue
            
            lineparts = line.split("contain");
            newbag = lineparts[0].strip()
            
            if newbag not in allcolors :
                allcolors.append(newbag)
                newbagcolors.append(newbag)

            found = True
    if found :
        count_bags(newbagcolors, lines)
    return

count_bags(["shiny gold bag"], lines)
total = len(Counter(allcolors).keys())
print(total)