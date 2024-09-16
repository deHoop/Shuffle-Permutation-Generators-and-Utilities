import pandas
import subprocess
import sys

start = int(sys.argv[1])
length = int(sys.argv[2])

for index in range(start+2, start+length+2):
    csv = pandas.read_csv("gapcode.csv")
    writecsv = pandas.read_csv("gap.csv")
    line = csv.loc[index-4]
    gapCode = line.gap_code
    #trivial group
    if gapCode == "g := Group([]);":
        writecsv.loc[index, "a_n"] = line.a_n
        writecsv.loc[index, "group_size"] = "1"
        writecsv.loc[index, "structure_description"] = "1"
    else:
        gapInput = line.gap_code + "\nSize(g);\nStructureDescription(g);"
        proc = subprocess.run(["gap", "-b", "-q", "--quitonbreak", "-x", "999999"],stdout=subprocess.PIPE, input=gapInput, text=True)
        output = proc.stdout.split("\n")
        writecsv = pandas.read_csv("gap.csv")
        writecsv.loc[index, "a_n"] = line.a_n
        writecsv.loc[index, "group_size"] = output[1]
        writecsv.loc[index, "structure_description"] = output[2].strip("\"")
    writecsv.to_csv("gap.csv", index=False, float_format='%.0f')
