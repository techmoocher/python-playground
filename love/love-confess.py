from termcolor import colored
import emoji
import time



print("Hey, will you be the INPUT to my life?")
time.sleep(2)
print("I will make your life colorful and add magic to it as OUTPUT till your last breath!")
time.sleep(5)
print()

print("Loving you is like breathing ... I just can't stop on purpose!")
time.sleep(5)
print()

print("Hardly my day goes by if I do not see you at least once!")
time.sleep(5)
print()

print("I will make your life easier too!")
time.sleep(3)
print("You do not have to declare your emotions to me like you declare to others.")
time.sleep(5)
print()

print("If your heart was a prison, I would want to be sentenced to life!")
time.sleep(5)
print()

print("Were your parents thieves? Cuz they stole the stars from the sky and put them in your eyes.")
time.sleep(5)
print()

print("I bet nothing even all the fireworks in the world can light up my world like you do.")
time.sleep(5)
print()

print("If I could change the alphabet, I would put U and I together.")
time.sleep(5)
print()

print("Send me your picture, so I can send Santa for my wish list.")
time.sleep(5)
print()

print("I'd give up my life if I could command one smille of your eyes, one touch of your hand.")
time.sleep(5)
print()

print('Do you accept my love? You have two options: Yes or No.')
print(emoji.emojize('Take a minute to think before saying No since you may regret for not entering my life! :wink:\n', language = 'alias'))

love_answer = input("""Please enter Yes if you accept my love
Otherwise, please enter No .....""")
love_answer = love_answer.lower()

def nice_suprise():
    print(emoji.emojize("Enter your name and I will show you how much I love you! :kissing_heart:", language = 'alias'))
    time.sleep(0.2)
    name = input("Your name is ... ")
    heart= ('\n'.join([''.join([(name[(x-y) % len(name)]
                             if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ')
                            for x in range(-30, 30)]) for y in range(30, -30, -1)]))
    print(emoji.emojize(':heart:', language = 'alias'))
    print(colored(heart , 'red'))

if love_answer == 'yes':
    nice_suprise()
    
elif love_answer == 'no': 
    print(emoji.emojize('I am Heart Broken! :cry:', language = 'alias'))
        
    time.sleep(1)
    print()

    print("""Goodbye ..... Sorry to see you go!
Hope you could find someone better than me.""")
    exit()
    
else:
    print(emoji.emojize("""Sorry, I can not understand you.
It's never occured to me that someday I'm unable to understand you :confused:""", language = 'alias'))
        
    time.sleep(1)
    print()
    print(emoji.emojize('Goodbye ..... Sorry to see you go! :cry:', language = 'alias'))