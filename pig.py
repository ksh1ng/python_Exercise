'''
Author: <ksh1ng>
Date: <2018.5.25>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<hw05>
'''
import random
# put all of your import statements below this line and then delete this comment
def print_scores(name1 , score1 , name2 , score2):
    '''
    Four parameters :1.the name of the first player (a string)
                     2. his/her score (an int)
                     3.the second player's name (a string)
                     4.score (an int)
        a) Print the following message, using the current parameter values
           for the player names and scores (NOT necessarily Ziggy, 18, Elmer, and 23):
               --- SCORES Ziggy: 18 Elmer: 23 ---
              • Print an empty line before this line.
              • There is a single tab between SCORES and the name of player 1.
              • There is a single tab between player 1's score and player 2's name.
              • Every other gap is a single space.
    '''
    print()
    print("--- SCORES\t"+name1+":",str(score1)+"\t"+name2+":",str(score2),"---")

def check_for_winner(name , score):
    '''
    Two parameters: a name (a string) and a score (an int)

       a) If the score is 50 or more print the following message
          (using the current parameter value for the name, not Ziggy):
          THE WINNER IS: Ziggy!!!!!
       b) The function returns True if the score is 50 or more,
          otherwise it returns False.
    '''
    if score >= 50:
        print("THE WINNER IS:",name+"!!!!!")
        return True

    return False

def roll_again(name):
    '''
     A single string parameter to hold a player's name
     In the function:
        a) Enter a while loop which repeats the following steps:
           • Ask whether the player would like to roll again, using the
             following message:
              Roll again, Ziggy? (Y/N)
              @There is a single space after (Y/N).
           • If the player answers with Y, y, N, or n, exit from the loop.
           • Otherwise print the following message (replacing XXX with the user’s entry):
               I don't understand: "XXX". Please enter either "Y" or "N".
        b) The function returns either True or False depending on
           whether the player wants to roll again.
    '''
    while True:
        user_input = input("Roll again, " + name + "? (Y/N) ")
        if user_input in 'Yy':
            return True
        elif user_input in 'Nn':
            return False
        else:
            print("I don't understand: "+'"'+user_input+'".'+' Please enter either "Y" or "N".')


def play_turn(name):
    '''
    A single string parameter , which holds a player’s name. The function will:
        a) Print the player’s name as shown in the following example:
            ---------- Ziggy's turn ----------
            • There are 10 hyphens on either side of the message.
        b) Initialize a variable to keep track of the points the player
           earns on this turn
        c) The function then enters a while loop in which the player attempts
           to earn points. It repeats the following steps:
           • Generate a random integer between 1 and 6 inclusive using the random module.
           • Print a message displaying the roll as shown in the following example:
             <<< Ziggy rolls a 4 >>>
           @ Put a tab to the left of the first angle bracket.
           • If the roll is a 1:
           @Print the following message:
           !!! PIG! No points earned, sorry Ziggy !!!
            Put a tab to the left of the first exclamation point.
           @ Make sure the player earns no points for the turn.
           @ Make a change to ensure you exit the loop or exit directly.
           @ Use the following message to pause the program until the user is ready to
            continue:
                (enter to continue)
           • If the roll is not a 1:
            @ Print the following message:
            !!! PIG! No points earned, sorry Ziggy !!!
             Put a tab to the left of the first exclamation pointself.
            @ Make sure the player earns no points for the turn.
            @ Make a change to ensure you exit the loop or exit directly.
            @ Use the following message to pause the program until the user is ready to
              continue:
              (enter to continue)

           • If the roll is not a 1:
            @ Add the roll to the player’s points earned for the turn.
            @ Print the player’s turn total as in the following example:
                Points: 12
                 Put a tab to the left of the word Points.
            @ Use the roll_again function to ask the player if he/she would like to roll again.
            @ If not, make a change to ensure you exit the loop or exit directly
        d) Make sure that you returned the number of points earned by
           the player for this turn in all cases
    '''
    print("---------- "+name+"'s turn ----------")

    turn_earn = 0

    while True:
        roll_num = random.randint(1,6)
        print("\t<<< "+name+" rolls a "+str(roll_num)+" >>>")

        if roll_num == 1:
            print("\t!!! PIG! No points earned, sorry "+name+" !!!")
            input("(enter to continue)")
            return 0
        else:
            turn_earn += roll_num
            print("\tPoints: "+str(turn_earn))

            if  roll_again(name):
                continue
            else:
                return turn_earn


# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    a) Get an integer to use for the random seed from the user with the prompt:
        Enter seed value:
    b) Set random.seed to the value retrieved from the user.
    c) Print two blank lines followed by the title of the game:
        Pig Dice
    d) Ask the user to enter the first player’s name with this prompt:
        Enter name for player 1:
    e) Ask the user to enter the second player’s name with this prompt:
        Enter name for player 2:
    f) Print a greeting message in the following form:
        Hello Ziggy and Elmer, welcome to Pig Dice!
        • Put a tab to the left of Hello
    g) Initialize the players’ scores to 0.
    h) Print their scores using the print_scores function.
    i) Enter a while loop in which repeats the following steps:
        • Call the play_turn function for player 1 and add any earned points
        to his/her total score.
        • Print the players’ scores (use the appropriate function).
        • Check whether player 1 won the game (use the appropriate function).
        • If player 1 didn’t win, call the play_turn function for player 2
          and add any earned points to his/her total.
           Print the players’ scores.
           Check whether player 2 won the game.
        • If either player won the game, ensure that you exit the while loop.
    '''
    seed_value=int(input("Enter seed value: "))
    random.seed(seed_value)
    #print()
    print("\n\nPig Dice")
    player1=input("Enter name for player 1: ")
    player2=input("Enter name for player 2: ")
    print("\tHello "+player1+" and "+player2+", welcome to Pig Dice!")
    #input()
    score1 = 0
    score2 = 0
    print_scores(player1 , score1 , player2 , score2)
    while True:
        score1 += play_turn(player1)
        print_scores(player1 , score1 , player2 , score2)
        if check_for_winner(player1 , score1):
            break

        score2 += play_turn(player2)
        print_scores(player1 , score1 , player2 , score2)
        if check_for_winner(player2 , score2):
            break


    #print(roll_again('nick'))
    #print_scores("nick",100,"benson",80)
    # put main code here, make sure each line is indented one level, and delete this comment
    #print(play_turn('nick'))


    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
