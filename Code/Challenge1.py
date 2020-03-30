"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
import unittest


# SOLUTION
def challenge(n):
    multiples = []
    for number in range(1, n):
        if number % 5 == 0 or number % 3 == 0:
            multiples.append(number)
    return sum(multiples)


# UNIT TESTING
class ChallengeTest(unittest.TestCase):
    def setUp(self):
        self.challenge_elems = ((10, 23), (1000, 233168))
        print("setUp executed !")

    def testCalculation(self):
        for (i, val) in self.challenge_elems:
            self.assertEqual(challenge(i), val)

    def tearDown(self):
        self.challenge_elems = None
        print('tearDown executed !')


if __name__ == "__main__":
    unittest.main()
