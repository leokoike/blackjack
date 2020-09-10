import random

def Valores():
    return [ "A", "2", "3", "4", "5", "6", "7","8", "9", "10", "J", "Q", "K"]

def Suits():
    return ["Ouro","Espadas","Copas","Paus"]

class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return str((self.value,self.suit))

class Deck:
    def __init__(self):
        self.cards = [Card(value,suit) for value in Valores() for suit in Suits()]
        random.shuffle(self.cards)
    def purchase(self):
        return self.cards.pop()
    def __len__(self):
        return len(self.cards)
    def __str__(self):
        return str([str(card) for card in self.cards])

class Player:
    def __init__(self):
        self.cards=[]
    def recive(self,card):
        self.cards.append(card)


