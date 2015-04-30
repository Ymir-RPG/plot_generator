from character import Character

INIT_POP_SIZE = 5

def main():
    space = set()
    for _ in range(INIT_POP_SIZE):
        space.add(Character(space))
    time_loop(space)

def time_loop(space):
    year = 0
    while space:
        for character in space:
            character.age += 1
            character.make_decision()
        add_born()
        remove_dead()
        year += 1
        print("year: " + str(year))
        print("population size: " + str(len(space)))

def add_born():
    for character in Character.born:
        character.space.add(character)
    Character.born = set()

def remove_dead():
    for character in Character.dead:
        print(character.action_log)
        character.space.remove(character)
    Character.dead = set()

if __name__ == "__main__":
    main()
