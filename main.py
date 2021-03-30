print('Guess the number!!!')
_try = 0
guess = 15

while True:
    _try += 1
    number = input('Write the number: ')
    number = int(number)

    if number == guess:
        print(f'You win!!!\n'
              f'Try № {_try}')
        break
    elif number < guess:
        print(f'The number is bigger, try again\n'
              f'Try № {_try}')
        continue
    else:
        print(f'The number is less, try again\n'
              f'Try № {_try}')
        continue

