class Item(self):
    """Some item."""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def look():
        return '\n'.join([
            self.name, self.description
        ])
