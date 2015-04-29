from random import randint

class Character(object):
  
    dead = set()
    born = set()

    def __init__(self, space):
        self.space = space

    def make_decision(self):
        roll = randint(0, 1) 
        if roll:
            self.spawn()
        else:
            self.die()

    def spawn(self):
        Character.born.add(Character(self.space))

    def die(self):
        Character.dead.add(self)
