'''
Author: <ksh1ng>
Date: <2018.7.17>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<hw09-1>
'''

# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment
def fish_dict_from_file(filename):
    '''
    Description:
     i.) In the function make a literal dictionary containing the mapping from the
         Numeric Species Code to the English fish name.
     ii.) Next create an empty dictionary and read each fish Species and Weight from
          the “fishcatch.dat” file into the dictionary, mapping the English name of each
          fish species onto a list containing the weights of all of the fish of that type that
          were caught.


    Parameters:
     filename: (str) giving the name of a file to read.

    Return: (dict) the dictionary that contains the fish names and weights
    '''
    f = open(filename, 'r')
    fishmap = {1: 'Bream', 2: 'Whitefish', 3: 'Roach', 4: '?', 5: 'Smelt', 6: 'Pike', 7: 'Perch'}

    fish = {}

    for line in f:
        line = line.strip().split()

        Numeric_code = int(line[1])
        species = fishmap[Numeric_code]
        weight = line[2]

        if species not in fish:
            fish[species] = []

        if weight == 'NA':  #Skip any fish that has a missing weight value (i.e. weight is “NA”).
            continue

        fish[species].append(float(weight))
    f.close()

    return fish

#==========================================================
def main():
    '''
     Call the function above to get a dictionary of fish names and weights
    '''

    # put main code here, make sure each line is indented one level, and delete this comment
    fish = fish_dict_from_file('fishcatch.dat')

    print('#'.rjust(4) + ' ' + 'NAME'.ljust(10) + 'MEAN WT'.rjust(11))

    for species in sorted(fish.keys()):
        number = len(fish[species])
        sum_weight = 0

        for weight in fish[species]:
            sum_weight += weight

        mean_wt = round(sum_weight / number, 1)
        print(str(number).rjust(4) + ' ' + species.ljust(10) + str(mean_wt).rjust(10) + 'g')






    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
