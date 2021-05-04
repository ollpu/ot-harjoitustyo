
class Round:
    """
    Represents one round of a game. Consists of multiple (caption, image)-pairs.

    Attributes:
        id: Unique id used by GameRepository.
        pairs: List of tuples, `(str, Image)`.
    """

    def __init__(self, pairs):
        self.id = None
        self.pairs = pairs
