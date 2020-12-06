filelines = open("advofcode3_input.txt", "r").readlines()

def count_trees(lines, right, down):
    x = 0
    y = 0
    treecount = 0

    for i, line in enumerate(lines):
        if i != y:
            continue
        line = line.strip()
        index = x % len(line)
        x += right
        y += down
        if line[index] == "#":
            treecount += 1

    return treecount

c0 = count_trees(filelines, 1, 1)
c1 = count_trees(filelines, 3, 1)
c2 = count_trees(filelines, 5, 1)
c3 = count_trees(filelines, 7, 1)
c4 = count_trees(filelines, 1, 2)

total = c0 * c1 * c2 * c3 * c4

print(total)