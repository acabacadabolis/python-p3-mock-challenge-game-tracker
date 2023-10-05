

class Game:
    def __init__(self, title="1"):
        self.title = title
        self.results = []
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if (len(new_title) == 0) or (type(new_title) != type("asd")):
            raise ValueError("Invalid Title")
        self._title = new_title

    def get_players(self):
        player_list = []
        for result in self.results:
            player_list.append(result.player)
        return player_list
    
    def average_score(self, player):
        scores = [result.score for result in self.results if result.player == player]
        return (sum(scores)/len(scores))
