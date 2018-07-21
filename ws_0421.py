'''
Author: <ksh1ng>
Date: <2018.7.21>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<WS0421>
'''
# put all of your import statements below this line and then delete this comment
from ws_0419 import *

# put all of your function definitions below this line and then delete this comment
class Zoo:
    '''create a zoo object containing the following attributes.'''

    def __init__(self, animalf, foodf):
        '''
        Instance variables:
         self.animals: (dict)  holds all of the animals in the zoo and maps their names to their
                               Animal objects.
         self.foods: (dict) maps food names to Food objects.
        Arguments:
         animalf: (str) animal file name. --format: <name>,<species>,<food>,<amount>
         foodf: (str) the food file name. --format: <name>,<price>,<qoh>
        '''
        self.animals = {}
        self.foods = {}
        AnimalF = open(animalf, 'r')
        FoodF = open(foodf, 'r')

        for animal in AnimalF:
            a_data = animal.strip().split(',')
            a_name = a_data[0]
            a_species = a_data[1]
            a_food = a_data[2]
            a_amount = float(a_data[3])

            while a_name in self.animals:
                a_name += '-2'
            self.animals[a_name] = Animal(a_name, a_species, a_food, a_amount)

        for food in FoodF:
            f_data = food.strip().split(',')
            f_name = f_data[0]
            f_price = float(f_data[1])
            f_qoh = float(f_data[2])

            while f_name in self.foods:
                f_name += '-2'

            self.foods[f_name] = Food(f_name, f_price, f_qoh)

    def reorder(self, food_object):
        '''
        It determines if the amount on hand of that type of food is enough to feed all of the
        animals that eat that kind of food in the zoo for at least 7 days.
        If not, it returns the amount necessary to feed all of the animals in
        the zoo that eat that food for 30 days. If so, it returns None.
        '''
        aDayNeedAmount = 0

        for animal in self.animals:
            animal = self.animals[animal]

            if animal.food == food_object.name:
                aDayNeedAmount +=  animal.amount * 2

        if food_object.qoh < aDayNeedAmount * 7:
            return aDayNeedAmount * 30

        return None

    def get_order(self):
        '''
        builds and returns a dictionary of orders for each type of food.
        It maps the name of each food to the amount that needs to be ordered as determined by reorder.
        '''
        orders = {}

        for food_name in self.foods:
            food = self.foods[food_name]  #food is ab object
            orders[food_name] = self.reorder(food)

        return orders


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''

    # put main code here, make sure each line is indented one level, and delete this comment



    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
