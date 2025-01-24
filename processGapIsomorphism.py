import pandas
import subprocess
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])
filein = "gapcode2.csv"
fileout = "gapisomorphism.csv"

for index in range(start-2, end-1):
    csv = pandas.read_csv(filein)
    writecsv = pandas.read_csv(fileout)
    line = csv.loc[index]
    gapCode = line.gap_code
    #trivial group
    if gapCode == "g := Group([]);":
        writecsv.loc[index, "isormorphic to b_k"] = "fail"
    else:
        #value k of b_k if g_n is full
        k = (int(line.a_n)-2) // 2
        gapCommands = [
            "\nf := WreathProduct(CyclicGroup(2),SymmetricGroup(" + str(k) + "));",
            "\nIsomorphismGroups(f,g);"
        ]
        gapInput = line.gap_code + "".join(gapCommands)
        proc = subprocess.run(["gap", "-b", "-q", "--quitonbreak", "-x", "999999"],stdout=subprocess.PIPE, input=gapInput, text=True)
        output = proc.stdout.split("\n")
        writecsv = pandas.read_csv(fileout)
        writecsv.loc[index, "a_n"] = line.a_n
        writecsv.loc[index, "isormorphic to b_k"] = output[2]
    writecsv.to_csv(fileout, index=False, float_format='%.0f')
