# how many colors can, eventually, contain at least one shiny gold bag?
# 1.Count number of items that mention "shiny gold", substract one,
#   sum the number to the total and extract the color. Add the extracted color to the list to check.
# 2.Repeat the step before. 

from collections import Counter

lines = open("advofcode7_input.txt", "r").readlines()
#lines = open("advofcode7_example.txt", "r").readlines()

def count_bags(bagcolor, lines):

    if bagcolor.endswith("s") : bagcolor = bagcolor[:-1]

    bagsum = 0

    for line in lines :

        if not line.startswith(bagcolor) : continue
        
        lineparts = line.split("contain");
        bags = lineparts[1].split(",")

        for bag in bags:
            try:
                mult = int(bag.strip()[0])
                newbagcolor = "".join(i for i in bag if not i.isdigit() and i != "." and i != "\n").strip()
                bagcount = count_bags(newbagcolor, lines)
                bagsum += mult + (mult * bagcount)
            except:
                continue

    return bagsum

total = count_bags("shiny gold bags", lines)

print(total)