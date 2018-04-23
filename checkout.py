def checkout():
    total=0
    count=0
    moreItems=True

    price=float(input("Enter the price of item(0 when done!):"))
    print("Subtotal: $",price)
    if price==0:
        print("you can’t compute an average without data")

    else:
        while moreItems:
            total+=price

            price=float(input("Enter the price of item(0 when done!):"))
            if price!=0:

                if price < 0:

                    print("Error!please try again")
                    print("Subtotal: $",total)
                else:

                    count+=1
                    total+=price
                    #moreItems=True
                    print("Subtotal: $",total)
            elif price<0:
                print("Error!please try again")
            else:
                moreItems=False
        print("Total items:",count)
        print("Total price: $",total)
        print("Average price per item: $", total/count)



def main():
    checkout()

if __name__ == '__main__':
    main()
