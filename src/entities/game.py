
class Game:
    """
    Represents one game, consisting of multiple rounds.

    Attributes:
        id: Unique ID used by the repository.
        name: Descriptive name.
        rounds: An array of the rounds associated with this game, in order.
    """

    def __init__(self, name, rounds):
        """
        Construct new Game entity. ID is set to None initially.

        Args:
            name: Descriptive name.
            rounds: An array of Round entities, in order.
        """

        self.id = None
        self.name = name
        self.rounds = rounds
