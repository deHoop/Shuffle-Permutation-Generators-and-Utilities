import unittest
import permutations
import numpy

class TestPermutationMethods(unittest.TestCase):

    def test_prime(self):
        perms = permutations.permutations(3)
        numpy.testing.assert_array_equal(perms, [[1,2,3]])

    def test_perfect_square_of_primes(self):
        perms = permutations.permutations(9)
        numpy.testing.assert_array_equal(perms, [[1,2,3,4,5,6,7,8,9], [1,4,7,2,5,8,3,6,9]])

    def test_composite(self):
        perms = permutations.permutations(12)
        numpy.testing.assert_array_equal(perms, [[1,2,3,4,5,6,7,8,9,10,11,12], 
            [ 1,  4,  2,  5,  3,  6,  7, 10,  8, 11,  9, 12],
            [ 1,  2,  3,  7,  8,  9,  4,  5,  6, 10, 11, 12],
            [ 1,  7,  2,  8,  3,  9,  4, 10,  5, 11,  6, 12],
            [ 1,  4,  7, 10,  2,  5,  8, 11,  3,  6,  9, 12],
            [ 1,  7,  4, 10,  2,  8,  5, 11,  3,  9,  6, 12],
            [ 1,  3,  5,  2,  4,  6,  7,  9, 11,  8, 10, 12],
            [ 1,  2,  7,  8,  3,  4,  9, 10,  5,  6, 11, 12],
            [ 1,  3,  5,  7,  9, 11,  2,  4,  6,  8, 10, 12],
            [ 1,  7,  3,  9,  5, 11,  2,  8,  4, 10,  6, 12],
            [ 1,  3,  2,  4,  5,  7,  6,  8,  9, 11, 10, 12],
            [ 1,  2,  5,  6,  9, 10,  3,  4,  7,  8, 11, 12],
            [ 1,  5,  9,  2,  6, 10,  3,  7, 11,  4,  8, 12],
            [ 1,  5,  9,  3,  7, 11,  2,  6, 10,  4,  8, 12]])
  

if __name__ == '__main__':
    unittest.main()