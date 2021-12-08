import unittest
from TestInput import TestInput
from BlackJack import BlackJack


class MyTestCase(unittest.TestCase):


    def testInput(self):
        testInput = TestInput()
        testInput.setListOfTestInputs(["D", "D", "D", 3])
        blackJack = BlackJack()
        blackJack.setGameInput(testInput)
        blackJack.main()

        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
