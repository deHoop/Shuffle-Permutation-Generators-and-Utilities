import primefac
import partition
import numpy
import itertools
import more_itertools

def arreq_in_list(myarr, list_arrays):
    return next((True for elem in list_arrays if numpy.array_equal(elem, myarr)), False)


def permutations(n):
    factorList = list(primefac.primefac(n))

    generators = []
    array = range(1,n+1)

    #reshape to dimensions of a factorization j
    reshaped = numpy.reshape(array, newshape=factorList)
    for k in itertools.permutations(range(len(factorList))):
        #transpose to every compatible shape which is every possible permutation of the axes
        transposed = numpy.transpose(reshaped, axes=k)
        #reshape back
        reshapedBack = numpy.reshape(transposed, n)
        if not arreq_in_list(reshapedBack, generators):
            generators.append(numpy.reshape(transposed, n))

    return generators