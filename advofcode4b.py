lines = open("advofcode4_input.txt", "r").readlines()
#lines = open("advofcode4_example.txt", "r").readlines()
lines.append("\n") #hack to finish avoid ignoring last item.

goodpassports = 0

templine = ""

for i,line in enumerate(lines):
    if line != "\n":
        templine = templine + line.replace("\n"," ")
    else:
        #byr
        byridx = templine.find("byr:")
        if byridx == -1:
            templine = ""
            continue
        else:
            byr = int(templine[byridx+4:byridx+8])
            if byr < 1920 or byr > 2002:
                templine = ""
                continue
        #iyr
        iyridx = templine.find("iyr:")
        if iyridx == -1:
            templine = ""
            continue
        else:
            iyr = int(templine[iyridx+4:iyridx+8])
            if iyr < 2010 or iyr > 2020:
                templine = ""
                continue
        #eyr
        eyridx = templine.find("eyr:")
        if eyridx == -1:
            templine = ""
            continue
        else:
            eyr = int(templine[eyridx+4:eyridx+8])
            if eyr < 2020 or eyr > 2030:
                templine = ""
                continue
        #hgt
        hgtidx = templine.find("hgt:")
        if hgtidx == -1:
            templine = ""
            continue
        else:
            cmidx = templine.find("cm")
            if cmidx != -1 and abs(cmidx - hgtidx) < 8:
                cm = int(templine[hgtidx+4:cmidx])
                if cm < 150 or cm > 193:
                    templine = ""
                    continue
            inidx = templine.find("in")
            if inidx != -1 and abs(inidx - hgtidx) < 8:
                inches = int(templine[hgtidx+4:inidx])
                if inches < 59 or inches > 76:
                    templine = ""
                    continue
            if inidx == -1 and cmidx == -1:
                templine = ""
                continue
        #hcl
        hclidx = templine.find("hcl:#")
        if hclidx == -1:
            templine = ""
            continue
        else:
            try:
                int(templine[hclidx+5:hclidx+11], 16)
            except ValueError as e:
                templine = ""
                continue
        #ecl
        eclidx = templine.find("ecl:")
        if eclidx == -1:
            templine = ""
            continue
        else:
            ecl = templine[eclidx+4:eclidx+7]
            if ecl not in ["amb","blu","brn","gry","grn","hzl","oth"]:
                templine = ""
                continue
        #pid
        pididx = templine.find("pid:")
        if pididx == -1:
            templine = ""
            continue
        else:
            pidend = templine.find(" ", pididx)
            pid = templine[pididx+4:pidend]
            if len(pid) != 9 or not pid.isdigit():
                templine = ""
                continue

        goodpassports += 1
        print("VALID: " + templine)
        templine = ""

print(goodpassports)