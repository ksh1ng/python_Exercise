'''
Author: <ksh1ng>
Date: <2018.7.17>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<hw09-2>
'''

# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment
def load_twitter_dicts_from_file(filename, emoticons_to_ids, ids_to_emoticons):
    '''
    Description:
     The function should read the given file and load the two dictionaries with keyvalue
     pairs.
    Parameters:
     filename: (str) the name of a twitter data file to read.
     emoticons_to_ids: (dict) an empty dictionary.
     ids_to_emoticons: (dict) an empty dictionary.
    Return:None
    '''
    f = open(filename, 'r')

    for data in f:
        data = data.strip().split()
        emoticon = data[0].strip('"')
        id = data[2].strip('"')

        if emoticon not in emoticons_to_ids:
            emoticons_to_ids[emoticon] = []
        emoticons_to_ids[emoticon].append(id)

        if id not in ids_to_emoticons:
            ids_to_emoticons[id] = []
        ids_to_emoticons[id].append(emoticon)
    f.close()

def find_most_common(adict):
    '''
    Description:
      Find the key that has the longest list as a value and print
      out that key and the length of its list. Print in the following format:
                            :) occurs 871 times
    Parameters:
     adict: (dict) Assume the keys of the dictionary will be strings (e.g. emoticons) and each
                   value will be a list of strings (e.g. user ID's).
    Return: (str) the key that had the longest list.
    '''
    max_len = 0

    for key in adict:
        if len(adict[key]) > max_len:
            max_len = len(adict[key])
            max_key = key
    print(max_key.ljust(21) + 'occurs' + str(max_len).rjust(9) + ' times')

    return max_key







#==========================================================
def main():
    '''
    i.) Create two empty dictionaries .(emoticons_to_ids and
        ids_to_emoticons)
    ii.) Call your load_twitter_dicts_from_file function passing it the file
         name and the two dictionaries.
    iii.) Print the number of different emoticons found in the data file.
    iv.) Print the number of different user ID's found in the data file.
    v.) Next call your find_most_common, passing it the emoticons_to_ids
        dictionary. The result should look like this.
    '''

    # put main code here, make sure each line is indented one level, and delete this comment

    #test

    emoticons_to_ids = {}
    ids_to_emoticons = {}
    load_twitter_dicts_from_file('twitter_emoticons.dat', emoticons_to_ids, ids_to_emoticons)
    print('Emoticons: ' + str(len(emoticons_to_ids)))
    print('UserIDs:   ' + str(len(ids_to_emoticons)))

    print()


    #find_most_common(emoticons_to_ids)
    #find_most_common(ids_to_emoticons)


    #List the top five emoticons
    for i in range(5):
        emoticons_to_ids.pop(find_most_common(emoticons_to_ids)) #first->print ; second->pop





if __name__ == '__main__':
    main()
