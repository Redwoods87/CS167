# wget http://cs.whitman.edu/~davisj/cs/167/2016F/exmpls/dictionaries.py 

def add_fruit(inventory, fruit, quantity):
    """ Add the specified quantity of fruit to the inventory.
    Parameters:
        inventory, a dictionary mapping names to quantities
        fruit, a string naming a type of fruit
        quantity, a positive number
    Produces: Nothing; called for its side effects.
    Preconditions: No additional.
    Postconditions: fruit in inventory, 
                    inventory[fruit] is increased by quantity
    """
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity
    return

def test_add_fruit():
    new_inventory = {}
    add_fruit(new_inventory, "strawberries", 10)
    assert "strawberries" in new_inventory
    assert new_inventory["strawberries"] == 10
    add_fruit(new_inventory, "strawberries", 25)
    assert new_inventory["strawberries"] == 35

def print_seniors(roster, year):
    """ Given a roster, print names of students graduating this year.
    Parameters: 
        roster, a dictionary mapping names to class years
        year, the current graduation year as an integer
    Produces:
        Nothing, called for its side effects
    """
    #for name in roster.keys():
    #    classyear = roster[name]
    #    if classyear == year:
    #        print(name)
    for (name, classyear) in roster.items():
        if classyear == year:
            print(name)

def test_print_seniors():
    roster = {"Nathaniel": 2019, "Kyler": 2020, "Jesse": 2018,
              "Nobody": 2017}
    print_seniors(roster, 2017)

def print_letter_frequencies(string):
    """ Print number of occurrences of each letter in string, ignoring case.
    """
    freq = {}
    # Counting up the characters in string
    for char in string.lower():
         if char in freq:
             freq[char] += 1
         else:
             freq[char] = 1
    # Print out table of characters and frequencies
    # See http://stackoverflow.com/questions/28039155/dict-items-object-has-no-attribute-sortreplace-min
    # for reference to sorted()
    for char in sorted(freq.keys()):
        print(char, freq[char])

    print()

    # CHALLENGE: Print table sorted by frequency, instead of alphabetically
    # Does this sort by values? No, it still sorts by keys.
    for (char, fr) in sorted(freq.items()):
        print(char, fr)

if __name__=='__main__':
    test_add_fruit()
    test_print_seniors()
    print_letter_frequencies("Supercalifragilisticexpialidocious")
