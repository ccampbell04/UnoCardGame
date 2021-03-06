import unittest
from TestOutput import TestOutput
from TestInput import TestInput
from Output import Output
from BlackJack import BlackJack


class TestCase(unittest.TestCase):

    def testFirstOutput(self):
        testInput = TestInput()
        blackJack = BlackJack()
        testOutput = TestOutput()

        testInput.setListOfTestInputs([3, "D", "D", "D"])

        blackJack.setGameInput(testInput)
        blackJack.setGameOutput(testOutput)
        blackJack.main()

        self.assertEqual("Your hand is", testOutput.listOfTestOutputs[0])

    def testFullOutput(self):
        expectedResult = ["Your hand is", ['C10', 'D10'], "Your hand is", ['C10', 'D10', 'DA'],
                          "Sorry you have gone over the score and are bust", ['C10', 'D10', 'DA', 'S8'],
                          "PLayer 2 is the winner", [['C10', 'D10', 'DA', 'S8'], ['H4', 'H8'], ['C8', 'S6']]]

if __name__ == '__main__':
    unittest.main()



