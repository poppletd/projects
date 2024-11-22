'''
Name: Delaina Poppleton
Date: 11/22/24
Assignment: LoopFun
Description: Repitition structures programming project
'''

def main():

    # Part 1 - get user input
    while True:
        height = int(input("Enter a box height(between 3 and 10): "))
        if 3 <= height <= 10:
            break
        else:
            print("that number is out of bounds, try again.")
    while True:
        min_num = height + 1
        width = int(input(f"Enter a width(between {min_num} and 20): "))
        if height <= width <= 20:
            break
        else:
            print("that number is out of bounds, try again.")
    # Part 2a - print numbers
    print(f"The integers from {height} to {width} are:")
    for i in range(height, width+1):
        print(i,end=" ")
    # Part 2b - calculate and print average of the numbers
    average = (height + width)/2
    print()
    print(f"and the average of those numbers is {average}")
    print()
    # Part 3 - print the hollow box
    print("*"*width)
    for i in range(height-2):
        for i in range(2):
            print("*",end=" "*(width-2))
        print()  
    print("*"*width)
    print()      
    # Part 4 - print the triangular shape
    asterisks = ("**")
    for i in range(height):
        print(asterisks)
        asterisks = (asterisks + ("**"))

if __name__ == '__main__':
    main() # don't change this
