def cycleNotation(generators, n, zeroIndexed=False):
    #format as valid GAP syntax for this we need to write the array permutation as group syntax (1,2,3,4,5,6) -> (1,4,2,5,3,6) = (1)(2,4,5,3,2)(6)
    allCycles = []

    for i in generators:
        cycles = []
        if zeroIndexed:
            todo = list(range(n))
            indexAdjust = 0
        else:
            todo = list(range(1,n+1))
            indexAdjust = 1

        while len(todo) > 0:
            index = todo[0]
            cycle = []
            #if an index is unchanged then we can leave it out of the cycle notation
            if index == i[index-indexAdjust]:
                todo.remove(index)
                continue
            while index != i[index-indexAdjust] and index not in cycle:
                cycle.append(index)
                todo.remove(index)
                index = i[index-indexAdjust]
            if len(cycle) > 0:
                cycles.append(cycle)
        if len(cycles) > 0:
            allCycles.append(cycles)
    return allCycles