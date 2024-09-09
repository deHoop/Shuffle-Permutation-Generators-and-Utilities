def partitionFactors(primeFactors):
    #a number with 1 (prime) factor only has 1 factorization
    if len(primeFactors) == 1:
        return [primeFactors]
    number = primeFactors[0]
    factorList = []
    parts = partitionFactors(primeFactors[1:])
    #for each possible factorization of primeFactors[1:] we will either add primeFactors[0] as a seperate new factor or add it to an already existing factor
    for part in parts:
        for n, factor in enumerate(part):
            #add the first number to all possible factors
            res = sorted(part[:n] +  [number * factor] + part[n+1:])
            if res not in factorList:
                factorList.append(res)
        #add the first number as a new factor  
        res = sorted([number] + part)
        if res not in factorList:
            factorList.append( res )
    return sorted(factorList)