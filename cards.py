import numpy as np
from attackCard import AttackCard, DarknessAttackCard
from defenceCard import DefenceCard

class Cards():
    def __init__(self):
        self.num_cards = 7
        self.deck = {}
        self.deck[0] = AttackCard(1)
        self.deck[1] = AttackCard(5)
        self.deck[2] = AttackCard(10)
        self.deck[3] = DefenceCard(1)
        self.deck[4] = DefenceCard(5)
        self.deck[5] = DefenceCard(10)
        self.deck[6] = DarknessAttackCard(5)
        
        self.deck_probs = {}
        for i in range(6):
            self.deck_probs[i] = 0.95 / 6
        self.deck_probs[6] = 0.05
    
    def __len__(self):
        return len(self.deck)
    
    def draw(self) -> int:
        cards = list(self.deck_probs.keys())
        probs = list(self.deck_probs.values())
        return np.random.choice(cards, p=probs)
        