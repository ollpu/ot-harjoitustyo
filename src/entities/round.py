
class Round:
    """
    Represents one round of a game. Consists of multiple (caption, image)-pairs.

    Attributes:
        id: Unique ID used by GameRepository.
        pairs: List of tuples, `(str, Image)`.
    """

    def __init__(self, pairs):
        """
        Construct a Round entity. ID is set to None initially.

        Args:
            pairs: List of tuples, `(str, Image)`.
        """

        self.id = None
        self.pairs = pairs
