'''
Author: <ksh1ng>
Date: <2018.7.18>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<WS0419>
'''

# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment
class Animal:
    '''create a animal object containing the following attribues.'''

    def __init__(self, name, species, food, amount, notes = None):
        '''
        Amount is a float, the others are strings. food is the type of food the Animal eats,
        amount is the amount in kilograms of one meal.
        '''
        self.name = name
        self.species = species
        self.food = food
        self.amount = amount
        self.notes = notes

    def __repr__(self):
        content = self.name + '\n-----------------------------'
        content += '\nSpecies: ' + self.species + '\nFood type: ' + self.food + '\nAmount per meal: ' + str(self.amount) + ' kg\n'

        if self.notes is not None:   #not None == True is True, and any nonempty string represents True!!
                content += 'Special comment: ' + self.notes + '\n'

        return content

    def add_appt(self, doctor, date, time, remarks):
        '''
         doctor: (str) the name of a doctor.
         date: (str) a date string.
         time: (str) a time string.
         remarks: (str) a string with the reason for the appointment.

        It creates a string  and assigns it to the notes instance variable.
        '''
        content = self.name + ' has an appt with Dr. ' + doctor + ' on ' + date + ' at ' + time + '.'
        content += '\nReason for appt: ' + remarks + '\n'

        self.notes = content

    def clear_notes(self):
        '''sets the notes instance variable to None'''
        self.notes = None


class Food:
    '''create a food object containing the following attributes.'''
    def __init__(self, name, price, qoh):
        '''qoh (short for quantity on hand). price and qoh are floats, name is a string.'''
        self.name = name
        self.price = price
        self.qoh = qoh

    def __repr__(self):
        return '<' + self.name + ', ' + str(self.price) + ', ' + str(self.qoh) + '>'

    def monthly_cost(self, Animal):
        '''
        returns a float containing the cost of feeding the Animal for 30 days
        (animals eat twice a day).
        '''
        return self.price * Animal.amount * 30 * 2  #animals eat twice a day.





#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''

    # put main code here, make sure each line is indented one level, and delete this comment
     #test1
    '''
    rocket = Animal('Rocket', 'dog', 'dogfood', .25)
    print(rocket)
    rocket.notes = 'best dog ever!!!'.title()
    print(rocket)
    '''

     #test2
    '''
    rocket.add_appt('Drew', '4/23/15', '11:00 am', 'Rabies shot')
    print(rocket.notes)
    '''

    #input('Press enter to end.')  # keeps the turtle graphics window open
     #test3
    '''
    rocket = Animal('Rocket', 'dog', 'dogfood', .25)
    kirkland = Food('Costco_generic', 2.00, 15)
    print(kirkland)
    print(kirkland.monthly_cost(rocket))
    '''
if __name__ == '__main__':
    main()
