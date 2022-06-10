from game import Game
from player import QLearningPlayer, RandomPlayer
from attackCard import AttackCard
from field import Field
from q_learning_nn import QLearningAgent

def run():
    player1 = RandomPlayer()
    player2 = RandomPlayer()
    players = {"p1": player1, "p2": player2}
    game = Game(players)
    action = player1.myturn()
    attack_flg = 1
    next_state, reward, done = game.step(attack_flg ,action)
    print(next_state)

def q_learning():
    player1 = QLearningPlayer()
    player2 = RandomPlayer()
    players = {"p1": player1, "p2": player2}
    game = Game(players)
    state = game.reset()
    for _ in range(3):
        print(player1.hand)
        if game.attack_player == "p1":
            action = player1.myturn(state)
        else:
            action = player1.defence(state)
        next_state, reward, done = game.step(action)
        print(next_state)

if __name__ == "__main__":
    q_learning()