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
    limits = policy[0:-2].split("-")
    min = int(limits[0])
    max = int(limits[1])
    count = password.count(pwdchar)
    if count >= min and count <= max:
        goodpwdcount += 1
        print(password + " " + pwdchar + " min:" + str(min) + " max:" + str(max))

print(goodpwdcount)
f.close()