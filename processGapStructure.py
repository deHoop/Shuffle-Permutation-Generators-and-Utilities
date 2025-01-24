import pandas
import subprocess
import sys
import re

start = int(sys.argv[1])
end = int(sys.argv[2])
fileout = "gaptable.csv"

for index in range(start-2, end-1):
    csv = pandas.read_csv(fileout)
    line = csv.loc[index]
    structure = line.structure_description
    if(str(structure) != 'nan'):
        x = re.findall("(?:C2 x )+C2", structure)
        outstring = structure
        for match in x:
            leng = len(match) + 3
            val = leng//5
            out = "C2^" + str(val)
            outstring = outstring.replace(match, out, 1)
        print(outstring)
        csv.loc[index, "struct"] = outstring
        csv.to_csv(fileout, index=False, float_format='%.0f')

        
    #csv.to_csv(fileout, index=False, float_format='%.0f')


