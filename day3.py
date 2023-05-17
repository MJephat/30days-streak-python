# Fibonacci: Write a program that prompts the user to enter a positive integer n, 
# and then prints the first n Fibonacci numbers. The Fibonacci sequence starts 
# with 0 and 1, and each subsequent number is the sum of the two preceding numbers.


def Fibonacci():
    n = int(input("Enter a Positive Integer:"))

    firstnum = 0
    secondnum = 1

    if n<=0:
        print("The Output of your input is", firstnum)
    else:
        # print(firstnum,secondnum)
        for x in range(2,n):
            thirdnum=firstnum+secondnum
            print(thirdnum)
            firstnum=secondnum
            secondnum=thirdnum
Fibonacci()