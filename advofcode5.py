lines = open("advofcode5_input.txt", "r").readlines()

def decode_value(line):
    translated = line.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0")
    return int(translated, 2)

maxseatid = 0
minseatid = 1023

for line in lines:
    row = decode_value(line[:7])
    col = decode_value(line[7:10])
    seatid = row * 8 + col
    if seatid > maxseatid :
        maxseatid = seatid
    if seatid < minseatid :
        minseatid = seatid

print(maxseatid)