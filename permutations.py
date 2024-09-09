import primefac
import partition
import numpy
import itertools

def arreq_in_list(myarr, list_arrays):
    return next((True for elem in list_arrays if numpy.array_equal(elem, myarr)), False)


def permutations(n):
    factors = primefac.primefac(n)
    #get all possible factorizations of n
    factorList = partition.partitionFactors(list(factors))

    generators = []
    array = range(1,n+1)

    for i in factorList:
        #when reshaping we consider every ordering of the factors
        #we do not know yet whether this makes a difference
        for j in itertools.permutations(i):
            #reshape to dimensions of a factorization j
            reshaped = numpy.reshape(array, newshape=j)
            for k in itertools.permutations(range(len(j))):
                #transpose to every compatible shape which is every possible permutation of the axes
                transposed = numpy.transpose(reshaped, axes=k)
                #reshape back
                reshapedBack = numpy.reshape(transposed, n)
                if not arreq_in_list(reshapedBack, generators):
                    generators.append(numpy.reshape(transposed, n))

    return generators