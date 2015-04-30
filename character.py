from random import randint, choice
from female_first import *
from male_first import *

class Character(object):
  
    dead = set()
    born = set()

    def __init__(self, space):
        self.gender = choice(["female", "male"])
        self.name = self.first_name_gen()
        self.space = space
        self.birth_year = 0
        self.age = 0
        self.relations = dict() #maps characters to ints
        self.action_log = list() #says what someone did, when, where, how, why

    def get_year(self):
        return str(" in year " + str(self.birth_year + self.age))

    def create_entry(self, action):
        return self.name + " " + action + self.get_year() + "."

    def first_name_gen(self):
        if self.gender == "female":
            return choice(female_first_list)
        return choice(male_first_list)

    def make_decision(self):
        roll = randint(0, 1) 
        if roll:
            self.spawn()
        else:
            self.die()

    def spawn(self):
        child = Character(self.space)
        child.birth_year = self.birth_year + self.age
        child.relations[self] = 1
        self.relations[child] = 1
        self.action_log.append(self.create_entry("spawned child"))
        Character.born.add(child)

    def die(self):
        self.action_log.append(self.create_entry("died"))
        Character.dead.add(self)

    def befriend(self, other):
        pass
