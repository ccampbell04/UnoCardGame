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

    def ableToPlay(self, hand, topCard):

        topCardSplit = topCard.split("-")

        for cards in hand:
            cardSplit = cards.split("-")

            if cardSplit[0] == topCardSplit[0]:
                return True
            elif cardSplit[1] == topCardSplit[1]:
                return True

        return False

    def userInput(self, hand):
        while True:
            play = int(input("Pick a card to play (by position)"))
            if len(hand) >= play > 0:
                break
            print("Out of Range")


        return play

    def userTurn(self, deck, hand, topCard):
        if self.ableToPlay(hand, topCard):

            print("Your hand is:")
            print(hand)
            play = self.userInput(hand)
            play -= 1
            playerSplit = hand[play].split("-")
            deckSplit = topCard.split("-")
            # print(split)
            while True:
                if playerSplit[0] == deckSplit[0]:
                    topCard = hand[play]
                    hand.pop(play)
                    break
                    # print("Valid choice")
                elif playerSplit[1] == deckSplit[1]:
                    topCard = hand[play]
                    hand.pop(play)
                    break
                    # print("Valid choice")
                else:
                    print("Invalid choice")
                    play = self.userInput(hand)
                    # Deal player card
        else:
            dealtCard = self.playing_card.deal_a_card(deck)
            dealtSplit = dealtCard.split("-")
            deckSplit = topCard.split("-")

            if dealtSplit[0] == deckSplit[0]:
                print("Your new card is valid, playing " + dealtCard)
            elif dealtSplit[1] == deckSplit[0]:
                print("Your new card is valid, playing " + dealtCard)
            else:
                print("New card can't be played, adding to hand")
                hand.append(dealtSplit)

            print(hand)
        return topCard

    def uno(self, deck, hands):
        topCard = self.startCard(deck)
        print(topCard)
        topCard = self.userTurn(deck, hands[self.playing_card.user_hand], topCard)

    def main(self):
        number_of_players = int(input("Please enter the number of players, max is six"))
        deck = self.generateDeck()
        deck = self.playing_card.shuffle_cards(deck)
        hands = self.playing_card.deal_cards(deck, 7, number_of_players)
        self.uno(deck, hands)


if __name__ == "__main__":
    uno = Uno()
    uno.main()
