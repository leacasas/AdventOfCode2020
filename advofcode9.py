# What is the first number that is not equal to the sum of two of the previous 25?

lines = open("advofcode9_input.txt", "r").readlines()
#lines = open("advofcode9_example.txt", "r").readlines()

def find_number(lines, preamble_length):
    
    for i, line in enumerate(lines):
        
        if i < preamble_length:
            continue
        
        number = int(line)
        isvalid = False
        preamble = lines[i - preamble_length : i]

        for preamblenumber in preamble:
            another = number - int(preamblenumber)
            if str(another) + "\n" in preamble:
                isvalid = True
        
        if isvalid == False:
            return number
    
    return -1

found = find_number(lines, 25)

print(found)