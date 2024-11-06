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

    def __init__(self, alpha = 0.5, epsilon = 0.1):
        
        self.q = {}
        self.alpha = alpha
        self.epsilon = epsilon

    def update(self, old_state, action, new_state, reward):

        pass

    def get_value(self, state, action):

        raise NotImplementedError

    def update_value(self, state, action):

        raise NotImplementedError

    def choose_action(self, state, epsilon = True):

        raise NotImplementedError


class QLearning():

    def __init__(self, alpha = 0.5, epsilon = 0.1):

        self.alpha = alpha
        self.epsilon = epsilon

    def update(self, old_state, action, new_state, reward):

        pass

    def get_value(self, state, action):

        raise NotImplementedError

    def update_value(self, state, action):

        raise NotImplementedError

    def best_future_reward(self, state):

        raise NotImplementedError

    def choose_action(self, state, epsilon = True):

        raise NotImplementedError

def train(player, n_episodes):

    for episode in range(n_episodes):

        game = Nim()

        # keep track of last move made either player
        last = {0 : {'state' : None, 'action' : None}, {'state' : None, 'action' : None}}

        while True:

            # keep track of current state and action
            state, action = game.piles.copy(), player.choose_action(game.piles)

            # keep track of last state and action
            last[game.player]['state'], last[game.player]['action'] = state, action

            # make move
            game.move(action)
            new_state = game.piles.copy()

            # when game is over, update Q values with rewards
            if game.winner is not None:
                player.update(state, action, new_state, -1)
                player.update(last[game.player]['state'], last[game.player]['action'], new_state, 1)
                break
            # if the game is continuing, no rewards yet
            elif last[game.player]['state'] is not None:
                player.update(last[game.player]['state'], last[game.player]['action'], new_state, 0)

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
