'''
Author: <ksh1ng>
Date: <2018.7.8>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<hw8>
'''

# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment
def find_insert_position(name, names_list):
    '''
    Description:
     The function does not insert the name, it does not change the names list
     in any way. It simply finds and returns the appropriate integer index.

    Parameter:
     name: (str) a terrestrial mammal’s name.
     names_list: (list) a list of strings in alphabetical order.

    Return: (int)  indicating the position (index) in the list of names.
                [ such that if you inserted the given mammal’s name into
                  the list at that index the list would still be in alphabetical
                  order.]
    '''
    names = names_list.copy()

    names.append(name)
    names.sort()

    return names.index(name)

#test
'''
names = ['Big brown bat', 'Brazilian tapir', 'Chimpanzee']
print(find_insert_position('Cat', names))
'''

def populate_lists(names, body_weights, brain_weights):
    '''
    Description:
     Open the “BrainBodyWeightKilos.csv”  file and then populate each list
     accordingly. The mammal names "MUST" be in title case.
    Parameter:
     names: (list)  to hold the mammal names.
     body_weights: (list) to hold the mammal body weights (these should be floats)
     brain_weights: (list)  hold the mammal brain weights (these should be floats)
    Return: None.
    '''
    f = open('BrainBodyWeightKilos.csv', 'r')

    for line in f:
        data = line.strip().split(',')
        names.append(data[0].title())
        body_weights.append(float(data[1]))
        brain_weights.append(float(data[2]))
    f.close()

def write_converted_csv(fname_write, names, body_weights, brain_weights):
    '''
    Description:
     i)writes a new .csv file (with the given filename) in the same format
     as the original “BrainBodyWeightKilos.csv” using the values in the three lists,
     but all kilogram values and all gram values should first be converted to pounds
     , and names should be in title case. Your conversion factor for converting from
     kilograms should be 2.205; from grams it should be 0.0022.
     ii)The floats written to the file should be rounded to 2 decimal places.

    Parameter:
     fname_write: (str) the name of a file to write.
     names: (list)  a list of strings (the names of mammals).
     body_weights: (list) a list of floats (weights of mammals in kilograms).
     brain_weights: (list) a list of floats (brain weights of mammals in grams.)
    Return: None.
    '''
    output_f = open(fname_write, 'w')

    for i in range(len(names)):
        names[i] = names[i].title()
        body_weights[i] = round(body_weights[i] * 2.205, 2)
        brain_weights[i] = round(brain_weights[i] * 0.0022, 2)
        output_f.write(names[i] + ',' + str(body_weights[i]) + ',' + str(brain_weights[i]) + '\n')


    output_f.close()

#test
'''
names = []
body_weights = []
brain_weights = []
populate_lists(names, body_weights, brain_weights)

write_converted_csv('new.csv', names, body_weights, brain_weights)

'''
#==========================================================
def main():
    '''
    i.) Create three empty lists to hold mammal names, body weights, and brain
    weights.
    ii.) Populate the three empty lists you just created.
    iii.) Next you will repeatedly ask the user to (note that the prompt is
            preceded by a blank line)

    @@If the name entered by the user is not in your list of names (case
      insensitive search):
        1.i.  Print a message indicating the animal was not found.
        1.ii. Ask the user if he would like to add it. (You can assume the user will
              answer either ‘y’ or ‘n’.)

    @@• If the name entered by the user is already in your list of names:
          i. Print the animal’s data
          ii. Ask the user if he would like to delete the animal.
             (You can assume the user will answer either ‘y’ or ‘n’.)

    @@• If the user entered ‘q’ you should:
          – use the function you wrote for part 2 above to write the data out to
            a new file called “BrainBodyWeightPounds.csv” and program
            will end.

    '''

    # put main code here, make sure each line is indented one level, and delete this comment
    names = []
    body_weights = []
    brain_weights = []
    populate_lists(names, body_weights, brain_weights)

    while True:
        print()
        name_enter = (input('Enter animal name (or "q" to quit): ')).title()

        if name_enter in 'Qq':
            break

        elif name_enter not in names:
            while True:
                print('File does not contain "' + name_enter + '".')
                is_continue = input('Add "' + name_enter + '" to file? (y|n) ')

                if is_continue in 'Nn':
                    break
                elif is_continue in 'Yy':
                    body_weight = float(input('Enter body weight for "' + name_enter + '" in kilograms: '))
                    brain_weight = float(input('Enter brain weight for "'+ name_enter + '" in grams: '))

                    insert_position = find_insert_position(name_enter, names)
                    names.insert(insert_position, name_enter)
                    body_weights.insert(insert_position, body_weight)
                    brain_weights.insert(insert_position, brain_weight)
                    break
                else:
                    print('Try again!\n')


        elif name_enter in names:
            while True:
                index = names.index(name_enter)
                print(names[index] + ': ' + 'body = ' + str(body_weights[index]) + ', '
                      + 'brain = ' + str(brain_weights[index]) + '')

                to_delete = input('Delete "' + name_enter + '"? (y|n) ')

                if to_delete in 'Nn':
                    break
                elif to_delete in 'Yy':
                    names.remove(names[index])
                    body_weights.remove(body_weights[index])
                    brain_weights.remove(brain_weights[index])
                    break
                else:
                    print('Try again!\n')

        elif name_enter in 'Qq':
            break

    write_converted_csv('BrainBodyWeightPounds.csv', names, body_weights, brain_weights)












    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
