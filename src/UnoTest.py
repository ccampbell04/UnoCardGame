import unittest
from src.Uno import Uno


class UnoTest(unittest.TestCase):
    uno = Uno()
    number_of_players = 2

    def testGenerateDeck(self):
        self.cards = self.uno.generateDeck()
        self.assertEqual(108, len(self.cards))

    def testStartDeck(self):
        testDeck = ["R0", "B4", "G7"]
        self.assertEqual("G7", self.uno.startCard(testDeck))

    def testUserTurn(self):
        topCard = "R-1"
        hand = ["B-2", "R-4"]
        deck = []
        play = 1
        hands = []
        index = 0

        self.assertEqual(("R-4", False), self.uno.userTurn(deck, hand, topCard, hands, index))

    def testUserCantPlay(self):
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

    def testAbleToPlay(self):
        topCard = "R-1"
        hand = ["B-2", "Y-4", "G-+2"]

        self.assertEqual(False, self.uno.ableToPlay(hand, topCard))

    def testSpecialAbleToPlay(self):
        topCard = "R-+2"
        hand = ["B-2", "B-+2"]

        self.assertEqual(True, self.uno.ableToPlay(hand, topCard))

    def testComputerTurn(self):
        deck = []
        hands = []
        hand = ["B-1", "B-7", "B-9"]
        topCard = "B-6"
        index = 1

        self.assertEqual(("B-9" ,False), self.uno.computerTurn(deck, hand, topCard, hands, index))

    def testComputerCantPlay(self):
        deck = ["W-W"]
        hands = [["B-2"], ["B-3", "B-4"]]
        hand = ["B-3", "B-4"]
        topCard = "G-7"
        index = 1

        self.assertEqual(("B-4", False), self.uno.computerTurn(deck, hand, topCard, hands, index))

    def testBestCompMove(self):
        possibleMoves = ["Y-9", "B-+2", "R-S"]

        self.assertEqual(1, self.uno.bestCompMove(possibleMoves))

    def testCheckWinner(self):
        hand = []
        self.assertTrue(self.uno.checkWinner(hand))

    def testCalcUserPoints(self):
        hands = [["W-W"], [], ["R-R", "B-8"]]
        number_of_players = 3

        # Expected output should be
        # Player scored 50 points
        # Computer 1 scored 0 points
        # Computer 2 scored 28 points

    def testPlaySpecial(self):
        topCard = "R-1"
        hand = ["R-+2"]
        index = 1
        hands = [["R-2"], ["R-+2"]]
        deck = ["B-3", "G-5"]

        self.assertEqual(("R-+2", True), self.uno.computerTurn(deck, hand, topCard, hands, index))

def main():
    unittest.main()


if __name__ == "__main__":
    unittest.main()
