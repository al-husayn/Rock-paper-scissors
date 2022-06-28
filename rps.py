#!/usr/bin/env python3
from ast import Assert
import random
from secrets import choice
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        choice = input("Hey! What's your next move?: ")
        while choice not in moves:
            choice = input("Please enter a valid move!: ")
        return choice


class ReflectPlayer(Player):
    def __init__(self):
        self.current_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.current_move = their_move

    def move(self):
        return self.current_move


class CyclePlayer(Player):
    def __init__(self):
        self.current_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.current_move = my_move

    def move(self):
        last = len(moves)
        for i in range(last):
            if moves[i] == self.current_move:
                if i != last-1:
                    return moves[i+1]
                else:
                    return moves[0]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.keep_score(move1, move2)

    def play_game(self):
        print("Game start!")
        for round in range(5):
            print(f"Round {round}:")
            self.play_round()
            self.display_outcome()

        print("Game over!")

        if self.p2_score > self.p1_score:
            return f"PLAYER2 WINS!"

        if self.p2_score == self.p1_score:
            return "Draw Game"

        return f"PLAYER1 WINS!"

    def keep_score(self, one, two):
        if one == two:
            return

        if beats(one, two):
            self.p1_score += 1
        else:
            self.p2_score += 1

    def display_outcome(self):
        print(
            f"Player1 Score: {self.p1_score} | Player2 Score: {self.p2_score}"
        )


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    print(game.play_game())
