from random import choice


# Initial states
triads = {'000': [0, 0],
          '001': [0, 0],
          '010': [0, 0],
          '011': [0, 0],
          '100': [0, 0],
          '101': [0, 0],
          '110': [0, 0],
          '111': [0, 0]}
capital = 1000
next_round = True


# Taking from user input only "0" and "1"
def new_piece():
    user_input = input("Print a random string containing 0 or 1:\n")
    for letter in user_input:
        if letter not in "01":
            user_input = user_input.replace(letter, "")
    return user_input


# Creating dictionary with triads based on user input
def analyze(bin_code):
    global triads

    for i in range(0, len(bin_code) - 3):
        current_chunk = bin_code[i:i+3]
        if bin_code[i+3] == '0':
            triads[current_chunk][0] += 1
        else:
            triads[current_chunk][1] += 1


def printer():
    for key, value in triads.items():
        print(key, value)


# Prediction based on triads and result
def prediction():
    global triads
    global capital
    global next_round

    predicted_string = str()
    user_input = input("\nPrint a random string containing 0 or 1:\n")
    if user_input == 'enough' or capital <= 0:
        print("Game over!")
        next_round = False
    elif "1" not in user_input or "0" not in user_input:
        next_round = True
    else:
        for letter in user_input:
            if letter not in "01":
                user_input = user_input.replace(letter, "")
        for _ in range(3):
            predicted_string += choice("01")
        for i in range(len(user_input) - 3):
            for key, value in triads.items():
                if user_input[i:i+3] == key:
                    if value[0] > value[1]:
                        predicted_string += "0"
                    elif value[0] == value[1]:
                        predicted_string += choice("01")
                    else:
                        predicted_string += "1"
        print(f'prediction:\n{predicted_string}')
        right = 0
        wrong = 0
        for i in range(3, len(predicted_string)):
            if user_input[i] == predicted_string[i]:
                right += 1
            else:
                wrong += 1
        print(f'\nComputer guessed right {right} out of {len(user_input) - 3} symbols '
              f'({round(right / (len(user_input) - 3) * 100, 2)} %)')
        capital += wrong - right
        print(f"Your capital is now ${capital}")
        # printer()
        analyze(user_input)
        next_round = True


def start():
    print('Please give AI some data to learn...')
    print('Current data length is 0, 100 symbols left')
    bin_code = new_piece()
    while len(bin_code) < 100:
        print(f'Current data length is {len(bin_code)}, {100 - len(bin_code)} symbols left')
        bin_code += new_piece()
    print("You have $1000. Every time the system successfully predicts your next press, you lose $1.\n"
          "Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!")
    analyze(bin_code)


start()
prediction()
while next_round:
    prediction()
