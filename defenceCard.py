from card import Card


class DefenceCard(Card):
    def __init__(self, prob, defence_value):
        super().__init__(prob)
        self.defence_value = defence_value
        self.type = "defence"
    
    def use(self):
        return self.defence_value