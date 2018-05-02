'''Every exercise in worksheet'''
def bluebird_count():
    sum=0
    num_teams=int(input("Enter the number of teams:"))
    for i  in range(num_teams):
        num_observers=int(input("Enter the number of observers of team{}:".format(i+1)))
        for j in range(num_observers):
            print("----Observer {} -----".format(j+1))
            num_bird=int(input("Enter number spotted by this observer:"))
            sum=sum+num_bird
    #print("There were {} Eastern Bluebirds spotted today".format(sum))
    return sum



def  number_of_odds():
    number=int(input("Enter a nonnegative integer:"))
    num_odds=0
    for n in range(number+1):
        if n%2!=0:
            num_odds=num_odds+1
    print("The number of odds between 0 and",number,"is",num_odds)

def main():
    number_of_odds()

    print("There were {} Eastern Bluebirds spotted today".format(bluebird_count()))


if __name__ == '__main__':
    main()
