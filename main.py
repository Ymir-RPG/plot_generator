from character import Character

INIT_POP_SIZE = 10

def main():
    space = set()
    for _ in range(INIT_POP_SIZE):
        space.add(Character(space))
    time_loop(space)

def time_loop(space):
    while space:
        for character in space:
            character.make_decision()
            character.age += 1
        add_born()
        remove_dead()
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
