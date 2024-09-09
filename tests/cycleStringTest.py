import unittest
import permutations
import cycleNotation
import cycleString
import numpy

class TestCycleNotation(unittest.TestCase):

    def test_prime(self):
        n = 3 
        gens = permutations.permutations(n)
        cycles = cycleNotation.cycleNotation(gens, n)
        string = cycleString.cyclesString(cycles)
        self.assertEqual(string, "[]")

    def test_perfect_square_of_primes(self):
        n = 9 
        gens = permutations.permutations(n)
        cycles = cycleNotation.cycleNotation(gens, n)
        string = cycleString.cyclesString(cycles)
        self.assertEqual(string, "[(2,4)(3,7)(6,8)]")

    def test_composite(self):
        n = 12
        gens = permutations.permutations(n)
        cycles = cycleNotation.cycleNotation(gens, n)
        string = cycleString.cyclesString(cycles)
        print(cycles)
        print(string)
        self.assertEqual(string, "[(2,4,5,3)(8,10,11,9),(4,7)(5,8)(6,9),(2,7,4,8,10,11,6,9,5,3),(2,4,10,6,5)(3,7,8,11,9),(2,7,5)(3,4,10,9)(6,8,11),(2,3,5,4)(8,9,11,10),(3,7,9,5)(4,8,10,6),(2,3,5,9,6,11,10,8,4,7),(2,7)(4,9)(6,11),(2,3)(6,7)(10,11),(3,5,9,7)(4,6,10,8),(2,5,6,10,4)(3,9,11,8,7),(2,5,7)(3,9,10,4)(6,11,8)]")  
  

if __name__ == '__main__':
    unittest.main()