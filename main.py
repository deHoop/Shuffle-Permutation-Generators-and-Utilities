import permutations
import cycleString
import cycleNotation


for n in range(2, 1001):
    generators = permutations.permutations(n)
    cycles = cycleNotation.cycleNotation(generators, n)
    #now format the cycles as gap code
    code = cycleString.cyclesString(cycles)
    with open("gapCode", "a") as file:
        file.write("g := Group(" + code + ");" + "\n")


