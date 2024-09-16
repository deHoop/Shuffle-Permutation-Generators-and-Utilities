import permutations
import cycleString
import cycleNotation
import primePermutations
import pandas

# csv = pandas.read_csv("template_csv.csv")
# csv.to_csv("gap.csv", index=False)

for n in range(127, 1001):
    generators = primePermutations.permutations(n)
    cycles = cycleNotation.cycleNotation(generators, n)
    #now format the cycles as gap code
    code = cycleString.cyclesString(cycles)

    csv = pandas.read_csv("gapcode.csv")
    print(str(n))
    csv.loc[n-2, "a_n"] = str(n)
    csv.loc[n-2, "gap_code"] = "g := Group(" + code + ");"
    csv.to_csv("gapcode.csv", index=False, float_format='%.0f')