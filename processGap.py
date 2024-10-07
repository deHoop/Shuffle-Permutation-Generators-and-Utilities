import pandas
import subprocess
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])
file = "../gapcode3.csv"

for index in range(start-2, end-1):
    csv = pandas.read_csv(file)
    writecsv = pandas.read_csv(file)
    line = csv.loc[index]
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
        writecsv = pandas.read_csv(file)
        writecsv.loc[index, "a_n"] = line.a_n
        writecsv.loc[index, "group_size"] = output[1]
        writecsv.loc[index, "structure_description"] = output[2].strip("\"")
    writecsv.to_csv(file, index=False, float_format='%.0f')
