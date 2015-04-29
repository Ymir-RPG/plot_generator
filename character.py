from random import randint

class Character(object):
  
    dead = set()
    born = set()

    def __init__(self, space):
        self.space = space
        self.action_log = list() #says what someone did, when, where, how, why

    def make_decision(self):
        roll = randint(0, 1) 
        if roll:
            self.spawn()
        else:
            self.die()

    def spawn(self):
        Character.born.add(Character(self.space))
        self.action_log.append("spawned child")

    def die(self):
        Character.dead.add(self)
        self.action_log.append("died")
