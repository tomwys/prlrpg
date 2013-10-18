

class Item:
    """Some item."""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def look(self):
        return '\n'.join([
            self.name, self.description
        ])
