from random import randint, shuffle

global game_count
game_count = 0

def intro():
    print("""Hi! Welcome to GleanScreen, the pseudo-random algorithm decision-making method
    \nOur motto is: 'We make the decisions so you don't have to'.
    \nHow we work: First, input as many items as you'd like to choose between through either a csv 
    file or by typing them, 
    they can be numbers, names, book titles, foods, next on your revenge list, etc.
    \nOnce you're finished adding items, please type no or quit and 
    we'll take over from there!
    \n Happy Decision Making!""")


# initializes user_input variable and hold variable for looping error avoidance and subsequent


def decisions(user_input, hold):

    while True:
        if user_input.upper() != "DONE":

            user_input = input("Adding an item? What is it? \n(note: if you're done adding, simply type 'done') ")
            # adds an arrow between added elements for parsing into list
            # uniqueness of the symbol adds a wider range of functionality for the user
            if user_input != "done":
                hold += (user_input + "^")
        # checks for exit intention
        elif user_input[0].upper() == "N" or user_input[0].upper() == "Q" or user_input.upper() == "DONE":
            break

    return hold


def ending(hold):

    options = hold.split("^")

    # removes initialized space from string
    options.pop(options.index(""))
    shuffle(options)
    choice_index = randint(0, len(options) - 1)
    print(
        f"Congratulations!! Out of {len(options)} options we've made a decision for you! "
        f"You should choose: {options[choice_index]}"
    )
    user_input = input("Are you happy with your decision? Type Y/N: ")
    return user_input


user_input = "Y"
hold = ""

while True:
    if game_count < 1:
        intro()

    elif game_count >= 1:
        user_input = input("Would you like to decide something else? (Type Y/N) ")

    if "Y" in user_input.upper():
        place_string = decisions(user_input, hold)
        game_count += 1

        while True:
            if ending(place_string).upper() == "Y":
                break
            else:
                ending(place_string)

    else:
        print(f"Congratulations! You've made {game_count} decision(s) today!")
        break
