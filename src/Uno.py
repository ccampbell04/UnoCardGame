import time

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
    gameOutput = ConsoleOutput()

    def setGameInput(self, gameInput):
        self.gameInput = gameInput

    def setGameOutput(self, gameOutput):
        self.gameOutput = gameOutput

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
            self.gameOutput.display("Out of Range")

        return play

    def splitCard(self, card):
        splitCard = card.split("-")
        return splitCard

    def checkSpecialCard(self, card, index, hand, deck, hands):

        if card[2] == "+" and card[0] == "W":
            self.gameOutput.display("Wildcard played")

            if index == 0:
                topCard = self.userWildCard()
            else:
                topCard = self.computerWildCard(hand)

            self.gameOutput.display("Top card is now " + topCard)
            self.gameOutput.display("Dealing 4 cards to next player")

            if index == 0:
                self.dealFourCards(hands, (index + 1), deck)
            else:
                self.dealFourCards(hands, (index - 1), deck)

        elif card[0] == "W" and card[2] == "W":

            self.gameOutput.display("Wildcard played")
            if index == 0:
                topCard = self.userWildCard()
            else:
                topCard = self.computerWildCard(hand)
            self.gameOutput.display("Top card is now " + topCard)

        elif card[2] == "+":

            self.gameOutput.display("Dealing 2 cards to next player")
            topCard = card
            if index == 0:
                self.dealTwoCards(hands, (index + 1), deck)
            else:
                self.dealTwoCards(hands, (index - 1), deck)

        elif card[2] == "S":
            topCard = card
            self.gameOutput.display("Skipping next turn")
            if index == 0:
                return topCard, "user"
            else:
                return topCard, "computer"

        else:
            topCard = card

        if index == 0:
            return topCard, "computer"
        else:
            return topCard, "user"

    def dealTwoCards(self, hands, index, deck):
        for i in range(2):
            hands[index].append(self.playing_card.deal_a_card(deck))

    def dealFourCards(self, hands, index, deck):
        for i in range(4):
            hands[index].append(self.playing_card.deal_a_card(deck))

    def userWildCard(self):
        colour = self.gameInput.getString("Which colour would you like")
        colour = colour.upper()
        number = self.gameInput.getString("Which number would you like")
        return colour + "-" + number

    def computerWildCard(self, hand):
        bestCardPosition = self.bestCompMove(hand)
        bestCard = hand[bestCardPosition]
        return bestCard

    def userTurn(self, deck, hand, topCard, hands, index):
        self.gameOutput.display(topCard)
        if self.ableToPlay(hand, topCard):

            self.gameOutput.display("Your hand is:")
            self.gameOutput.display(hand)
            play = self.userInput(hand)
            deckSplit = self.splitCard(topCard)
            while True:
                play -= 1
                playerSplit = self.splitCard(hand[play])
                if playerSplit[0] == deckSplit[0] or playerSplit[1] == deckSplit[1] or playerSplit[0] == "W":
                    topCard, turn = self.checkSpecialCard(hand[play], index, hand, deck, hands)
                    hand.pop(play)
                    self.gameOutput.display("Valid choice")
                    break
                else:
                    self.gameOutput.display("Invalid choice")
                    play = self.userInput(hand)
        else:
            topCard, turn = self.cantPlay(hand, deck, topCard, index, hands)

        win = self.checkWinner(hand)
        if len(hand) == 1:
            self.gameOutput.display("Uno!")
        return topCard, win, turn

    def computerTurn(self, deck, hand, topCard, hands, index):
        if self.ableToPlay(hand, topCard):
            possibleMoves = []
            topSplit = self.splitCard(topCard)
            for cards in hand:
                cardSplit = self.splitCard(cards)
                if cardSplit[0] == topSplit[0] or cardSplit[1] == topSplit[1]:
                    possibleMoves.append(cards)
                elif cardSplit[0] == "W":
                    possibleMoves.append(cards)

            topCard, turn = self.playComputerCard(possibleMoves, index, hand, deck, hands)

        else:
            topCard, turn = self.cantPlay(hand, deck, topCard, index, hands)

        win = self.checkWinner(hand)
        if len(hand) == 1:
            self.gameOutput.display("Uno!")
        return topCard, win, turn

    def playComputerCard(self, possibleMoves, index, hand, deck, hands):

        bestMoveIndex = self.bestCompMove(possibleMoves)
        bestMove = possibleMoves[bestMoveIndex]
        topCard, turn = self.checkSpecialCard(bestMove, index, hand, deck, hands)

        pos = 0
        count = 0
        for card in hand:
            if card == bestMove:
                pos = count
            count += 1
        hand.pop(pos)

        self.gameOutput.display("Computer played " + topCard)

        return topCard, turn

    def cantPlay(self, hand, deck, topCard, index, hands):
        dealtCard = self.playing_card.deal_a_card(deck)
        dealtSplit = self.splitCard(dealtCard)
        deckSplit = self.splitCard(topCard)

        if index == 0:
            turn = "computer"
        else:
            turn = "user"

        if dealtSplit[0] == deckSplit[0] or dealtSplit[1] == deckSplit[1]:
            self.gameOutput.display("New card is valid, playing " + dealtCard)
            topCard = dealtCard
        elif dealtSplit[0] == "W":
            self.gameOutput.display("New card is valid, playing " + dealtCard)
            topCard, turn = self.checkSpecialCard(dealtCard, index, hand, deck, hands)
        else:
            self.gameOutput.display("New card can't be played, adding " + dealtCard + " to hand")
            hand.append(dealtCard)

        time.sleep(1)

        return topCard, turn

    def bestCompMove(self, possibleMoves):
        bestFace = 0
        position = 0
        counter = 0

        for moves in possibleMoves:
            split = self.splitCard(moves)
            try:
                if int(split[1]) > bestFace:
                    bestFace = int(split[1])
                    position = counter
            except:
                self.gameOutput.display("Special card")
            finally:
                if split[1] == "+2":
                    bestFace = split[1]
                    position = counter

            counter += 1

        return position

    def checkWinner(self, hand):
        if len(hand) == 0:
            return True
        else:
            return False

    def calcLoserPoints(self, hands, number_of_players):
        for i in range(0, number_of_players):
            score = 0
            for card in hands[i]:
                if card[0] == "W":
                    score += 50
                elif card[1] == "+" or card[1] == "R" or card == "S":
                    score += 20
                else:
                    score += int(card[2])

            if i == 0:
                self.gameOutput.display("Player scored " + str(score))
            else:
                self.gameOutput.display("Computer " + str(i) + " scored " + str(score))

    def playGame(self, deck, hands, number_of_players, topCard):
        playing = True
        turn = "user"
        while playing:

            if turn == "user":
                self.gameOutput.display("------------------------User turn------------------------------")
                topCard, win, turn = self.userTurn(deck, hands[self.playing_card.user_hand], topCard, hands, 0)
                if win:
                    self.gameOutput.display("User Wins!")
                    break

            elif turn == "computer":
                self.gameOutput.display("------------------------Computer turn------------------------")
                topCard, win, turn = self.computerTurn(deck, hands[1], topCard, hands, 1)
                if win:
                    self.gameOutput.display("Computer Wins!")
                    break

            time.sleep(1)

    def uno(self, deck, hands, number_of_players):
        valid = False
        while not valid:
            topCard = self.startCard(deck)
            if topCard[0] != "W":
                valid = True

        self.gameOutput.display(topCard)
        self.playGame(deck, hands, number_of_players, topCard)
        self.calcLoserPoints(hands, number_of_players)

    def main(self):
        # number_of_players = int(self.gameInput.getString("Please enter the number of players, max is six"))
        number_of_players = 2
        deck = self.generateDeck()
        deck = self.playing_card.shuffle_cards(deck)
        hands = self.playing_card.deal_cards(deck, 7, number_of_players)

        self.uno(deck, hands, number_of_players)


if __name__ == "__main__":
    uno = Uno()
    uno.main()
