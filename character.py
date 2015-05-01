from random import randint, choice
from female_first import *
from male_first import *
from last import last_name_list

class Character(object):
  
    dead = set()
    born = set()

    def __init__(self, space):
        self.gender = choice(["female", "male"])
        self.first_name = self.first_first_name_gen()
        self.last_name = choice(last_name_list) 
        self.space = space
        self.birth_year = 0
        self.age = 0
        self.relations = dict() #maps characters to ints
        self.action_log = list() #says what someone did, when, where, how, why

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_year(self):
        return str(" in year " + str(self.birth_year + self.age))

    def create_entry(self, action):
        return str(self) + " " + action + self.get_year() + "."

    def first_first_name_gen(self):
        if self.gender == "female":
            return choice(female_first_list)
        return choice(male_first_list)

    def get_greatest_enemy(self):
        greatest_enemy = (None, 0) 
        for key in self.relations:
            if self.relations[key] < greatest_enemy[1]:
                greatest_enemy = (key, self.relations[key])
        return greatest_enemy[0]

    def make_decision(self):
        roll = randint(0, 3)
        if roll == 0:
            self.spawn()
        elif roll == 1:
            self.die()
        elif roll == 2:
            relation = choice(list(self.space)) #O(n), find way to fix
            if relation != self:
                self.effect_other(relation, choice([-1, 1]))
        elif roll == 3 and self.get_greatest_enemy() in self.space:
            self.kill(self.get_greatest_enemy())

    def spawn(self):
        child = Character(self.space)
        child.birth_year = self.birth_year + self.age
        child.last_name = self.last_name
        child.relations[self] = 1
        self.relations[child] = 1
        self.action_log.append(self.create_entry("spawned " + str(child)))
        Character.born.add(child)

    def kill(self, other):
        print("#############")
        other.action_log.append(other.create_entry("was killed by " + str(self)))
        self.action_log.append(self.create_entry("killed " + str(other)))
        Character.dead.add(other)

    def die(self):
        self.action_log.append(self.create_entry("died"))
        Character.dead.add(self)

    def effect_other(self, other, effect):
        assert self != other
        if other in self.relations:
            self.relations[other] += effect
        else:
            self.relations[other] = effect
        if self in other.relations:
            other.relations[self] += effect
        else:
            other.relations[self] = effect
        if effect < 0:
            self.action_log.append(self.create_entry("harmed " + str(other)))
        elif effect > 0:
            self.action_log.append(self.create_entry("helped " + str(other)))
