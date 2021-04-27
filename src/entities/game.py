
class Game:
    """
    Represents one game, consisting of multiple rounds.

    Attributes:
        id: Unique id used by the repository.
        name: Descriptive name.
        rounds: An array of the rounds associated with this game, in order.
    """

    def __init__(self, name, rounds):
        self.id = None
        self.name = name
        self.rounds = rounds
