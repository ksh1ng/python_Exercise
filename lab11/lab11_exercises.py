#demo example
def load_fruit_prices(prices_dict,price_data):
    '''This function takes an empty dictionary from main and populates it with data
       from a text file.  The file has two columns, a food and a price.
       Create an item using the food as the key and the price as a value.
       If the entry already exists, keep the lower price.
            prices_dict - (dict) an empty dictionary to store the food prices
            price_data - (str) a filename of a csv file with food and prices

        returns nothing
    '''
    f = open(price_data, 'r')

    for line in f:
        line = line.strip().split(',')
        fruit = line[0]
        price = line[1]

        prices_dict[fruit] = float(price)
    f.close()




def save_earth(fname, animal_dict):
    '''
    This function will read from a file and populate the empty dictionary passed in as a
    parameter.

    The file contains information of animals found on Earth. The file contains two names on
    each line. The first name is either an animal type or deadly bacteria/virus. The second name
    is a name for the animal type, bacteria, or virus. Animal types include Bird, Fish, Mammal,
    and Reptile.

    Your task is to save all the creatures (animal types) listed in the file from the evil
    bacteria and viruses that randomly roam the file. You are to map only animal types to their
    corresponding names. If you come across a bacteria or a virus do not place it in the animal_dict.

    Example:
        animal_dict{
            "Bird" : ["Humming Bird", "Crow", "Dove" ...]
            ...
        }

    Parameters: fname - name of the file to be read
                animal_dict - empty dictionary that will eventually map animal types to a list of animal names.

    Returns: None
    '''
    f = open(fname, 'r')

    for line in f:
        line = line.strip().split(',')
        type = line[0]
        name = [line[1]]  #value of every element in dict is list

        #skip the Bacteria and Virus
        if type == 'Bacteria' or type == 'Virus':
            continue

        if type not in animal_dict:
            animal_dict[type] = []

        animal_dict[type] += name
    f.close()


def find_largest_animal_name(animal_dict):
    '''
    This function will print out the largest animal name for each animal type. The animal type is the key
    value in animal_dict. You are guaranteed that no animal name will be of equal length.

    Example:
        animal_dict {
                        "Bird" : ["Humming Bird", "Crow", "Dove"]
                        "Fish" : ["Tuna", "Marlin"]
                     }

        The function will print:  Bird -> Humming Bird
                                  Fish -> Marlin

    Parameter: animal_dict - dictionary

    Returns: None
    '''
    for species in animal_dict:
        max_name_len = 0

        for name in animal_dict[species]:
            if len(name) > max_name_len:
                max_name_len = len(name)
                max_name = name

        print(species + ' -> ' + max_name)


def parse_kisses(fname):
    '''
    Return a dictionary mapping people to who they've kissed.

    fname (str) -- The name of the file to read

    The given filename refers to a file that has 2 names per line. The people
    on that line have kissed. This function will map each person to a list of
    people that they've kissed. Some people have kissed more than once, so
    they appear on the same line together in the file more than once. The
    lists in the dictionary will have unique elements (no one can show up in
    a list twice)

    Example return value:
    {
        "Alex" : ["Olivia", "Mason"]
        "Olivia" : ["Alex"]
        "Mason" : ["Alex"]
    }
    '''
    parse_dict = {}
    f = open(fname, 'r')

    for line in f:
        line = line.split()
        name1 = line[0]
        name2 = line[1]

        if name1 not in parse_dict:
            parse_dict[name1] = []
        if name2 not in parse_dict[name1]:
            parse_dict[name1] += [name2]

        if name2 not in parse_dict:
            parse_dict[name2] = []
        if name1 not in parse_dict[name2]:
            parse_dict[name2] += [name1]

    f.close()
    return parse_dict




def print_number_of_people_kissed(kiss_dict):
    '''
    Print out each name along with how many people they have kissed.

    kiss_dictionary (dict) -- person (str) to list of people (list of str)

    Example format:
    Alex 2
    Olivia 1
    Mason 1
    '''
    for key in kiss_dict:
        print(key, len(kiss_dict[key]))



def most_kisses(kiss_dict):
    '''
    Return the name of the person who has kissed the most people.

    kiss_dictionary (dict) -- person (str) to list of people (list of str)

    Assume that there is no tie.
    '''
    max_num = 0
    for key in kiss_dict:
        if len(kiss_dict[key]) > max_num:
            max_num = len(kiss_dict[key])
            max_name = key

    return max_name



def main():
    #Test
    '''
    adict = {}
    load_fruit_prices(adict, 'fruits.csv')
    print(adict)
    '''


    #test
    '''
    empty_dict = {}
    save_earth('creatures.csv', empty_dict)
    print(empty_dict)
    print('----------------------------------')
    print(empty_dict['Reptile'])  # key does not exist
    print(empty_dict['Bacteria']) # key does not exist
    '''

    #test
    '''
    empty_dict = {}
    save_earth('creatures.csv', empty_dict)
    print(empty_dict)
    find_largest_animal_name(empty_dict)

    print()

    animal_dict = {"Bird" : ["Humming Bird", "Crow", "Dove"], "Fish" : ["Tuna", "Marlin"]}
    find_largest_animal_name(animal_dict)
    '''

    #test
    '''
    print(parse_kisses('kisses.txt'))
    '''

    #test
    '''
    kiss_dict = parse_kisses('kisses.txt')
    print_number_of_people_kissed(kiss_dict)
    '''

    #test
    '''
    kiss_dict = parse_kisses('kisses.txt')
    print(most_kisses(kiss_dict))
    '''



if __name__ == '__main__':

    main()
