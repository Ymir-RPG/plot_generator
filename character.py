from random import randint

class Character(object):
  
    dead = set()
    born = set()

    def __init__(self, space):
        self.space = space
        self.birth_year = 0
        self.age = 0
        self.action_log = list() #says what someone did, when, where, how, why

    def get_year(self):
        return str(" in year " + str(self.birth_year + self.age))

    def make_decision(self):
        roll = randint(0, 1) 
        if roll:
            self.spawn()
        else:
            self.die()

    def spawn(self):
        child = Character(self.space)
        child.birth_year = self.birth_year + self.age
        self.action_log.append("spawned child" + self.get_year())
        Character.born.add(child)

    def die(self):
        self.action_log.append("died" + self.get_year())
        Character.dead.add(self)
