# Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the accumulator?
# 1.Iterate through the code, executing instructions, and mark them.
# 2.Mantain the value of the accumulator
# 3.Before every iteration, check if mark is present. If it is, return accumulator

lines = open("advofcode8_input.txt", "r").readlines()
#lines = open("advofcode8_example.txt", "r").readlines()

def run_code(lines):
    accsum = 0
    i = 0

    while i < len(lines):
        if lines[i].endswith("X") : return accsum

        parts = lines[i].split(" ")
        instr = parts[0]
        instrval = int(parts[1])
        
        if instr == "acc":
            accsum += instrval
            lines[i] += "X"
            i += 1
            continue
        elif instr == "jmp":
            lines[i] += "X"
            i += instrval
            continue
        else:
            lines[i] += "X"
            i += 1
            continue

    return accsum

acc = run_code(lines)

print(acc)