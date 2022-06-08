class DefenceCard():
    def __init__(self, defence_value):
        self.defence_value = defence_value
        self.type = "defence"
    
    def use(self):
        return self.defence_value