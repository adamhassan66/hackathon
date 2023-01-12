from python.hackathon.card import Card
from python.hackathon.deck import Deck


class User:
  def __init__(self,name,):
    self.name = name
    self.hand =[]

    def draw(deck):
      self.hand.append(deck.draw_top())
