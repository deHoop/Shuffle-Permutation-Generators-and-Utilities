def cycleString(cycle):
    return "(" + ",".join(str(s) for s in cycle) + ")"

def multiCycleString(multiCycle):
    return "".join(cycleString(s) for s in multiCycle)

def cyclesString(cycles):
    return "[" + ",".join( multiCycleString(i) for i in cycles) + "]"