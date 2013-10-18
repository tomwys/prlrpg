from game import Game
from input import Input

import yaml

from prlrpg.map import Map

import os

def main():

    with open('sample_map.yaml') as f:
        data = yaml.load(f)

    map = Map(data)

    input_object = Input(read_line=input, put_line=print)
    game = Game(data = map)
    input_object.put_line(game.start())
    while True:
        read = input_object.next_move()

        if read:
            move, args = read
            response = getattr(game, move)(*args)
            input_object.put_line(response)


if __name__ == "__main__":
    main()