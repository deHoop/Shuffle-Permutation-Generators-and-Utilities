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
    reshaped = numpy.reshape(array, newshape=factorList)
    for k in itertools.permutations(range(len(factorList))):
        reshapedBack = transposeSeq(reshaped, k, n)
        if not arreq_in_list(reshapedBack, generators):
            generators.append(reshapedBack)

    return generators

def transposeSeq(shape, axes, n):
    return shape.transpose(axes).reshape(n)
