# Assignment: W02 Prove: Developer - Solo Code Submission
# Application: Tic-Tac-Toe
# Author: M. Naif Amoodi
# Credits:
# https://stackoverflow.com/a/21786287 - Printing colored text to console

# Initialize 3x3 grid with initial value of e (empty)
squares = [
    'e',
    'e',
    'e',
    'e',
    'e',
    'e',
    'e',
    'e',
    'e'
]

def display_squares():
    print()

    for i in range(0, 9):
        if squares[i] == 'x':
            print('x', end = '')
        elif squares[i] == 'o':
            print('o', end = '')
        else:
            print(i + 1, end = '')
        
        if i == 0 or i == 1 or i == 3 or i == 4 or i == 6 or i == 7:
            print('|', end = '')
        elif i == 2 or i == 5:
            print('\n-+-+-\n', end = '')
    
    print()
    print()


def get_square(message):
    try:
        square = int(input(message))
    except (ValueError) as error:
        # If the user enters anything other than a number between 1 and 9, set value of square to zero so as to trigger an error message
        square = 0

    return square

def is_square_empty(square):
    if squares[square - 1] == 'e':
        return True
    else:
        return False

def main():
    # x starts the game
    whose_turn = 'x'

    # loop indefinitely
    while(True):
        display_squares()

        square = get_square(f'{whose_turn}\'s turn to choose a square (1-9): ')

        if square >= 1 and square <= 9:
            result = is_square_empty(square)

            if result == True:
                squares[square - 1] = whose_turn
            else:
                print()
                # fancy characters print colored text to console
                print('\x1b[1;37;41m' + ' Error: That square is already taken '  + '\x1b[0m')
        else:
            print()
            print('\x1b[1;37;41m' + ' Error: Please enter a value between 1 and 9 '  + '\x1b[0m')

        # swap turns
        if whose_turn == 'x':
            whose_turn = 'o'
        else:
            whose_turn = 'x'

if __name__ == '__main__':
    main()

    