"""
The Monty Hall problem is a brain teaser, in the form of a probability puzzle, loosely based on the American
television game show Let's Make a Deal and named after its original host, Monty Hall.
The problem was originally posed (and solved) in a letter by Steve Selvin to the American Statistician in 1975.

Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats.
You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat.
He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

"""

# ----------------------------------------------------- #
import random


def monte_hall(runs, nr_of_doors, choice):
    """
    runs: Number of iterations to run
    nr_of_doors: Number of doors that can be selected. All but one will be opened after initial selection.
    choice: whether to 'stick' to first choice, or 'switch' after the doors are opened.
    """

    hits = 0

    pick_options = [i for i in range(nr_of_doors)]

    for i in range(runs):
        doors = [1] + [0 for i in range(nr_of_doors-1)]
        random.shuffle(doors)
        # print(doors)

        # pick a door nr
        picked = random.choice(pick_options)
        result = doors[picked]

        if choice == 'stick':
            if result == 1:
                hits += 1

        if choice == 'switch':
            # open doors not containing prize
            for y in range(len(doors)):
                if y != picked:
                    if doors[y] != 1:
                        doors[y] = '*'  # door is revealed

            # switch to remaining closed door
            for y in range(len(doors)):
                if y != picked and doors[y] != '*':
                    result = doors[y]
                    if result == 1:
                        hits += 1

    hit_rate = round((hits / runs) * 100, 2)

    return hit_rate

# ----------------------------------------------------- #

runs = 1000
doors = 3
choice = 'stick'

hit_rate = monte_hall(runs=runs, nr_of_doors=doors, choice=choice)

_str = 'Choice: ' + str.upper(choice) + ' - From ' + str(doors) + ' doors, you achieved a hit rate of: '
_str += str(hit_rate) + '% over ' + str(runs) + ' iterations.'
print(_str)