import unittest
from src.Snap import Snap


class SnapTest(unittest.TestCase):
    snap = Snap()

    def test_initialise_score(self):
        self.init = self.snap.initialise_score()
        self.assertEquals(self.init, [{"turn": True, "score": 0}, {"turn": False, "score": 0}])

    def test_is_snap(self):
        self.init = self.snap.is_snap("D8", "D8")
        self.assertEquals(self.init, True)

    def test_play_card(self):
        hand = [["D4", "H6"], ["C8", "SA"]]
        self.init = self.snap.play_card(0, hand, 1)
        self.assertEquals(self.init, "SA")


def main():
    unittest.main()


if __name__ == "__main__":
    unittest.main()
