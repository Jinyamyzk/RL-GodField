from numpy import average
from game import Game
from player import QLearningPlayer, RandomPlayer
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
    player1 = QLearningPlayer()
    player2 = RandomPlayer()
    players = {"p1": player1, "p2": player2}
    game = Game(players)

    episodes = 100
    loss_history = []
    reward_history = []
    for episode in range(episodes):
        state = game.reset()
        total_loss, total_reward, cnt = 0, 0, 0
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
        total_reward += reward
        if episode % 10 == 0:
            reward_history.append(total_reward / 10)
            total_reward = 0
        average_loss = total_loss / cnt
        loss_history.append(average_loss)
    plt.plot(reward_history)
    plt.show()

        


if __name__ == "__main__":
    q_learning()