import random
from q_learning_nn import QLearningAgent
from util.remove_one_from_redundant_list import remove_just_one
class Player():
    def __init__(self):
        self.INITIAL_HP = 10
        self.hp = self.INITIAL_HP
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

class QLearningPlayer(Player):
    def __init__(self, action_size):
        super().__init__()
        self.agent = QLearningAgent(action_size)

    def myturn(self, state) -> int:
        if self.isattackable() == False:
            return -1
        played_card = self.agent.get_action(state, self.hand["attack"])
        self.hand["attack"] = remove_just_one(self.hand["attack"], played_card)
        return played_card
    
    def defence(self, state):
        if self.isdefencable() == False:
            return -1
        played_card = self.agent.get_action(state, self.hand["defence"])
        self.hand["defence"] = remove_just_one(self.hand["defence"], played_card)
        return played_card

class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
    
    def myturn(self):
        print("hand: ", self.hand["attack"])
        if self.isattackable() == False:
            return -1
        played_card = -1
        while played_card not in self.hand["attack"]:
            played_card = int(input("choose attack card: "))
        self.hand["attack"] = remove_just_one(self.hand["attack"], played_card)
        return played_card
    
    def defence(self) -> int:
        print("hand: ", self.hand["defence"])
        if self.isdefencable() == False:
            return -1
        played_card = -1
        while played_card not in self.hand["defence"]:
            played_card = int(input("choose defence card: "))
        self.hand["defence"] = remove_just_one(self.hand["defence"], played_card)
        return played_card
