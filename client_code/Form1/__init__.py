from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
# Battle Royale Game

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 200

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been eliminated!")

class Game:
    def __init__(self, players):
        self.players = players

    def start_battle(self):
        while len(self.players) > 1:
            attacker = random.choice(self.players)
            defender = random.choice([p for p in self.players if p != attacker])
            damage = random.randint(10, 30)
            print(f"{attacker.name} attacks {defender.name} for {damage} damage!")
            defender.take_damage(damage)

            if defender.health <= 0:
                self.players.remove(defender)

        print(f"{self.players[0].name} is the winner!")

# Example usage
if __name__ == "__main__":
    player_names = ["Player1", "Player2", "Player3", "Player4"]
    players = [Player(name) for name in player_names]
    game = Game(players)
    game.start_battle()
