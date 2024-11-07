import math
import random
import time


class Nim():

    def __init__(self, initial = [1, 3, 5, 7]):
        
        self.piles = initial.copy()
        self.player = 0
        self.winner = None

    def avaliable_actions(self, piles):

        actions = set()

        for i, pile in enumerate(piles):
            for j in range(1, pile + 1):
                actions.add((i, j))

        return actions

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


def play(ai, human = None):

    # if no player order set, chose human's order randomly
    if human is None:
        human = int(random.uniform(0, 1))
        
    # create new game
    game = Nim()

    while True:

        # print contents of piles
        for i, pile in enumerate(game.piles):
            print(f"Pile {i} : {pile}")

        # compute avaiable actions
        available_actions = Nim.available_actions(game.piles)

        # let human make a move
        if game.player == human:
            print('Your turn')
            while True:
                pile = int(input('Choose a pile: '))
                count = int(input('Choose a count: '))
                if (pile, count) in available_actions:
                    break
                print('Invalid move, try again')
        # have AI make a move
        else:
            print('AI turn')
            pile, count = ai.choose_action(game.piles, epsilon = False)
            print('AI chose to take {count} from pile {pile}.')
        
        # make move
        game.move((pile, count))
        
        # check for winner
        if game.winner is not None:
            print('GAME OVER')
            winner = 'Human' if game.winner == human else 'AI'
            print('Winner is {winner}')
