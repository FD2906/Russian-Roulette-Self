from random import randint

# --- Creates a list of characters, depending on the amount of players entered --- #
def character_count(count):
    characters = []
    for number in range(1, count + 1):
        character_name = 'Character ' + str(number)
        characters.append(character_name)
    return characters

# --- Allows you to pick from a list of revolvers, which will be used in the storyline. --- #
def revolver_selection(revolver_name):
    revolvers = ['.44 Magnum', 'Nagant M1895', '.357 Magnum']
    if revolver_name in revolvers:
        print('Your revolver has been chosen.')
        print('Your revolver is: ' + revolver_name + '.')
        return revolver_name
    else:
        print('That revolver doesn\'t exist.')
        return

# --- Allows you to pick from two time options (Day, Night) and two place options (Kitchen, Bar) --- #
# --- Note: can i experiment with using a dictionary in this area, pass in a time or place use .get() function to find a value from a key called time (or day), and check it against it? --- #
def storyline(time_in_day, place_in_game): 
    if time_in_day == 'Day':
        print('It is daytime. The sun is shining outside.')
    elif time_in_day == 'Night':
        print('It is nighttime. It is dark outside.')
    else:
        print('This time doesn\'t exist.')

    if len(number_of_characters) == 1:
        if place_in_game == 'Kitchen':
            print('You are alone in the kitchen. You take out your ' + revolver_choice + '. You decided to play some Russian Roulette.')
        elif place_in_game == 'Bar':
            print('You are alone in the back of the bar. You take out your ' + revolver_choice + '. You decided to play some Russian Roulette.')
    elif len(number_of_characters) != 1:
        if place_in_game == 'Kitchen':
            print('You are with your friends in the kitchen. You take out your ' + revolver_choice + '. You decided to play some Russian Roulette with your friends.')
        elif place_in_game == 'Bar':
            print('You are with your friends in the back of the bar. You take out your ' + revolver_choice + '. You decided to play some Russian Roulette with your friends.')

        

number_of_characters = character_count(1)
#print(number_of_characters)
revolver_choice = revolver_selection('.44 Magnum')
#print(revolver_choice)
storyline('Night', 'Bar')
    