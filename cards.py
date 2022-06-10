import numpy as np
from attackCard import AttackCard
from defenceCard import DefenceCard

class Cards():
    def __init__(self):
        self.num_cards = 6
        self.deck = {}
        self.deck[0] = AttackCard(1)
        self.deck[1] = AttackCard(5)
        self.deck[2] = AttackCard(10)
        self.deck[3] = DefenceCard(1)
        self.deck[4] = DefenceCard(5)
        self.deck[5] = DefenceCard(10)
        
        self.deck_probs = {}
        for i in range(self.num_cards):
            self.deck_probs[i] = 1/self.num_cards
    
    def __len__(self):
        return len(self.deck)
    
    def draw(self) -> int:
        cards = list(self.deck_probs.keys())
        probs = list(self.deck_probs.values())
        return np.random.choice(cards, p=probs)
        