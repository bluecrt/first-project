right_guess = 0
while True:
    import random
    target = random.randint(1,10)
    guess_number = int(input('what number you guess is:'))
    
    if guess_number > target:
        print("too big！")
    elif guess_number < target and guess_number != 0:
        print('too small!')
    elif guess_number == target:
        right_guess += 1
        print('bingo，you are right for {} time(s)。'.format (right_guess))
    elif guess_number == 0:
        break