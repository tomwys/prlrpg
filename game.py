# -*- coding: utf-8 -*-


class Game:
    def __init__(self, data):
        self.position = "INITIAL"
        self.data = data

    def start(self):
        return self.look()

    def look_item(self, item):
        position = self.get_position()
        if item == "shroom":
            return "You eat a magic shroom and are suddenly transported to a magic land\n YOU WIN"
        if item in position.items:
            return position.items[item].look()
        return  "Can't look at {}".format(item)


    def move(self, direction):
        position = self.get_position()
        if direction in position.directions:
            self.position = position.directions[direction]
            return self.look()
        else:
            return "You can't move in that direction."

    def get_position(self):
        return self.data[self.position]

    def look(self):
        return self.get_position().look()

    def kill(self, who):
        return "%s died in a pain." % who