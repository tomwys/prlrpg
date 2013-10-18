# -*- coding: utf-8 -*-

import sys

class Input:

    def __init__(self, read_line, put_line):
        self.read_line = read_line
        self.put_line = put_line

    def next_move(self):
        text = self.read_line()
        try:
            command, *args = text.split()
            if command == "look" and not args:
                return ("look", [])
            if command == "look" and len(args) == 1:
                return ("look_item", args)
            if command == "move" and len(args) == 1:
                return ("move", args)
            if command == "kill" and len(args) == 1:
                return ("kill", args)
        except ValueError:
            pass
        self.put_line('Wrong move. Try: look.')
