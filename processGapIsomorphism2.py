import pandas
import subprocess
import sys

def cyclicGenerators(a_n):
    command = ''
    for i in range(2, a_n//2):
        command += "(" + str(i) + "," + str(a_n-i+1) + ") in g and "
    command += "(" + str(i+1) + "," + str(a_n-i) + ") in g"
    return command

def symmetricGenerators(a_n):
    command = '('
    for i in range(2, a_n//2):
        command += str(i) + ','
    command += str(i+1) + ')('
    for i in range(a_n-1, (a_n+3)//2, -1):
        command +=  str(i) + ','
    command += str(i-1) + ') in g and '
    command += '(' + str(a_n//2-1) + ',' + str(a_n//2) + ')'
    command += '(' + str((a_n+1)//2+1) + ',' + str((a_n+1)//2+2) + ') in g'
    return command


start = int(sys.argv[1])
end = int(sys.argv[2])
filein = "gapcode2.csv"
fileout = "gapisomorphism2.csv"

for index in range(start-2, end-1):
    csv = pandas.read_csv(filein)
    writecsv = pandas.read_csv(fileout)
    line = csv.loc[index]
    outputLine = writecsv.loc[index]
    gapCode = line.gap_code
    gapCommands = ''
    gapSk = '('
    #trivial group
    if gapCode == "g := Group([]);":
        writecsv.loc[index, "isormorphic to b_k"] = "fail"
    else:
        if(str(outputLine["isormorphic to b_k"]) == "nan"):
            a_n = int(line.a_n)
            #value construct gap command to check if all necesarry elements are in the group
            #add elements that generate subgroup c2^k
            gapCommands = cyclicGenerators(a_n)
            gapCommands += ' and ' + symmetricGenerators(a_n) + ';'
            print(gapCommands)
            gapInput = line.gap_code + gapCommands
            proc = subprocess.run(["gap", "-b", "-q", "--quitonbreak", "-x", "999999"],stdout=subprocess.PIPE, input=gapInput, text=True)
            output = proc.stdout.split("\n")
            print(output)
            writecsv = pandas.read_csv(fileout)
            writecsv.loc[index, "a_n"] = line.a_n
            writecsv.loc[index, "isormorphic to b_k"] = output[1]
        
    writecsv.to_csv(fileout, index=False, float_format='%.0f')


