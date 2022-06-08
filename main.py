from game import Game
from player import RandomPlayer
from attackCard import AttackCard
from field import Field

def run():
    player1 = RandomPlayer()
    player2 = RandomPlayer()
    players = {"p1": player1, "p2": player2}
    game = Game(players)
    game.play()

if __name__ == "__main__":
    run()