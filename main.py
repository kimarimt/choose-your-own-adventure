from random import choice


def main():
    print('Welcome to Treasure Tracker')
    print('Traverse the tomb to collect the ancient treasure')
    
    hallway = input('''
You have just entered the tomb of King Ramses. The
door closes behind you. You turn to see two hallways on the left and
right. Which way do you choose:
''')
    correct_answer = choice(['left', 'right'])
    if hallway == correct_answer:
        door = input('''
After walking down the hallway. You come to two doors, one red
and one blue. Which door do you enter:
''')
        correct_answer = choice(['red', 'blue'])
        if door == correct_answer:
            print('''
You find yourself in a chamber. The door closes and a green mist 
fills the room. You reacted violently to the mist, turns out it was
poison. GAME OVER!
''')
        else:
            print('''
The door opens to reveal a collections of trinkets, gold,
and chalices. YOU WIN!
''')
    else:
        print('''
As you walk down the hallway, you activate and trip wire. The floor
opens beneath you and fall into a pit of spikes. GAME OVER!
''')

if __name__ == '__main__':
    main()
