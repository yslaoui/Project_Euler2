"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
# SOLUTION
import unittest


def challenge(n):
    fibonacci = [1, 2]
    while fibonacci[-1] + fibonacci[-2] < n:
        new = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(new)
    sum_even = 0
    for number in fibonacci:
        if number % 2 == 0:
            sum_even += number
    return (sum_even)


# UNIT TESTING
class ChallengeTest(unittest.TestCase):

    def testCalculation(self):
        self.assertEqual(challenge(4000000), 4613732)

    def tearDown(self):
        self.challenge_elems = None
        print('tearDown executed !')


if __name__ == "__main__":
    unittest.main()
