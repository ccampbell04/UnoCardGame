import unittest
from src.Uno import Uno
from src.TestOutput import TestOutput
from src.TestInput import TestInput


class UnoTest(unittest.TestCase):
    uno = Uno()
    testOutput = TestOutput()
    testInput = TestInput()
    number_of_players = 2

    def testGenerateDeck(self):
        self.cards = self.uno.generateDeck()
        self.assertEqual(108, len(self.cards))

    def testStartCard(self):
        testDeck = ["R-0", "B-4", "G-7"]
        self.assertEqual("G-7", self.uno.startCard(testDeck))

    def testAbleToPlay(self):
        topCard = "R-1"
        hand = ["B-2", "Y-4", "G-+2"]

        self.assertEqual(False, self.uno.ableToPlay(hand, topCard))

    def testSpecialAbleToPlay(self):
        topCard = "R-+2"
        hand = ["B-2", "B-+2"]

        self.assertEqual(True, self.uno.ableToPlay(hand, topCard))

    def testUserInput(self):
        hand = ["B-5", "G-7", "R-2"]

        self.testInput.setListOfTestInputs([1])
        self.uno.setGameInput(self.testInput)

        self.assertEqual(1, self.uno.userInput(hand))

    def testSplitCard(self):
        card = "B-5"
        self.assertEqual(["B", "5"], self.uno.splitCard(card))

    def testCheckSpecialCards(self):
        card = "W-W"
        index = 0
        hand = ["G-6"]
        deck = ["G-8", "B-2"]
        hands = [["G-6"], ["R-9"]]

        self.testInput.setListOfTestInputs(["B", "2"])
        self.uno.setGameInput(self.testInput)

        self.assertEqual(("B-2", "computer"), self.uno.checkSpecialCard(card, index, hand, deck, hands))

    def testDealTwoCards(self):
        hands=[["B-3"], ["G-2"]]
        index=1
        deck=["G-3", "R-7", "B-5"]

        self.uno.dealTwoCards(hands, index, deck)

        self.assertEqual(3, len(hands[index]))

    def testDealFourCards(self):
        hands=[["B-3"], ["G-2"]]
        index=1
        deck=["G-3", "R-7", "B-5", "G-4"]

        self.uno.dealFourCards(hands, index, deck)

        self.assertEqual(5, len(hands[index]))

    def testUserWildCard(self):
        self.testInput.setListOfTestInputs(["B", "2"])
        self.uno.setGameInput(self.testInput)

        self.assertEqual("B-2", self.uno.userWildCard())

    def testComputerWildCard(self):
        hand=["B-4", "B-3", "G-7", "R-5"]

        self.assertEqual("G-7", self.uno.computerWildCard(hand))

    def testUserTurn(self):
        topCard = "R-1"
        hand = ["B-2", "R-4", "G-3"]
        deck = []
        hands = []
        index = 0

        self.testInput.setListOfTestInputs([2])
        self.uno.setGameInput(self.testInput)
        self.assertEqual(("R-4", False, "computer"), self.uno.userTurn(deck, hand, topCard, hands, index))

    def testUserTurnUno(self):
        topCard = "B-2"
        hand = ["B-1", "G-7"]
        deck = []
        hands = []
        index = 0

        self.testInput.setListOfTestInputs([1])
        self.uno.setGameInput(self.testInput)
        self.uno.setGameOutput(self.testOutput)
        self.uno.userTurn(deck, hand, topCard, hands, index)

        self.assertEqual("Uno!", self.testOutput.listOfTestOutputs[-1])

    def testUserTurnCantPlay(self):
        topCard = "R-1"
        hand = ["B-2", "G-4"]
        deck = ["G-2"]
        hands = []
        index = 0

        self.assertEqual("R-1", self.uno.userTurn(deck, hand, topCard, hands, index)[0])

    def testSameSuitPickUpAndPlay(self):
        topCard = "R-4"
        hand = ["G-1", "B-9"]
        deck = ["R-3"]
        hands = []
        index = 0

        self.assertEqual("R-3", self.uno.userTurn(deck, hand, topCard, hands, index)[0])

    def testSameNumPickUpAndPlay(self):
        topCard = "R-4"
        hand = ["G-1", "B-9"]
        deck = ["G-4"]
        hands = []
        index = 0

        self.assertEqual("G-4", self.uno.userTurn(deck, hand, topCard, hands, index)[0])

    def testCantPlayPickUpWild(self):
        topCard = "B-2"
        hand = ["G-6"]
        index = 0
        hands = [["G-6"], ["R-9"]]
        deck = ["G-8", "W-W"]

        self.testInput.setListOfTestInputs(["G", "6"])
        self.uno.setGameInput(self.testInput)

        self.assertEqual(("G-6", False, "computer"), self.uno.userTurn(deck, hand, topCard, hands, index))

    def testComputerPlaySpecial(self):
        topCard = "R-1"
        hand = ["R-+2"]
        index = 1
        hands = [["R-2"], ["R-+2"]]
        deck = ["B-3", "G-5"]

        self.assertEqual(("R-+2", True, "user"), self.uno.computerTurn(deck, hand, topCard, hands, index))

    def testComputerTurn(self):
        deck = []
        hands = []
        hand = ["B-1", "B-7", "B-9"]
        topCard = "B-6"
        index = 1

        self.assertEqual(("B-9", False, "user"), self.uno.computerTurn(deck, hand, topCard, hands, index))

    def testPlayComputerCard(self):
        possibleMoves = ["R-3", "R-4", "R-7"]
        index = 1
        hand = ["B-3", "R-4", "G-7", "R-3", "R-7"]
        deck = []
        hands = []

        self.assertEqual(("R-7", "user"), self.uno.playComputerCard(possibleMoves, index, hand, deck, hands))

    def testUserCantPlay(self):
        hand = ["R-2"]
        deck = ["B-5"]
        topCard = "B-8"
        index = 0
        hands = []

        self.uno.setGameOutput(self.testOutput)
        self.uno.cantPlay(hand, deck, topCard, index, hands)

        self.assertEqual("New card is valid, playing B-5", self.testOutput.listOfTestOutputs[-1])

    def testComputerCantPlay(self):
        deck = ["W-W"]
        hands = [["B-2"], ["B-3", "B-4"]]
        hand = ["B-3", "B-4"]
        topCard = "G-7"
        index = 1

        self.assertEqual(("B-4", False, "user"), self.uno.computerTurn(deck, hand, topCard, hands, index))

    def testComputerPlaySpecial(self):
        topCard = "R-1"
        hand = ["R-+2"]
        index = 1
        hands = [["R-2"], ["R-+2"]]
        deck = ["B-3", "G-5"]

        self.assertEqual(("R-+2", True, "user"), self.uno.computerTurn(deck, hand, topCard, hands, index))

    def testBestCompMove(self):
        possibleMoves = ["Y-9", "B-+2", "R-S"]

        self.assertEqual(1, self.uno.bestCompMove(possibleMoves))

    def testCheckWinner(self):
        hand = []
        self.assertTrue(self.uno.checkWinner(hand))

    def testCalcLoserPoints(self):
        hands = [[], ["B-9", "W-W"]]
        number_of_players = 2
        expectedOutput = ["Player scored 0", "Computer 1 scored 59"]

        self.uno.setGameOutput(self.testOutput)
        self.uno.calcLoserPoints(hands, number_of_players)

        self.assertEqual(expectedOutput, self.testOutput.listOfTestOutputs)

    def testUnoStartCard(self):
        deck = ["B-9", "W-W"]
        hands = [["B-6"], ["B-3"]]
        number_of_players = 2

        self.testInput.setListOfTestInputs([1])
        self.uno.setGameInput(self.testInput)

        self.uno.setGameOutput(self.testOutput)
        self.uno.uno(deck, hands, number_of_players)

        print(self.testOutput.listOfTestOutputs)

        self.assertEqual("B-9", self.testOutput.listOfTestOutputs[0])



    # TODO - Test Whole game input/output


def main():
    unittest.main()


if __name__ == "__main__":
    unittest.main()
