import time
from graphics import *
"""This is a program created to run a wii system"""


class Wii():
    def __init__(self):
        self._on = "ON"
        self._playingGame = False
        self._game = None
        self.message = None
        self.wii = GraphWin("Power ON",300,300)

    def getState(self):
        return self._on

    def setGame(self, game):
        self._game = game
        self._playingGame = True
        self.message = Text(Point(self.wii.getWidth()/2, 30), 'Playing {}'.format(self._game))
        self.message.draw(self.wii)
        time.sleep(3)
        self.message.setText("Wii state is FUNCTIONAL.")
        time.sleep(2)
        self.message.setText("Use console for commands...")

    def endGame(self):
        if self._game != "":
            self._game = None
            self.message.setText("Game Closed")
            time.sleep(3)
            self.message.setText("Wii state is FUNCTIONAL.")
            time.sleep(2)
            self.message.setText("Use console for commands...")
        else:
            self.message.setText("The wii does not currently have any games playing.")

    def shutDown(self):
        self.wii.close()

    def __repr__(self):
        return self.getState()+" Is this Wii"+", it is playing -->"+self._game



def main():
    myNewWii = Wii()
    print(myNewWii.getState())
    myNewWii.setGame("CSGO")
    print(myNewWii)
    time.sleep(34)
    myNewWii.shutDown()

main()
