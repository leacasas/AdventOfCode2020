# Algorithm steps:
#   1.Read file with policies and passwords
#   2.Keep a count of how many pwd are valid
#       2A. Valid pwds follow their policies (min-max specified char)

f = open("advofcode2_input.txt", "r")
goodpwdcount = 0

for line in f:
    linesplits = line.split(":")
    password = linesplits[1].strip()
    policy = linesplits[0]
    pwdchar = policy[-1]
    indices = policy[0:-2].split("-")

    first = password[int(indices[0]) - 1]
    second = password[int(indices[1]) - 1]
    
    if (first == pwdchar or second == pwdchar) and (first != second):
        goodpwdcount += 1
        print(password + " " + pwdchar + " 1st:" + first + " 2nd:" + second )

print(goodpwdcount)
f.close()