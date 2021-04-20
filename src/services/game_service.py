import random
from enum import Enum

class GuessResult(Enum):
    """
    Enum representing the outcome of a guess.

    INCORRECT = Wrong image guessed.
    CORRECT_ONE = Correct image guessed, proceeding to next one.
    CORRECT_ROUND_COMPLETE = Correct image guessed, and the current round is complete.
    """
    INCORRECT = 0
    CORRECT_ONE = 1
    CORRECT_ROUND_COMPLETE = 2

class GameService:
    """Service governing the logic of a game being played."""

    def __init__(self, shuffle=random.shuffle):
        """
        Constructor.

        Args:
            shuffle: Inject different shuffle implementation. The texts are first shuffled,
                     followed by the images, at the beginning of each round.
        """

        self._game = None
        self._current_round = None
        self._round = None
        self._texts_left = []
        self._images = []
        self._images_used = []
        self._shuffle = shuffle

    def reset(self):
        """
        Reset and unload currently active game.
        """

        self._game = None
        self._current_round = None
        self._round = None
        self._texts_left = []
        self._images = []
        self._images_used = []

    def start_game(self, game):
        """
        Start the given `game`. The first round is loaded immediately.

        Args:
            game: The game to be started.
        """

        self._game = game
        self._current_round = 0
        self._load_round()

    def _load_round(self):
        self._round = self._game.rounds[self._current_round]
        self._texts_left = [(text, i) for i, (text, _) in enumerate(self._round.pairs)]
        self._shuffle(self._texts_left)
        self._images = [(image, i) for i, (_, image) in enumerate(self._round.pairs)]
        self._shuffle(self._images)
        self._images_used = [False]*len(self._round.pairs)

    def next_round(self):
        """
        Move to and load next round.

        Returns:
            True if successful, False if there is no next round available.
        """

        assert self._current_round is not None
        self._current_round += 1
        if self._current_round >= len(self._game.rounds):
            self.reset()
            return False
        else:
            self._load_round()
            return True

    def get_text(self):
        """
        Get currently active text, against which the correct image should be guessed.

        Returns:
            String, the active text, or None if the round is complete.
        """

        if not self._texts_left:
            return None
        else:
            return self._texts_left[-1][0]

    def get_images(self):
        """
        Get images associated with this round.  The order is shuffled at the
        start of the round, so it can be used to lay out the images.

        Returns:
            An array of tuples (image, index) which represent the images
            of this round.
        """

        return self._images

    def get_used_images(self):
        """
        Query which images have been used already.

        Returns:
            An array of booleans, where the index i is True if that image
            has already been used on this round.
        """

        return self._images_used

    def submit_guess(self, index):
        """
        Guess that the current text corresponds to the image `index`.

        Args:
            index: Guessed image index, gotten from `get_images`.
        Returns:
            A `GuessResult`.
        """

        if index != self._texts_left[-1][1]:
            return GuessResult.INCORRECT
        else:
            self._images_used[index] = True
            self._texts_left.pop()
            if not self._texts_left:
                return GuessResult.CORRECT_ROUND_COMPLETE
            else:
                return GuessResult.CORRECT_ONE
