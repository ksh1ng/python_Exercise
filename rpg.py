'''
Author: <ksh1ng>
Date: <2018.7.22>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<hw10>
'''

# put all of your import statements below this line and then delete this comment
import random
# put all of your function definitions below this line and then delete this comment
class Fighter:
    '''
    Each created individual Fighter will have an integer value called
    “hit points” that represents his/her current health (the amount of
    damage he/she can sustain before death).
    '''
    def __init__(self, name):
        '''name: (str) the name of a fighter.'''
        self.name = name
        self.hit_points = 10           #Hit Points is HP represents his/her current health.
                                      #(the amount of damage he/she can sustain before death).

    def __repr__(self):
        '''show the name and hit points of the instance'''
        return self.name + ' (HP: ' + str(self.hit_points) + ')'

    def take_damage(self, damage_amount):
        '''
        damage_amount: (int) represent the number of hit points of damage that have just been inflicted
                             on this Fighter.
        return: None.
        '''
        self.hit_points -= damage_amount

        if self.hit_points <= 0:
            print('\tAlas, ' + self.name + ' has fallen!')
        else:
            print('\t' + self.name + ' has ' + str(self.hit_points) + ' hit points remaining.')

    def attack(self, other):
        '''other: (class) another Fighter instance being attacked by self'''

        print(self.name + ' attacks ' + other.name + '!')

        randnum = random.randrange(1, 21)    #A number that is 12 or higher indicates a hit*

        if randnum >= 12:
            DamageAmount = random.randrange(1, 7)
            print('\tHits for ' + str(DamageAmount) + ' hit points!')
            other.take_damage(DamageAmount)
        else:
            print('\tMisses!')

    def is_alive(self):
        '''returns True if self has a positive number of points, False otherwise'''
        return self.hit_points > 0



def combat_round(fighter1, fighter2):
    '''
    Description:
     Determines which of the two fighters attacks first for the round

    Parameters:
     fighter1, fighter2: (class) instances of Fighter.
    Return: None.
    '''
    randnum1 = random.randrange(1, 7)     #fighter1 with the roll
    randnum2 = random.randrange(1, 7)     #fighter2 with the roll

    if randnum1 == randnum2:     #Have each fighter instance call his attack method on the other fighter
        print('Simultaneous!')   #(the first fighter in the argument list must attack first to make
        fighter1.attack(fighter2)#...the test work correctly)
        fighter2.attack(fighter1)

    elif randnum1 > randnum2:
        fighter1.attack(fighter2)

        if fighter2.is_alive():
            fighter2.attack(fighter1)

    else:
        fighter2.attack(fighter1)

        if fighter1.is_alive():
            fighter1.attack(fighter2)




#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''

    # put main code here, make sure each line is indented one level, and delete this comment
    f1 = Fighter('Death_Mongrel')
    f2 = Fighter('Hurt_then_Pain')

    round = 1

    while f1.is_alive() and f2.is_alive():
        print('\n' + (' ROUND ' + str(round) + ' ').center(47, '='))
        print(f1)
        print(f2)

        input('Enter to Fight!')
        combat_round(f1, f2)
        round += 1

    print('\nThe battle is over!')
    print(f1)
    print(f2)

    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
