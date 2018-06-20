'''
Author: <ksh1ng>
Date: <2018.6.20>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<Lab07, just some exercises for midtern~>
'''

# put all of your import statements below this line and then delete this comment

#Implementation 1:
'''
Given some integer, return True if that integer is a multiple of 3. Otherwise return False. A
number is a multiple of 3 if there is no remainder when you divide that number by 3.
'''

def is_multiple_of_three(n):
    '''
    Return True if the given number is a multiple of 3. False
    otherwise.
    '''
    if n % 3 == 0:
        return True

    return False



#Implementation 2:
'''
Your ISTA 116 professor has requested that you write a program to help students understand
the idea of frequency (how many times something shows up). You decide to do this by asking
the user for a bunch of words, then print out how many times "mean", "median" and "mode" are
typed.
'''
def occurrences_times():
    '''
    Example:
    Tell me the secret keywords:
    > mean
    > sample
    > deviation
    > stats
    > mean
    > mode
    > mean
    > done
    The user typed mean 3 times
    The user typed median 0 times
    The user typed mode 1 time
    '''
    user_typed = input('Tell me the secret keywords:\n> ')
    count_mean = 0
    count_median = 0
    count_mode = 0

    while user_typed != 'done':

        if user_typed == 'mean':
            count_mean += 1
        elif user_typed == 'median':
            count_median += 1
        elif user_typed == 'mode':
            count_mode += 1

        user_typed = input('> ')

    print('The user typed mean ' + str(count_mean) + ' times')
    print('The user typed median ' + str(count_median) + ' times')
    print('The user typed mode ' + str(count_mode) + ' times')








# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''

    # put main code here, make sure each line is indented one level, and delete this comment

    #test1
    '''
    print(is_multiple_of_three(0))
    print(is_multiple_of_three(1))
    print(is_multiple_of_three(-9))
    print(is_multiple_of_three(12))
    print(is_multiple_of_three(7))
    '''

    #test2
    occurrences_times()



    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
