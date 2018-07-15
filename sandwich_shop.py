def ingredients(filename, ingredient_dict):
    '''
    This function reads a file and populates an empty dictionary.

    The file contains two names on each line separated by a comma.
    The first name represents a sandwich ingredient category which is
    either a meat, cheese, bread, vegetable, or sauce. The second name
    is a delicious ingredient that corresponds to the first name.
    Example:
    bread,Sourdough

    You are to populate the dictionary by mapping the sandwich ingredient
    categories (meat, cheese, bread, vegetable, or sauce) to a list of there
    corresponding ingredient options.

    Example:
    {'meat': ['Ham', 'Turkey', 'Chicken']}

    Parameter(s):
    filename (str): represents a file name.
    ingredient_dict (dictionary): An empty dictionary that will eventually
    be populated.

    Returns: None
    '''
    f = open(filename, 'r')

    for ingredient in f:
        ingredient = ingredient.strip().split(',')
        type = ingredient[0]
        name = ingredient[1]

        if type not in ingredient_dict:
            ingredient_dict[type] = []

        ingredient_dict[type].append(name)
    f.close()



def display_ingredients(lst):
    '''
    This function will print out the contents of a list. You will
    first sort the list and then print each item one per line with
    a number separated by a colon.

    Iterate through the list by element. Right justify the number and
    colon 5 units then concatenate the current item from the list.

    Example:

    1: Bagel
    2: Dark Rye
    ...

    Parameter(s):
    lst (list) -- List containing strings.

    Returns: None
    '''
    lst.sort()

    i = 0
    for item in lst:
        i += 1
        print('  ' + str(i) + ': ' + item )


def make_sandwich(ingredient_dict):
    '''
    This function simulates a sandwich shop. You will use the dictionary
    that is passed in as a parameter to obtain the ingredients that will
    be used to build a sandwich. Keep track of the ingredients the user
    will be picking. (Hint: use a list).
    The function will first ask the user to either select an ingredient or
    if they would like to checkout.
    If the user selects check out call your display_ingredients function
    in order to display all the ingredients the user selected.

    If the user chooses to select an ingredient prompt them to pick from 5
    categories meat, cheese, bread, vegetable or sauce.
    Based on the user's selection use the dictionary to obtain the ingredients
    available for their selection.
    Call your display_ingredients selection to show the user their options.
    Check to see if the user's choice is a valid option. If it is print
    a message that indicates a successful add otherwise print 'Not a valid
    option.' Continue this process until the user decides to check out.
    If the user selects an option other than select an ingredient or to
    check out print 'Not a valid option try again' and allow them to pick
    a valid choice.

    Hint: It may be useful to use .title() in your function.

    Parameter(s):
    ingredient_dict (dictionary) -- Dictionary that maps a food group (key)
    to a list of possible ingredients for that food group.

    Returns: None
    '''
    userPick = []
    print('************ Sandwich Time *************')

    while True:


        print('\nPlease Select a Number\n  1. Select Ingredient\n  2. Check out')
        user = input('\nNumber: ')

        if user == '2':
            break

        elif user == '1':
            totalType = ['meat', 'cheese', 'bread', 'vegetable', 'sauce']
            totalType.sort()

            print('\nSelect Ingredient Group Number: ')
            display_ingredients(totalType)
            type = input('\nNumber: ')

            while type not in '12345':
                print('Not a valid option.')
                print('\nSelect Ingredient Group Number: ')
                display_ingredients(totalType)
                type = input('\nNumber: ')

            print()
            display_ingredients( ingredient_dict[totalType[int(type)-1]] )
            user_choice = input('\nPlease choose which one you want: ').title()


            while user_choice not in ingredient_dict[totalType[int(type)-1]]:
                print('Not a valid option.')
                user_choice = input('\nPlease choose which one you want: ').title()

            print('\nIngredient "' + user_choice + '" added successfully!')

            userPick.append(user_choice)


        else:
            print('\nNot a valid option try again.')



    print('Your Sandwich Includes: ')
    display_ingredients(userPick)

    print('\nEnjoy!')










def main():
    '''
    Make use of your functions in main.
    '''
    #test ingredients function:
    '''
    adict = {}
    ingredients('choices.csv', adict)
    print(adict)
    '''

    #test display_ingredients function:
    '''
    lst = ['nick', 'benson', 'johnny']
    display_ingredients(lst)
    '''

    #test make_sandwich function:
    adict = {}
    ingredients('choices.csv', adict)

    make_sandwich(adict)


if __name__ == '__main__':
    main()
