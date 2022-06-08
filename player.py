import random
class Player():
    def __init__(self):
        self.hp = 40
        self.hand = {"attack":[], "defence":[]}
    
    def draw_card(self, card: int, card_type: str):
        self.hand[card_type].append(card)
    
    def isattackable(self):
        return True if len(self.hand["attack"]) > 0 else False
    
    def isdefencable(self):
        return True if len(self.hand["defence"]) > 0 else False


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()   
    def myturn(self) -> int:
        if self.isattackable() == False:
            return -1
        random.shuffle(self.hand["attack"])
        played_card = self.hand["attack"].pop()
        return played_card
    
    def defence(self) -> int:
        if self.isdefencable() == False:
            return -1
        random.shuffle(self.hand["defence"])
        played_card = self.hand["defence"].pop()
        return played_card
