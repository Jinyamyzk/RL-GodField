from cards import Cards
from field import Field
import numpy as np
from typing import Literal


class Game:
    def __init__(self, players:dict):
        self.players = players
        self.field = Field()
        self.cards = Cards()
        self.attack_player = "p1"
        self.defence_player = "p2"
        self.num_turn = 0
        self.done = False
        self.com_played_attack_card = -1
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

    # ダメージ計算, HP反映
    def cal_damage(self, played_attack_card: int, played_defence_card: int = -1) -> int:
        attack_value = self.cards.deck[played_attack_card].use()
        defence_value = self.cards.deck[played_defence_card].use() if played_defence_card != -1 else 0
        damage = attack_value - defence_value
        damage = damage if damage > 0 else 0 # デフェンスが超過した場合0にする
        if self.cards.deck[played_attack_card].element=="darkness" and damage > 0: # Darknessのダメージを受けた場合負け
            damage = self.players[self.defence_player].hp
            self.players[self.defence_player].hp = 0
        else:
            self.players[self.defence_player].hp -= damage
        return damage
    
    def show_field(self, played_attack_card: int, played_defence_card: int, damage: int):
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
    
    def step(self, action:int)->tuple[list[int], Literal[-1,0,1], bool]:
        if self.attack_player == "p1":
            next_state, reward =  self.p1_attack(action)
        else:
            next_state, reward = self.p1_defence(action)
        self.num_turn += 1
        return next_state, reward, self.done

    def p1_attack(self, action:int) -> tuple[list[int], Literal[1, 0]]:
        reward = 0
        played_card = []
        attack_flg = 0
        if action != -1:
            played_defence_card = self.players[self.defence_player].defence()
            damage = self.cal_damage(action, played_defence_card)
            played_card.extend([action, played_defence_card])
            if self.players[self.defence_player].hp <= 0:
                self.done = True
                reward = 1
                # self.win(self.attack_player)
            else:
                # カードを使ったプレイヤーにカードを配る
                card = self.cards.draw()
                self.players[self.attack_player].draw_card(card, self.cards.deck[card].type)
                if played_defence_card != -1:
                    card = self.cards.draw()
                    self.players[self.defence_player].draw_card(card, self.cards.deck[card].type)
            # self.show_field(action, played_defence_card, damage)
        else:
            # passすればカードを配る
            card = self.cards.draw()
            self.players[self.attack_player].draw_card(card, self.cards.deck[card].type)
            # self.show_field(-1, -1, 0)
        self.change_turn()

        # comのアタック
        self.com_played_attack_card = self.players[self.attack_player].myturn()
        if self.com_played_attack_card != -1:
            played_card.append(self.com_played_attack_card)
        else: #comがパス
            self.change_turn()
            attack_flg = 1 # もう一回アタック

        next_state = self.state2vec(self.players["p1"].hand, self.players["p1"].hp, self.players["p2"].hp, played_card, attack_flg)
        return next_state, reward 
    
    def p1_defence(self, action:int) -> tuple[list[int], Literal[-1, 0]]:
        reward = 0
        played_card = []
        attack_flg = 1
        damage = self.cal_damage(self.com_played_attack_card, action)
        
        # self.show_field(self.com_played_attack_card, action, damage)
        # カードを配る
        card = self.cards.draw()
        self.players[self.attack_player].draw_card(card, self.cards.deck[card].type)
        if action != -1:
            card = self.cards.draw()
            self.players[self.defence_player].draw_card(card, self.cards.deck[card].type)
        if self.players[self.defence_player].hp <= 0:
            self.done = True
            reward = -1
            # self.win(self.attack_player)
        else:
            self.change_turn()
        next_state = self.state2vec(self.players["p1"].hand, self.players["p1"].hp, self.players["p2"].hp, played_card, attack_flg)
        return next_state, reward
    
    # numpy.ndarrayを返す
    def state2vec(self, hand:dict[str: list[int]], myHP:int, enemyHP:int, played_card:list[int], attack_flg:int):
        hand_vec = np.zeros(self.cards.num_cards, dtype=np.float32)
        for cards in hand.values():
            for card in cards:
                hand_vec[card] += 1
        played_card_vec = np.zeros(self.cards.num_cards, dtype=np.float32)
        for card in played_card:
            played_card_vec[card] += 1
        state = np.array([attack_flg, myHP, enemyHP], dtype=np.float32)
        state = np.append(state, hand_vec)
        state = np.append(state, played_card_vec)
        return state
    
    def reset(self):
        self.attack_player = "p1"
        self.defence_player = "p2"
        self.num_turn = 0
        self.done = False
        played_card = []
        attack_flg = 1
        for player in self.players.values():
            player.hp = player.INITIAL_HP
            player.hand = {"attack":[], "defence":[]}
        
        for _ in range(5):
            card = self.cards.draw()
            card_type = self.cards.deck[card].type
            self.players["p1"].draw_card(card, card_type)
            card = self.cards.draw()
            card_type = self.cards.deck[card].type
            self.players["p2"].draw_card(card, card_type)
        return self.state2vec(self.players["p1"].hand, self.players["p1"].hp, self.players["p2"].hp, played_card, attack_flg)



