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

    def userCheckSpecialcard(self, card, index, hands, deck, topCard):
        # +4 WildCard
        if card[2] == "+" and card[0] == "W":
            self.output.display("Wildcard played")
            colour = self.gameInput.getString("Which colour would you like")
            number = self.gameInput.getString("Which number would you like")
            topCard = colour + "-" + number
            self.output.display("Dealing 4 cards to next player")
            for i in range(3):
                hands[index + 1].append(self.playing_card.deal_a_card(deck))

                # Wildcard
        elif card[0] == "W" and card[2] == "W":
            self.output.display("Wildcard played")
            colour = self.gameInput.getString("Which colour would you like")
            number = self.gameInput.getString("Which number would you like")
            topCard = colour + "-" + number

        # +2 Card
        elif card[2] == "+":
            self.output.display("Dealing 2 cards to next player")
            topCard = card
            for i in range(0, 1):
                hands[index + 1].append(self.playing_card.deal_a_card(deck))
        else:
            topCard = card
        return topCard

    def userTurn(self, deck, hand, topCard, hands, index):
        self.output.display(topCard)
        if self.ableToPlay(hand, topCard):

            self.output.display("Your hand is:")
            self.output.display(hand)
            play = self.userInput(hand)
            deckSplit = self.splitCard(topCard)
            while True:
                play -= 1
                playerSplit = self.splitCard(hand[play])
                if playerSplit[0] == deckSplit[0] or playerSplit[1] == deckSplit[1] or playerSplit[0] == "W":
                    topCard = self.userCheckSpecialcard(hand[play], index, hands, deck, topCard)
                    hand.pop(play)
                    self.output.display("Valid choice")
                    break
                else:
                    self.output.display("Invalid choice")
                    play = self.userInput(hand)
        else:
            topCard = self.cantPlay(hand, deck, topCard)

        win = self.checkWinner(hand)
        if len(hand)==1:
            self.output.display("Uno!")
        return topCard, win

    def checkComputerSpecialCard(self, card, index, hand, deck, hands, topCard):
        # +4 WildCard
        if card[2] == "+" and card[0] == "W":
            self.output.display("Wildcard played")
            bestCardPosition = self.bestCompMove(hand)
            bestCard = hand[bestCardPosition]
            topCard = bestCard
            self.output.display("Top card is now " + topCard)
            self.output.display("Dealing 4 cards to next player")
            if index == len(hands):
                for i in range(3):
                    hands[index + 1] = self.playing_card.deal_a_card(deck)
            for i in range(3):
                hands[0] = self.playing_card.deal_a_card(deck)

        # Wildcard
        elif card[0] == "W" and card[2] == "W":
            self.output.display("Wildcard played")
            bestCardPosition = self.bestCompMove(hands[index])
            bestCard = hand[bestCardPosition]
            topCard = bestCard
            self.output.display("Top card is now " + topCard)
        # +2 Card
        elif card[2] == "+":
            topCard = card
            self.output.display("Dealing 2 cards to next player")
            if index == len(hands):
                for i in range(0, 1):
                    hands[index + 1] = self.playing_card.deal_a_card(deck)
            for i in range(0, 1):
                hands[0] = self.playing_card.deal_a_card(deck)
        else:
            topCard = card
        return topCard

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

            bestMoveIndex = self.bestCompMove(possibleMoves)
            bestMove = possibleMoves[bestMoveIndex]
            topCard = self.checkComputerSpecialCard(bestMove, index, hand, deck, hands,topCard)

            pos = 0
            count = 0
            for card in hand:
                if card == bestMove:
                    pos = count
                count += 1
            hand.pop(pos)

            self.output.display("Computer played " + topCard)

        else:
            topCard = self.cantPlay(hand, deck, topCard)

        win = self.checkWinner(hand)
        if len(hand)==1:
            self.output.display("Uno!")
        return topCard, win

    def cantPlay(self, hand, deck, topCard):
        dealtCard = self.playing_card.deal_a_card(deck)
        dealtSplit = self.splitCard(dealtCard)
        deckSplit = self.splitCard(topCard)

        if dealtSplit[0] == deckSplit[0] or dealtSplit[1] == deckSplit[1]:
            self.output.display("New card is valid, playing " + dealtCard)
            topCard = dealtCard
            time.sleep(2.5)
        else:
            self.output.display("New card can't be played, adding " + dealtCard + " to hand")
            time.sleep(2.5)
            hand.append(dealtCard)

        return topCard

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
                self.output.display("Special card")
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

    def playGame(self, deck, hands, number_of_players, topCard):
        playing = True

        while playing:

            self.output.display("------------------------User turn------------------------------")
            topCard, win = self.userTurn(deck, hands[self.playing_card.user_hand], topCard, hands, 0)
            if win:
                self.output.display("User Wins!")
                break
            for i in range(1, number_of_players):
                self.output.display("------------------------Computer " + str(i) + " turn------------------------")
                topCard, win = self.computerTurn(deck, hands[i], topCard, hands, i)
                if win:
                    self.output.display("Computer" + str(i) + "Wins!")
                    break
                time.sleep(2)

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
                self.output.display("Player scored " + str(score))
            else:
                self.output.display("Computer " + str(i) + " scored " + str(score))

    def uno(self, deck, hands, number_of_players):
        topCard = self.startCard(deck)
        self.output.display(topCard)
        self.playGame(deck, hands, number_of_players, topCard)
        self.calcLoserPoints(hands, number_of_players)

    def main(self):
        number_of_players = int(self.gameInput.getString("Please enter the number of players, max is six"))
        deck = self.generateDeck()
        deck = self.playing_card.shuffle_cards(deck)
        hands = self.playing_card.deal_cards(deck, 7, number_of_players)

        self.uno(deck, hands, number_of_players)


if __name__ == "__main__":
    uno = Uno()
    uno.main()

'''Still to do
Program wild cards and special cards
Have UNO! displayed when any player has 1 card left
'''
