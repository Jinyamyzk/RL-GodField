from numpy import average
from game import Game
from player import HumanPlayer, QLearningPlayer, RandomPlayer
import matplotlib.pyplot as plt


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
    player1 = QLearningPlayer(21)
    player2 = RandomPlayer()
    # player2 = HumanPlayer()
    players = {"p1": player1, "p2": player2}
    game = Game(players)

    episodes = 10000
    loss_history = []
    reward_history = []
    win_rate = 0
    for episode in range(episodes):
        state = game.reset()
        total_loss, cnt = 0, 0
        done = False

        while not done:
            # print(player1.hand)
            if game.attack_player == "p1":
                action = player1.myturn(state)
            else:
                action = player1.defence(state)
            next_state, reward, done = game.step(action)

            loss = player1.agent.update(state, action, reward, next_state, done)
            total_loss += loss
            cnt += 1
            state = next_state
        win_rate += 1 if reward == 1 else 0
        
        if episode % 100 == 0:
            win_rate = win_rate/100
            reward_history.append(win_rate)
            print(win_rate)
            win_rate = 0

        
        
        average_loss = total_loss / cnt
        loss_history.append(average_loss)
    plt.plot(loss_history)
    plt.show()
    print(reward_history)

        


if __name__ == "__main__":
    q_learning()