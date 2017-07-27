import datetime
import sys
import os

srcfilepath = "c:\\temp\\NIS_CIM_Export_sias_current_20161013_V9.rdf" if len(sys.argv)<2 else sys.argv[1]

sys.stdout.write(datetime.datetime.now().strftime("%I:%M%p") + " Trying to open " + srcfilepath + "...")
sys.stdout.flush()

try:
    srcf = open(srcfilepath, 'rt')

except:
    print("failed" + '\n' + datetime.datetime.now().strftime("%I:%M%p") + " Cannot open file: " + srcfilepath)
    sys.exit(0)

print("ok" + " (" + str(os.stat(srcfilepath).st_size >> 10) + " KB)")

countCimClassNameList = dict()

iLoop = 0
for line in srcf:
    curLine = str(line)

    if " rdf:ID=\"" in curLine:
        cimclass = curLine.split(":")[1].split(" ")[0]

        if cimclass in countCimClassNameList:
            countCimClassNameList[cimclass] += 1
        else:
            countCimClassNameList.update({cimclass:1})

    # Progress indicator
    iLoop = iLoop + 1
    if iLoop % 1000000 == 0:
        sys.stdout.write("-")
        sys.stdout.flush()


srcf.close()

print("\nResult: (" + str(iLoop/1000) + "K lines scanned)")
for c in countCimClassNameList:
    print(c + ":" + str(countCimClassNameList[c]))
print("\nTotal: " + str(sum(countCimClassNameList.values())) + " classes found.")

sys.stdout.write(datetime.datetime.now().strftime("%I:%M%p") + "...done")
sys.stdout.flush()
