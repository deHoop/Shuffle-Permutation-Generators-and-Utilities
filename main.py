import cycleString
import cycleNotation
import distinctPermutations
import pandas
import primefac
import numpy

def main():
    for n in range(2, 1001):
        generators = distinctPermutations.permutations(n)
        cycles = cycleNotation.cycleNotation(generators, n)
        #now format the cycles as gap code
        code = cycleString.cyclesString(cycles)
        csv = pandas.read_csv("gapcode2.csv")
        csv.loc[n-2, "a_n"] = str(n)
        csv.loc[n-2, "gap_code"] = "g := Group(" + code + ");"
        csv.to_csv("gapcode2.csv", index=False, float_format='%.0f')

def helper(n, axisPermutations):
    factorList = list(primefac.primefac(n))
    array = range(1,n+1)
    reshaped = numpy.reshape(array, newshape=factorList)
    for a, j in enumerate (axisPermutations):
        generators = []        
        for k in j:
            reshapedBack = distinctPermutations.transposeSeq(reshaped, k, n)
            generators.append(reshapedBack)
        cycles = cycleNotation.cycleNotation(generators, n)
        permCycles = cycleNotation.cycleNotation(j, len(factorList), True)
        csv = pandas.read_csv("../gapcode3.csv")
        csv.loc[a, "gap_code"] = "g := Group(" 
            + cycleString.cyclesString(cycles) + ");"
        csv.to_csv("../gapcode3.csv", index=False, float_format='%.0f')

if __name__ == "__main__":
    main()