# question 6

r=int(input("enter the rows: "))
def show_stars(r):
    for i in range(0,r):
        for j in range(0,i+1):
            print("*",end="")
        print()
show_stars(r)
