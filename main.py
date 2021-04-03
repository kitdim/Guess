def GuessNumber(a, b, i):
    while True:
        a += 1
        b = int(input('Write the number: '))

        if b == i:
            print(f'You win!!!\n'
                  f'Try № {a}')
            break
        elif b < i:
            print(f'The number is bigger, try again\n'
                  f'Try № {a}')
        else:
            print(f'The number is less, try again\n'
                  f'Try № {a}')
    else:
        print('Done')


print('Guess the number!!!')
_try = 0
number = 0
guess = 15

GuessNumber(_try, number, guess)



