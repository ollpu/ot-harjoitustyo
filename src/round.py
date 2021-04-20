
class Round:
    """
    Represents one round of a game. Consists of multiple (text, image)-pairs.

    Attributes:
        pairs: List of tuples, `(str, Image)`.
    """

    def __init__(self, pairs):
        self.pairs = pairs
