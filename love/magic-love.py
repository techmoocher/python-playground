from termcolor import colored
import emoji
import os



def heart():
    print("Enter your name as the INPUT then I will make your life colorful and add magic to it as OUTPUT!")
    name = input("""Your input here .....
>>> ..... """)
    heart= ('\n'.join([''.join([(name[(x-y) % len(name)]
                             if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ')
                            for x in range(-30, 30)]) for y in range(30, -30, -1)]))
    print(emoji.emojize(u':kissing_heart:'))
    print(colored(heart, 'red'))

def replay():
    ask_replay = input("""Do you wish to replay this? (Yes or No)
(case-sensitive)
>>> """)
    if ask_replay == 'YES' or ask_replay == 'Yes' or ask_replay == 'yes':
        print()
        return True
    elif ask_replay == 'NO' or ask_replay == 'No' or ask_replay == 'no':
        print()
        return False
    else:
        print('Sorry? What do you mean?')
        print()
        replay()

heart()

user_replay = replay()

while user_replay == True:
    heart()
    os.system('cls')
    user_replay = replay()

print('Bye ..... Sorry to see you go.')