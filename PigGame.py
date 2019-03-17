import random

class PigGame():
    def __init__(self):
        self.yourScore = 0      #user score
        self.computerScore = 0  #computer score(pig)
        self.runningScore = 0   #sum of roll score
        self.currentTurn = 'u'  #variable for current player turn u: user , c: pig
        self.turn = 0

    def changeTurn(self):
        print('')
        if (self.currentTurn == 'u'):
            self.currentTurn = 'c'
            self.runningScore = 0
            print('Pig turn')
        elif(self.currentTurn == 'c'):
            self.currentTurn = 'u'
            self.runningScore = 0
            print('Player turn')

    def hold(self):
        if (self.currentTurn=='u'):
            self.yourScore += self.runningScore
        self.turn = 0
        self.runningScore = 0
        self.changeTurn()
        self.ask()

    def roll(self):
        self.turn += 1
        result = random.randint(1, 6)
        print('# %s dice result : %s'%(self.turn,result))
        if(result>1):
            self.runningScore+=result
            if (self.currentTurn == 'u'):
                print('Current your sum of score is %s' % self.runningScore)
                self.ask()
            elif (self.currentTurn == 'c'):
                print('Current pig sum of score is %s' % self.runningScore)
                self.roll()
        elif(result==1):
            #self.runningScore = 0
            if (self.currentTurn == 'u'):
                self.yourScore += self.runningScore
                if (self.yourScore >= 100):
                    self.win()
                else:
                    self.turn = 0
                    self.changeTurn()
                    self.roll()
            elif (self.currentTurn == 'c'):
                self.computerScore += self.runningScore
                if (self.computerScore >= 100):
                    self.win()
                else:
                    self.turn = 0
                    self.changeTurn()
                    self.ask()

    def ask(self):
        if (self.yourScore>=100 or self.computerScore>=100):
            if (self.yourScore>=100):
                self.win()
            else:
                self.win()
        else:
            if (self.currentTurn=='u'):
                self.showScore()
                decision = raw_input('Enter r is roll or Enter h is hold:    ')
                if(decision!='r' and decision!='h' and decision!='e'):
                    print('Invaild Decision. Please try again')
                    self.ask()
                elif(decision=='e'):
                    exit()
                else:
                    if(decision=='r'):
                        self.roll()
                    else:
                        print('Hold your turn')
                        self.hold()
            elif (self.currentTurn=='c'):
                print('it is pig call roll')
                self.roll()

    def win(self):
        if (self.yourScore >= 100):
            print('congratulations you win')
            exit()
        else:
            print('pig win')
            exit()

    def showScore(self):
        print('Player: %s' % (self.yourScore))
        print('Pig: %s' % (self.computerScore))


def main():
    game = PigGame()
    game.ask()

main()