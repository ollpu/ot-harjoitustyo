import random
from enum import Enum

class GuessResult(Enum):
    INCORRECT = 0
    CORRECT_ONE = 1
    CORRECT_ROUND_COMPLETE = 2

class GameService:
    def __init__(self):
        self.game = None
        self.current_round = None
        self.round = None
        self.texts_left = []
        self.images = []
        self.images_used = []

    def reset(self):
        self.__init__()

    def start_game(self, game):
        self.game = game
        self.current_round = 0
        self._load_round()

    def _load_round(self):
        self.round = self.game.rounds[self.current_round]
        self.texts_left = [(text, i) for i, (text, _) in enumerate(self.round.pairs)]
        random.shuffle(self.texts_left)
        self.images = [(image, i) for i, (_, image) in enumerate(self.round.pairs)]
        random.shuffle(self.images)
        self.images_used = [False]*len(self.round.pairs)

    def next_round(self):
        self.current_round += 1
        if self.current_round >= len(self.game.rounds):
            self.reset()
            return False
        else:
            self._load_round()
            return True

    def get_text(self):
        if not self.texts_left:
            return None
        else:
            return self.texts_left[-1][0]

    def get_images(self):
        """
        Retuns an array of tuples (image, index). The order is shuffled at the
        start of the round, so it can be used to lay out the images.
        """
        return self.images

    def get_used_images(self):
        """
        Returns an array of booleans, where the index i is True if that image
        has already been used.
        """
        return self.images_used

    def submit_guess(self, index):
        """
        Guess that the current text corresponds to the image `index`.
        """
        if index != self.texts_left[-1][1]:
            return GuessResult.INCORRECT
        else:
            self.images_used[index] = True
            self.texts_left.pop()
            if not self.texts_left:
                return GuessResult.CORRECT_ROUND_COMPLETE
            else:
                return GuessResult.CORRECT_ONE
