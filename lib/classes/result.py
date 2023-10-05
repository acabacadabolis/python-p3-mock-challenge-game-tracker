from classes.player import Player 
from classes.game import Game

class Result:
    def __init__(self, player, game, score):
        self.player = player
        player.results.append(self)
        self.game = game
        game.results.append(self)
        self.score = score

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if (type(new_score) != type(1)) or (new_score > 5000) or (new_score < 1):
            raise ValueError("Invalid score")
        self._score = new_score

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        if (not isinstance(new_player, Player)):
            raise ValueError("Invalid player")
        self._player = new_player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        if (not isinstance(new_game, Game)):
            raise ValueError("Invalid game")
        self._game = new_game
