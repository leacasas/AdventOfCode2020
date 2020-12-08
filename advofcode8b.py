# Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). 
# What is the value of the accumulator after the program terminates?
# 0.Try different versions of the algorithm below, always changing one line as explained above:
#   1.Iterate through the code, executing instructions, and mark them.
#   2.Mantain the value of the accumulator
#   3.Before every iteration, check if mark is present. If it is, return accumulator

lines = open("advofcode8_input.txt", "r").readlines()
#lines = open("advofcode8_example.txt", "r").readlines()

def run_code(lines):
    accsum = 0
    i = 0
    visited = []
    reached_end = False

    while i < len(lines):
        if i in visited : return reached_end, accsum

        parts = lines[i].split(" ")
        instr = parts[0]
        instrval = int(parts[1])
        visited.append(i)
        
        if instr == "acc":
            accsum += instrval
            i += 1
            continue
        elif instr == "jmp":
            i += instrval
            continue
        else:
            i += 1
            continue

    reached_end = True
    
    return reached_end, accsum

for i, line in enumerate(lines):
    if line[0] == "a" : continue
    elif line[0] == "n":
        linescopy = lines.copy()
        linescopy[i] = linescopy[i].replace("nop","jmp")
    elif line[0] == "j":
        linescopy = lines.copy()
        linescopy[i] = linescopy[i].replace("jmp","nop")
    found, acc = run_code(linescopy)
    if found:
        print("Reached end of code. Result: " + str(acc))