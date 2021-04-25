# """THIS IS THE GAME COWS AND BULLS"""
# def main():
from random import seed, randint

def create_secret_number():
    """create random number in [x, x, x, x] format"""
    seed()
    secret_num = []

    while len(secret_num) < 4:
        secret_digit = randint((int('0')), int('9'))
        if secret_digit not in secret_num:
            secret_num.append(secret_digit)
    return secret_num

def cow_bull(secret_num, player_num):
    """returns count of cows and bulls in a tuple (cows, bulls)"""
    cows = len([digit for digit in player_num if digit in secret_num])

    bulls = 0
    for i in range(len(player_num)):
        if player_num[i] == secret_num[i]:
            bulls += 1

    return cows, bulls

def get_player_num():
    """"gets player number and returns list with 4 digits [x, x, x, x]"""
    player_num = []
    while len(player_num) == 0:
        player_input = input('Please enter 4 digits: ').replace(' ', '')
        if player_input.isdigit() and len(player_input) == 4:
            player_num = [int(i) for i in player_input]
            return player_num

def another_game(state):
    if not state:
        play_again = input('Sorry, you ran out of tries! Would you like to play again?\n')
    else:
        play_again = input('Great! Would you like to play again?\n')

    if play_again in ['yes', 'y', 'Y', 'YES', 'Yes']:
        return play_game()
    else:
        return print('OK, Thank you for playing.')

def play_game():
    """"Main function to play the game. If won, or out of tries calls another_game()"""
    secret_num = create_secret_number()
    print(secret_num)

    for i in range(7):
        player_num = get_player_num()
        cows, bulls = cow_bull(secret_num, player_num)

        print(f'Try {i + 1} of 7 -> Cows: {cows}, Bulls: {bulls}')
        if bulls == 4:
            print(f'YOU WON!\n{player_num} is the secret number: {secret_num}.\n')
            another_game(True)

    return another_game(False)

    # play_game()


# if __name__ == '__main__':
#     pass