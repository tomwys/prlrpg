"""Definitions for maps."""

class InvalidMove(BaseException):
    """Exception for invalid moves."""

class Location(object):
    """A single game location."""

    title = None
    description = None
    directions = {}

    def __init__(self, title, description, directions):
        self.title = title
        self.description = description
        self.directions = directions

    def look(self):
        return '\n\n'.join([
            self.title,
            self.description,
            self.show_directions(),
        ])

    def show_directions(self):
        """Human readable list of directions."""
        return "You see the following exits: {0}".format(
            ','.join(self.directions.keys()))
            
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
