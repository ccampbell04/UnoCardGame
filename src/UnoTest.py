import unittest
from src.Uno import Uno


class Uno(unittest.TestCase):
    uno = Uno()
    number_of_players = 2

    def testGenerateDeck(self):
        self.cards = self.uno.generateDeck()
        self.assertEqual(108, len(self.cards))

    def testStartDeck(self):
        testDeck=["R0", "B4", "G7"]
        self.assertEqual("G7", self.uno.startCard(testDeck))

    def testUserTurn(self):
        topCard = "R-1"
        hand = ["B-2", "R-4"]
        deck = []
        play = 1

        self.assertEqual("R-4", self.uno.userTurn(deck, hand, topCard))
def main():
    unittest.main()


if __name__ == "__main__":
    unittest.main()