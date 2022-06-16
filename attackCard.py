from card import Card


class AttackCard(Card):
    def __init__(self, prob, attack_value):
        super().__init__(prob)
        self.attack_value = attack_value
        self.type = "attack"
    
    def use(self):
        return self.attack_value

class DarknessAttackCard(AttackCard):
    def __init__(self, prob, attack_value):
        super().__init__(prob, attack_value)
        self.element = "darkness"