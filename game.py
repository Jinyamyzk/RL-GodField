from cards import Cards
from field import Field


class Game:
    def __init__(self, players: dict):
        self.players = players
        self.field = Field()
        self.cards = Cards()
        self.attack_player = "p1"
        self.defence_player = "p2"
        self.num_turn = 0
        self.done = False
        for _ in range(5):
            card = self.cards.draw()
            card_type = self.cards.deck[card].type
            self.players["p1"].draw_card(card, card_type)
            card = self.cards.draw()
            card_type = self.cards.deck[card].type
            self.players["p2"].draw_card(card, card_type)
    
    # 攻守交代
    def change_turn(self):
        if self.attack_player == "p1":
            self.attack_player = "p2"
            self.defence_player = "p1"
        else:
            self.attack_player = "p1"
            self.defence_player = "p2"

    def cal_damage(self, played_attack_card: int, played_defence_card: int = -1) -> int:
        attack_value = self.cards.deck[played_attack_card].use()
        defence_value = self.cards.deck[played_defence_card].use() if played_defence_card != -1 else 0
        damage = attack_value - defence_value
        damage = damage if damage > 0 else 0
        return damage
    
    def show_field(self, played_attack_card: int, played_defence_card: int, damage: int):
        self.num_turn += 1
        print("---------------------------------------")
        print(f"{self.num_turn}th turn")
        print(f"attack player: {self.attack_player}")
        print(f"hand: {self.players[self.attack_player].hand}")
        if played_attack_card == -1:
            print(f"pass")
        else:
            print(f"played attack card: {played_attack_card}")
            if played_defence_card != -1:
                print(f"defence player: {self.defence_player}")
                print(f"played defence card: {played_defence_card}")
            print(f"{self.defence_player} got {damage} damage. HP: {self.players[self.defence_player].hp}")
    
    def win(self, player: str):
        print(f"***** {player} Win!! *****")

    def play(self):
        while self.done != True:
            # print(f"hand: {self.players[self.attack_player].hand}")
            played_attack_card = self.players[self.attack_player].myturn()
            # print(played_attack_card)
            if played_attack_card != -1:
                played_defence_card = self.players[self.defence_player].defence()
                damage = self.cal_damage(played_attack_card, played_defence_card)
                self.players[self.defence_player].hp -= damage
                if self.players[self.defence_player].hp <= 0:
                    self.done = True
                    self.win(self.attack_player)
                    continue
                else:
                    # カードを使ったプレイヤーにカードを配る
                    card = self.cards.draw()
                    self.players[self.attack_player].draw_card(card, self.cards.deck[card].type)
                    if played_defence_card != -1:
                        card = self.cards.draw()
                        self.players[self.defence_player].draw_card(card, self.cards.deck[card].type)
                self.show_field(played_attack_card, played_defence_card, damage)
            else:
                # passすればカードを配る
                card = self.cards.draw()
                self.players[self.attack_player].draw_card(card, self.cards.deck[card].type)
                self.show_field(-1, -1, 0)
            self.change_turn()
            
            

