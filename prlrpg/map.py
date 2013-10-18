"""Definitions for maps."""

class InvalidMove(BaseException):
    """Exception for invalid moves."""

class Location(object):
    """A single game location."""

    title = None
    description = None
    directions = {}
    items = {}

    def __init__(self, title, description, directions, items={}):
        self.title = title
        self.description = description
        self.directions = directions
        self.items = {
            itemname: Item(itemname, description)
            for (itemname, description) in items
        }

    def look(self):
        return '\n\n'.join([
            self.title,
            self.description,
            self.show_items(),
            self.show_directions(),
        ])

    def show_directions(self):
        """Human readable list of directions."""
        return "You see the following exits: {0}".format(
            ','.join(self.directions.keys()))

    def show_items(self):
        """Items in this location."""
        return "You see here: {0}".format(','.join(self.items.keys()))

            
class Map(dict):
    """The game map."""

    def __init__(self, data):
        for k, v in data.items():
            self[k] = Location(**v)
        self.position = self['INITIAL']

    def move(self, direction):
        """Move to another position."""
        if direction not in self.position.directions:
            raise InvalidMove()
        self.position = self[self.position.directions[direction]]

    def look(self, item=None):
        if item is None:
            return self.position.look()
        else:
            return self.position.items[item].look()
