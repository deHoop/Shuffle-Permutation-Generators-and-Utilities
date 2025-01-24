import pandas
import subprocess
import sys

gapCommands = [
    "\nSize(g);",
    "\nStructureDescription(g);"
    "\nOrbits(g);",
    "\nIsTransitive(g);",
    "\nTransitiveIdentification(g);",
]

start = int(sys.argv[1])
end = int(sys.argv[2])
filein = "gapcode2.csv"
fileout = "gap.csv"

for index in range(start-2, end-1):
    csv = pandas.read_csv(filein)
    writecsv = pandas.read_csv(fileout)
    line = csv.loc[index]
    gapCode = line.gap_code
    #trivial group
    if gapCode == "g := Group([]);":
        writecsv.loc[index, "a_n"] = line.a_n
        writecsv.loc[index, "group_size"] = "1"
        writecsv.loc[index, "structure_description"] = "1"
    else:
        gapInput = line.gap_code + "".join(gapCommands)
        proc = subprocess.run(
            ["gap", "-b", "-q", "--quitonbreak", "-x", "999999"],
            stdout=subprocess.PIPE, 
            input=gapInput, 
            text=True
        )
        output = proc.stdout.split("\n")
        writecsv = pandas.read_csv(fileout)
        writecsv.loc[index, "a_n"] = line.a_n
        writecsv.loc[index, "group_size"] = output[1]
        writecsv.loc[index, "structure_description"] = output[2].strip("\"")
        writecsv.loc[index, "orbits"] = output[3].strip("\"")
        writecsv.loc[index, "is_transitive"] = output[4].strip("\"")
        writecsv.loc[index, "transitive_degree"] = output[5].strip("\"")
    writecsv.to_csv(fileout, index=False, float_format='%.0f')
