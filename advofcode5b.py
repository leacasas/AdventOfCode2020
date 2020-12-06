lines = open("advofcode5_input.txt", "r").readlines()

def decode_value(line):
    translated = line.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0")
    return int(translated, 2)

listofids = list(range(13, 881)) #calculated min and max ids by code

for line in lines:
    row = decode_value(line[:7])
    col = decode_value(line[7:10])
    seatid = row * 8 + col
    listofids.remove(seatid)

print(listofids)