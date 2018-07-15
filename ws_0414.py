'''
Author: <ksh1ng>
Date: <2018.7.15>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<WS0414>
'''

# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment
class SocialPerson:
    '''SocialPerson will represent a person and his/her social connections'''
    def __init__(self, name, friends):
        '''
        name: (str) represents the person's name.
        friends: (dict) that has the names of friends as keys and the time the person
                       has known them as values
        '''
        self.my_name = name
        self.friends = friends

    def __repr__(self):
        content = 'Friends of ' + self.my_name + '\n' + '*' * 20
        for friend in self.friends:
            content += '\n' + friend
        return content

    def new_year(self):
        '''increments the value associated with each key in self.friends.'''
        for friend in self.friends:
            self.friends[friend] += 1

    def add_friend(self, friend, time):
        '''adds the name of friend to self.friends as a key, with associated value time.'''
        self.friends[friend] = time

    def unfriend(self, sp):
        '''
        This method pops the name of sp from self.friends.
            sp: (class) another instance of SocialPerson
        '''
        if sp.my_name in self.friends:
            self.friends.pop(sp.my_name)



#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''

    # put main code here, make sure each line is indented one level, and delete this comment

    #test
    nick = SocialPerson('nick',{'benson': 2, 'ks': 3})
    print(nick)

    nick.new_year()
    print(nick.friends)

    nick.add_friend('ben' , 7)
    print(nick.friends)

    ks = SocialPerson('ks', {'sk': 1, 'jason': 2})
    nick.unfriend(ks)
    print(nick.friends)



    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
