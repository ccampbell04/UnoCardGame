from src.ConsoleInput import ConsoleInput
from src.ConsoleOutput import ConsoleOutput
from PlayingCard import PlayingCard


class Uno:
    playing_card = PlayingCard()
    suits = {"R": "Red", "B": "Blue", "Y": "Yellow", "G": "Green"}
    faces = ["0", "1", "1", "2", "2", "3", "3", "4", "4", "5", "5", "6", "6", "7", "7", "8", "8", "9", "9", "S", "S",
             "R", "R", "+2", "+2"]
    wild = ["W-W", "W-W", "W-W", "W-W", "W-+4", "W-+4", "W-+4", "W-+4"]

    gameInput = ConsoleInput()
    output = ConsoleOutput()

    def generateDeck(self):
        deck = []
        for suit in self.suits.keys():
            for face in self.faces:
                deck.append(suit + "-" + face)
        for face in self.wild:
            deck.append(face)

        return deck

    def startCard(self, deck):
        topCard = self.playing_card.deal_a_card(deck)
        return topCard

    def ableToPlay(self, hand, topCard):

        topCardSplit = self.splitCard(topCard)

        for cards in hand:
            cardSplit = self.splitCard(cards)

            if cardSplit[0] == topCardSplit[0]:
                return True
            elif cardSplit[1] == topCardSplit[1]:
                return True

        return False

    def userInput(self, hand):
        while True:
            play = int(self.gameInput.getString("Pick a card to play (by position)"))
            if len(hand) >= play > 0:
                break
            self.output.display("Out of Range")

        return play

    def splitCard(self, card):
        splitCard = card.split("-")
        return splitCard

    def userTurn(self, deck, hand, topCard):
        self.output.display(topCard)
        if self.ableToPlay(hand, topCard):

            self.output.display("Your hand is:")
            self.output.display(hand)
            play = self.userInput(hand)
            play -= 1
            playerSplit = self.splitCard(hand[play])
            deckSplit = self.splitCard(topCard)
            # print(split)
            while True:
                if playerSplit[0] == deckSplit[0]:
                    topCard = hand[play]
                    hand.pop(play)
                    self.output.display("Valid choice")
                    break
                elif playerSplit[1] == deckSplit[1]:
                    topCard = hand[play]
                    hand.pop(play)
                    self.output.display("Valid choice")
                    break
                else:
                    self.output.display("Invalid choice")
                    play = self.userInput(hand)

        else:
            topCard = self.cantPlay(hand, deck, topCard)

        win = self.checkWinner(hand)

        return topCard, win

    def computerTurn(self, deck, hand, topCard):
        if self.ableToPlay(hand, topCard):
            possibleMoves = []
            topSplit = self.splitCard(topCard)
            for cards in hand:
                cardSplit = self.splitCard(cards)
                if cardSplit[0] == topSplit[0]:
                    possibleMoves.append(cards)
                elif cardSplit[1] == topSplit[1]:
                    possibleMoves.append(cards)

            bestMoveIndex = self.bestCompMove(possibleMoves)
            bestMove = possibleMoves(bestMoveIndex)
            topCard = bestMove
            hand.pop(bestMove)

        else:
            topCard = self.cantPlay(hand, deck, topCard)

        win = self.checkWinner(hand)

        return topCard, win

    def cantPlay(self, hand, deck, topCard):
        dealtCard = deck.pop
        dealtSplit = self.splitCard(dealtCard)
        deckSplit = self.splitCard(topCard)

        if dealtSplit[0] == deckSplit[0]:
            self.output.display("Your new card is valid, playing " + dealtCard)
            topCard = dealtCard
        elif dealtSplit[1] == deckSplit[0]:
            self.output.display("Your new card is valid, playing " + dealtCard)
            topCard = dealtCard
        else:
            self.output.display("New card can't be played, adding to hand")
            hand.append(dealtSplit)

        self.output.display(hand)
        return topCard

    def bestCompMove(self, possibleMoves):
        bestFace = 0
        for moves in possibleMoves:
            split = self.splitCard(moves)
            intSplit = int(split[1])
            if intSplit > bestFace:
                bestFace = int(split[1])
                bestMove = moves

        return bestMove

    def checkWinner(self, hand):
        if len(hand) == 0:
            return True
        else:
            return False

    def uno(self, deck, hands):
        topCard = self.startCard(deck)
        self.output.display(topCard)
        win = False
        while win==False:
            topCard, win = self.userTurn(deck, hands[self.playing_card.user_hand], topCard)




    def main(self):
        number_of_players = int(self.gameInput.getString("Please enter the number of players, max is six"))
        deck = self.generateDeck()
        deck = self.playing_card.shuffle_cards(deck)
        hands = self.playing_card.deal_cards(deck, 7, number_of_players)

        self.uno(deck, hands)


if __name__ == "__main__":
    uno = Uno()
    uno.main()

'''Still to do
Loop in uno to continue game after turn 1
Program wild cards and special cards
Calculate winner
Calculate points for losing players

'''
