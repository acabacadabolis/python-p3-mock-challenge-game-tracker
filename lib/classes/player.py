class Player:
    def __init__(self, username):
        self.username = username
        self.results = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if (len(new_username) < 2) or (type(new_username) != type("asd")) or (len(new_username) > 16):
            raise ValueError("Invalid username")
        self._username = new_username
    
    def games_played(self):
        games = []
        for result in self.results:
            games.append(result.game)
        return games
    
    def has_played_game(self, game):
        played = False
        for result in self.results:
            if result.game == game:
                played = True
        return played
    
    def num_times_played(self, game):
        played = [1 for result in self.results if result.game == game]
        return sum(played)