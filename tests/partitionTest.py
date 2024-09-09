import unittest
import partition

class TestPartitionMethods(unittest.TestCase):

    def test_prime(self):
        factors = partition.partitionFactors([3])
        self.assertEqual(factors, [[3]])

    def test_composite_four(self):
        factors = partition.partitionFactors([2,2])
        self.assertEqual(factors, [[2,2], [4]])

    def test_composite_eight(self):
        factors = partition.partitionFactors([2,2,2])
        self.assertEqual(factors, [[2,2,2], [2,4], [8]])

    def test_composite_sixty_six(self):
        factors = partition.partitionFactors([2,3,11])
        self.assertEqual(factors, [[2,3,11], [2,33], [3,22], [6,11], [66]])    

if __name__ == '__main__':
    unittest.main()