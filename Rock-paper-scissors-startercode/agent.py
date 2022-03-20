'''
Rock-Paper-Scissors game
Starter code for Stanford CME 193
author: Sven Schmit
'''

import random
from shutil import move

guarentee_p_rock = 0.0
guarentee_p_scissors = 0.0


class Agent:
    def getMove(self, moves_other, moves_self):
        pass


class InstructorAgent(Agent):
    def __init__(self):
        p_rock = random.random()
        p_scissors = random.random()
        p_paper = random.random()
        p_total = p_rock + p_scissors + p_paper

        self.p_rock = p_rock / p_total
        self.p_scissors = self.p_rock + p_scissors / p_total
        global guarentee_p_rock
        global guarentee_p_scissors

        guarentee_p_rock = self.p_rock
        guarentee_p_scissors = self.p_scissors

    def getMove(self, moves_other, moves_self):
        random_move = random.random()
        if random_move < self.p_rock:
            return 'r'
        elif random_move < self.p_scissors:
            return 's'
        else:
            return 'p'


class MyAgent(Agent):

    def getMove(self, moves_other, moves_self):
        random_move = random.random()
        if random_move < guarentee_p_rock:
            return 'p'
        elif random_move < guarentee_p_scissors:
            return 'r'
        else:
            return 's'


class HumanAgent(Agent):
    def getMove(self, moves_other, moves_self):
        moves = ['r', 'p', 's']
        move = ''
        while True:
            theMove = str(input('\tGet your all moves (r,p,s) >>  ')).lower()
            if theMove in moves:
                move = theMove
                break
        return move
