import random


class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def cardvalue(self):
        if self.rank == "J" or self.rank == "Q" or self.rank == "K":
            return 10
        elif self.rank == "A":
            return 11
        else:
            return int(self.rank)

        

class Deck:
    def __init__(self):
        self.deck = []


    def createddeck(self):
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['Hearts ♥', 'Diamonds ♦', 'Clubs ♣', 'Spades ♠']
        # deck = []

        for i in suits:
            for x in ranks:
                cards = card(i,x)
                #players cards so we can add them up together in function sumofp and sumofd
                self.deck.append(cards)
        # return deck
        
    
    def shuffledeck(self):
        random.shuffle(self.deck)


    def printdeck(self):

        for i in self.deck:
            print(i.rank,i.suit)

    


class Dealer:
    def __init__(self, deck):
        self.deck = deck
        self.listofd = []
        self.listofp = []

    def deal(self):
        x=self.deck.pop()
        print(x.rank,x.suit)
        self.listofp.append(x)
    
    def dealerdeal(self):
        x =self.deck.pop()
        print(x.rank,x.suit)
        self.listofd.append(x)
        


    def dealercards(self):
        d1=self.deck.pop()
        d2=self.deck.pop()
        print(d1.rank, d1.suit)
        self.listofd.append(d1)
        self.listofd.append(d2)
    
    def playercards(self):
        p1 = self.deck.pop()
        p2= self.deck.pop()
        print(p1.rank, p1.suit)
        #made this into a list so we can add all the cards
        self.listofp.append(p1)
        print(p2.rank,p2.suit)
        self.listofp.append(p2)

    def under21(self):
 
        if self.sumofplayercards() > 21:
            return False
        else:
            return True

    def sumofplayercards(self):
        Sum = 0 

        for I in range(len(self.listofp)): 
            Sum = Sum  + (self.listofp[I].cardvalue())
        return Sum


    def sumofdealercards(self):
        Sum = 0 

        for I in range(len(self.listofd)): 
            Sum = Sum  + (self.listofd[I].cardvalue())
        return Sum

    def aces(self):
        x = False
        for a in range(len(self.listofp)):
            if self.listofp[a].rank == "A":
                self.listofp[a].rank = "1"
                x = True
        return x
    
                


    def hitstand(self):
            hit = input(f'Type in (h) for hit and (s) for stand: ')
            if hit == 'h':
                self.deal()
                if self.under21() == True:
                    self.hitstand()

                else:
                    if self.aces() == True:
                        
                        self.hitstand()
                    else:
                        print(f'You bust!' )
                        print("You got:", self.sumofplayercards())
                        print("Dealer got: ", self.sumofdealercards())

            elif hit == 's':
                print("Players total:", self.sumofplayercards())
                return

            else: 
                print(f'Make a move fr')
                self.hitstand()
        
        
    

    def dealerhitstand(self):
        if self.sumofplayercards() > 21:
            print(f'Dealer wins!')
            return
        if self.sumofdealercards() > 21:
            print(f'Dealer bust! ')
            print(f'Player wins! ')
            print(f'Players total:', self.sumofplayercards())
        if self.sumofdealercards() <17:
            print(f'Dealers draw: ')
            self.dealerdeal()
            print(self.sumofdealercards())
            self.dealerhitstand()

        else:
            print("Dealers total:", self.sumofdealercards())
            return

    def blackjack(self):
        if self.sumofplayercards() ==21 and self.sumofdealercards() == 21:
            print(f'Its a standoff!')
            return True
        elif self.sumofplayercards() ==21:
            print(f'Player Blackjack!')
            return True
        elif self.sumofdealercards() ==21:
            print(f'Dealer Blackjack!')
            return True
        else:
            return False
        

    def winnerwinner(self):
        if self.sumofplayercards() <=21 and self.sumofdealercards() <=21:
            if self.sumofplayercards() > self.sumofdealercards():
                print(f'Player wins! ')
            elif self.sumofplayercards() == self.sumofdealercards():
                print(f"Its a standoff! Let's play a new game!")
            else:
                print(f'Dealer wins!')




    
print("Welcome to the game of BLACKJACK my friend! May the odds ever be in your favor!")
playagain = "Yes".lower()
while playagain == "Yes".lower():


    deck1= Deck()
    deck1.createddeck()
    deck1.shuffledeck()
    # deck1.printdeck()

    dealer1 = Dealer(deck1.deck)
    print(f'These are the dealer cards: ')
    dealer1.dealercards()
    print(f'These are the player cards: ')
    dealer1.playercards()
    x=dealer1.blackjack()
    if x == False:
        dealer1.hitstand()
        dealer1.dealerhitstand()
    dealer1.winnerwinner()

    playagain = input(f'Type "Yes" if you want to play again, and no if you do not!').lower()
    if playagain != "yes" or playagain == "no":
        print("Better luck next time champ. Until next time! See ya!")
    





