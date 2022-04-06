'''
Rock-Paper-Scissors game
Starter code for Stanford CME 193
author: Sven Schmit
'''

import agent
from collections import Counter


class Game:
    def __init__(self, agent1: agent, agent2: agent):
        self.moves_a1 = []
        self.moves_a2 = []
        self.nround = 0
        self.score_a1 = 0
        self.score_a2 = 0

        self.agent1 = agent1
        self.agent2 = agent2

    def round(self):
        print('Round {}: '.format(self.nround+1))
        # we pass along history so a player can take that into account when
        # deciding the next move
        move_a1 = self.agent1.getMove(self.moves_a2, self.moves_a1)
        move_a2 = self.agent2.getMove(self.moves_a1, self.moves_a2)

        # compare the moves and decide who wins
        outcome = self.compare(move_a1, move_a2)

        # output outcome of current round
        if outcome == 1:
            print('\tPlayer 1 wins: {} beats {}'.format(move_a1, move_a2))
            self.score_a1 += 1
        elif outcome == 0:
            print('\tThis round is tied, both players played {}'.format(move_a1))
        else:
            print('\tPlayer 2 wins: {} beats {}'.format(move_a2, move_a1))
            self.score_a2 += 1

        self.moves_a1.append(move_a1)
        self.moves_a2.append(move_a2)

    def play(self, nrounds):
        for r in range(nrounds):
            self.round()
            self.nround += 1

    def mostMove(self, winnerAgentMoves):
        return Counter(winnerAgentMoves).most_common(1)

    def summary(self):
        # print some summary of the games
        most = ""
        print('='*20)
        if self.score_a1 > self.score_a2:
            print('Player 1 wins')
            most = self.mostMove(self.moves_a1)
        elif self.score_a1 < self.score_a2:
            print('Player 2 wins')
            most = self.mostMove(self.moves_a2)
        else:
            print('The game ends in a tie')

        print('Final score: {} - {}'.format(self.score_a1, self.score_a2))

        # To implement: find the move that was played most often

        print('Most played move: {}'.format(most))
        print('='*20)

    def compare(self, move1, move2):
        # returns 1 if move1 wins, 0 if it's a tie, and -1 if move2 wins
        if (move1 == 'r' and move2 == 's') or (move1 == 's' and move2 == 'p') or (move1 == 'p' and move2 == 'r'):
            return 1
        elif (move2 == 'r' and move1 == 's') or (move2 == 's' and move1 == 'p') or (move2 == 'p' and move1 == 'r'):
            return -1
        else:
            return 0
