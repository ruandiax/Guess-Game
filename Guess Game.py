from random import shuffle

mylist = [' ','O',' ']

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    
    guess=''
    
    while guess not in ['0','1','2']:
        guess= input("Pick a number: 0,1 or 2 \n")
        
    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong Guess!')
        print(mylist)

# Initial List
mylist = [' ','O',' ']

# Shuffle List
mixedup_list = shuffle_list(mylist)

# User Guess
guess = player_guess()

# Check Guess
check_guess(mixedup_list,guess)