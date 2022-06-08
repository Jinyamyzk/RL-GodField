class AttackCard():
    def __init__(self, attack_value):
        self.attack_value = attack_value
        self.type = "attack"
    
    def use(self):
        return self.attack_value