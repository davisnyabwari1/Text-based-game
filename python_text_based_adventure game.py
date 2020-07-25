import time

# Responses from the user

response_A = ['A', 'a']
response_B = ['B', 'b']
response_C = ['C', 'c']
response_Y = ['Yes', 'Y', 'y']
response_N = ['No', 'N', 'n']
required = '\n\nA,B,C are the only acceptable choices.Please select a new choice\n\n'


# GameOVer function:
def gameover():
    print('''
        \t:) GAME OVER!!!

          '''

          )


# game retrial function:
def retry():
    choice = input('Do you want to replay the game?Select Y or N: ')
    if choice in response_Y:
        intro()
    elif choice in response_N:
        print('')
        print("\tThank you for Playing the Game!!!")


# Introduction
def intro():
    print('\t\t\t\t\t\t\t--------------------------------------------------')
    print('\t\t\t\t\t\t\t\tWELCOME TO THE TEXT-BASED ADVENTURE GAME')
    print('\t\t\t\t\t\t\t--------------------------------------------------')
    print('You wake up out of a deep sleep and feel like your head is so heavy, your hands are tied to a chair and '
          'you are alone in the room.\nYou see a metal plate on the ground.What step will you take?')
    print('')
    # choices for the Player
    time.sleep(2)
    print('\tA:Sit and wait for you to be saved\n'
          '\tB:Try to get the metallic plate to untie yourself\n'
          '\tC:Drag yourself with the chair and stay in a corner so that you are not found')
    # Player response:

    choice = input('>>>')
    print('')
    if choice in response_A:
        print('Huh, that was too fast,You chose death, You died')
        gameover()
        retry()
    elif choice in response_B:
        escape()
    elif choice in response_C:
        print('Too easy, You died')
        gameover()
        print('')
        retry()
    else:
        print(required)
        intro()


def escape():
    print('After pulling yourself you get the metal plate and you manage to cut the ropes on your hands and legs.\n'
          'suddenly you hear some people talking heading to the room you are currently in.You')
    print('')
    time.sleep(2)
    print('\tA:Jump through the window of the room\n'
          '\tB:Hide yourself behind the door as they open it\n'
          '\tC:Open the door and walk out')
    choice = input('>>>')
    print('')
    if choice in response_A:
        run()
    elif choice in response_B:
        weapon()
    elif choice in response_C:
        print('Too easy, You were caught')
    else:
        print(required)
        intro()


def weapon():
    print('A man enters the room he has a knife and gun on his waist belt.Slowly choose a weapon from the waist belt:')
    print('')
    time.sleep(2)
    print('\tA:knife\n'
          '\tB:Gun\n')
    choice = input('>>>')
    print('')
    if choice in response_A:
        print("Good Job!!!now you are equipped with a weapon at least.")
        print('')
        alarm()
    elif choice in response_B:
        print("wow!!you have got the best weapon but unfortunately the gun has no bullets")
        print('')
        alarm()


def alarm():
    print("However,the man raises an alarm when he sees the ropes cut and the window is open and that the prisoner "
          "has\n "
          "escaped.You choose to:")
    print('\tA:Jump through the window\n'
          '\tB:Wait for your death.\n'
          '\tC:Come out of your hiding place, behind the door and run to the find the exit gate.')
    time.sleep(2)
    choice = input('>>>')
    print('')
    if choice in response_A:
        run()
    elif choice in response_B:
        print("You were caught")
        gameover()

    elif choice in response_C:
        print('Easy catch the men saw you and caught you.')
        gameover()
        retry()
    else:
        print(required)
        intro()


def run():
    print('Outside the window is a bush you head into the bush and the men follow you.\n'
          'You see them and begin to run they start shooting at you.\n'
          '\tA:You run\n'
          '\tB:Run and hide behind a tree\n'
          '\tC:Wait for the men so that you can fight them\n')
    time.sleep(2)
    choice = input('>>>')
    print('')
    if choice in response_A:
        continue_run()
    elif choice in response_B:
        print('You were caught,bad luck')
        gameover()
        retry()
    elif choice in response_C:
        print('OOh my!! that is soo daring but they caught you')
        gameover()
        retry()


def continue_run():
    print("You continue running, the men are after you but you have no idea why they want You.You reach a two\n "
          "branched.choose path\n")
    print('\tA:Left\n'
          '\tB:Right\n'
          '\tC:Sit and wait for the men\n')
    time.sleep(2)
    choice = input('>>>')
    print('')
    if choice in response_A:
        death()
        retry()
    elif choice in response_B:
        print("You Escaped!!You win")
    elif choice in response_C:
        print("It was not worthed to run away and give up here.")
        gameover()
        retry()


def death():
    print('You begin running but unfortunately you are trapped in an ogre trap.You are their supper today!!')
    retry()


intro()
