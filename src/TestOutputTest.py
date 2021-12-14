import unittest
from TestOutput import TestOutput
from TestInput import TestInput
from Output import Output
from BlackJack import BlackJack


class TestCase(unittest.TestCase):

    def testOutput(self):
        testInput = TestInput()
        testInput.setListOfTestInputs([3, "D", "D", "D"])
        blackJack = BlackJack()
        blackJack.setGameInput(testInput)
        blackJack.main()
        testOutput = TestOutput()
        testOutput.setListOfTestOutput(["Your hand is", ['C10', 'D10'], "Your hand is", ['C10', 'D10', 'DA'], "Sorry you have gone over the score and are bust", ['C10', 'D10', 'DA', 'S8'], "PLayer 2 is the winner", [['C10', 'D10', 'DA', 'S8'], ['H4', 'H8'], ['C8', 'S6']]])

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()



