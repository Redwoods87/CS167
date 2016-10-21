# Problem 4.3.5
def zombieApocalypse(people):
    """
    A zombie can convert two peiople into zombies every day. Starting with one zombie, how long does it take for the entire world population (or 7 billions people) to become zombies?
    Produces a number of days.
    """
    
    zombies = 1
    days = 0
    while (people > 0):
        new_zombies = 2 * zombies
        zombies = zombies + new_zombies
        people = people - new_zombies
        days = days + 1
    return days

def vampireApocalypse(v, k, vampires, people):
    """
    Vampires can each convert v people a day into vampires.  However, there is a band of vampires starts with the given number, how long before a town with a given population becomes a town with no people left in it?
    """
    days = 0
    while (people > 0):
        new_vampires = v * vampires
        people = people - new_vampires
        vampires = vampires + new_vampires - k
        days = days + 1
    return days

def main():
    print("Days until zombie apocalypse: " + str(zombieApocalypse(7e9)))
    print("Days until vampire apocalyse: " + str(vampireApocalypse(2, 2, 5, 32e3)))
    
main()