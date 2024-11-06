import math
import random
import time


class Nim():

    def __init__(self, initial = [1, 3, 5, 7]):
        
        self.piles = initial.copy()
        self.player = 0
        self.winner = None

    def avaliable_actions(self, piles):

        pass

    def other_player(self, player):

        pass

    def switch_player(self):

        pass

    def move(self, action):

        pass



class SARSA():

    def __init__(self):
        
        pass


def train(player, n_episodes):

    for episode in range(n_episodes):

        game = Nim()

        # keep track of last move made either player
        last = {}

        while True:

            # keep track of current state and action

            # keep track of last state and action

            # make move

            # when game is over, update Q values with rewards

            # if the game is continuing, no rewards yet

            pass

        # return the trained player
        return player


def play():

    # if no player order set, chose human's order randomly

    # create new game

    while True:

        # print contents of piles

        # compute avaiable actions

        # let human make a move

        # have AI make a move

        # make move

        # check for winner

        pass