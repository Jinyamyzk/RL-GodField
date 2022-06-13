class AttackCard():
    def __init__(self, attack_value):
        self.attack_value = attack_value
        self.type = "attack"
    
    def use(self):
        return self.attack_value

class DarknessAttackCard(AttackCard):
    def __init__(self, attack_value):
        super().__init__(attack_value)
        self.element = "darkness"