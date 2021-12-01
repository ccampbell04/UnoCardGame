import unittest
from src.BlackJack import BlackJack


class BlackJackTest(unittest.TestCase):
    blackjack = BlackJack()

    def test_score_hand(self):
        self.assertEqual(18, self.blackjack.score_hand(["CK", "D8"]))

    def test_deal_to_player(self):
        deck = ["H7"]
        hand = ["S2", "D9"]
        self.assertEqual(True, self.blackjack.deal_to_player(deck, hand))

    def test_find_winner(self):
        self.assertEqual([1], self.blackjack.find_winner([['C2', 'D3'], ['DK', 'DA'], ['H4', 'H6']]))

    def test_initialise_computer_risk(self):
        self.number = self.blackjack.initialise_computer_risk(2)
        self.assertTrue(2 <= self.number[1] <= 9)


def main():
    unittest.main()


if __name__ == "__main__":
    unittest.main()