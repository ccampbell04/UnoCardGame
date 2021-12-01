from PlayingCard import PlayingCard


class Uno:
    playing_card = PlayingCard()
    suits = {"R": "Red", "B": "Blue", "Y": "Yellow", "G": "Green"}
    faces = ["0", "1", "1", "2", "2", "3", "3", "4", "4", "5", "5", "6", "6", "7", "7", "8", "8", "9", "9", "S", "S",
             "R", "R", "+2", "+2", "W", "+4"]

    def generateDeck(self):
        deck = []
        for suit in self.suits.keys():
            for face in self.faces:
                deck.append(suit + "-" + face)
        return deck

    def startCard(self, deck):
        topCard = self.playing_card.deal_a_card(deck)
        return topCard

    def userTurn(self, deck, hand, topCard):
        print(hand)
        while True:
            play = int(input("Pick a card to play (by position)"))
            if play <= len(hand):
                break
            print("Out of Range")
        play -= 1

        playerSplit = hand[play].split("-")
        deckSplit = topCard.split("-")
        # print(split)

        if playerSplit[0] == deckSplit[0]:
            topCard = hand[play]
            hand.pop(play)
            # print("Valid choice")
        elif playerSplit[1] == deckSplit[1]:
            topCard = hand[play]
            hand.pop(play)
            # print("Valid choice")
        else:
            print("Invalid choice dealing card")
            # Add a card to all players

        return topCard

    def Uno(self, deck, hands):
        topCard = self.startCard(deck)
        print(topCard)
        topCard = self.userTurn(deck, hands[self.playing_card.user_hand], topCard)

    def main(self):
        number_of_players = int(input("Please enter the number of players, max is six"))
        deck = self.generateDeck()
        deck = self.playing_card.shuffle_cards(deck)
        hands = self.playing_card.deal_cards(deck, 7, number_of_players)
        self.Uno(deck, hands)


if __name__ == "__main__":
    uno = Uno()
    uno.main()
