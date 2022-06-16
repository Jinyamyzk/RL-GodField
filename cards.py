import numpy as np
from attackCard import AttackCard, DarknessAttackCard
from defenceCard import DefenceCard

class Cards():
    def __init__(self):
        self.num_cards = 21
        self.deck = {}
        self.deck[0] = AttackCard(2/41, 1)
        self.deck[1] = AttackCard(2/41, 2)
        self.deck[2] = AttackCard(2/41, 3)
        self.deck[3] = AttackCard(2/41, 4)
        self.deck[4] = AttackCard(2/41, 5)
        self.deck[5] = AttackCard(2/41, 6)
        self.deck[6] = AttackCard(2/41, 7)
        self.deck[7] = AttackCard(2/41, 8)
        self.deck[8] = AttackCard(2/41, 9)
        self.deck[9] = AttackCard(2/41, 10)
        self.deck[10] = DefenceCard(2/41, 1)
        self.deck[11] = DefenceCard(2/41, 2)
        self.deck[12] = DefenceCard(2/41, 3)
        self.deck[13] = DefenceCard(2/41, 4)
        self.deck[14] = DefenceCard(2/41, 5)
        self.deck[15] = DefenceCard(2/41, 6)
        self.deck[16] = DefenceCard(2/41, 7)
        self.deck[17] = DefenceCard(2/41, 8)
        self.deck[18] = DefenceCard(2/41, 9)
        self.deck[19] = DefenceCard(2/41, 10)
        self.deck[20] = DarknessAttackCard(1/41, 5)
        
        self.deck_probs = {}
        for i in range(self.num_cards):
            self.deck_probs[i] = self.deck[i].prob
    
    def __len__(self):
        return len(self.deck)
    
    def draw(self) -> int:
        cards = list(self.deck_probs.keys())
        probs = list(self.deck_probs.values())
        return np.random.choice(cards, p=probs)

if __name__ == "__main__":
    cards = Cards()
    print(sum(cards.deck_probs.values()))
        