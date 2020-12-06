#Count the number of valid passports - those that have all required fields. Treat cid as optional.

lines = open("advofcode4_input.txt", "r").readlines()
#lines = open("advofcode4_example.txt", "r").readlines()
lines.append("\n") #hack to finish avoid ignoring last item.
goodpassports = 0
templine = ""

for i,line in enumerate(lines):
    if line != "\n":
        templine = templine + line.replace("\n"," ")
    else:
        if (("byr:" in templine) and ("iyr:" in templine) and ("eyr:" in templine) and ("hgt:" in templine) and ("hcl:" in templine) and ("ecl:" in templine) and ("pid:" in templine)):
            goodpassports += 1
        templine = ""

print(goodpassports)