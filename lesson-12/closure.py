# Closure is a function that remembers its parent's scope after the parent function has returned
def parent_function(person):
    coins = 4

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " has no coins left.")

    # returns an inner function
    return play_game


# calling a closure
tommy = parent_function("Tommy")
tommy()  # Tommy has 3 coins left.
tommy()  # Tommy has 2 coins left.
tommy()  # Tommy has 1 coin left.
tommy()  # Tommy has no coins left.
