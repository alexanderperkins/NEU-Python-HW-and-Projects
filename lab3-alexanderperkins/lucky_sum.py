"""
    CS 5001
    Lab 3
    Exercise 2
    Name: Alex Perkins
"""

'''
Write a Python program that implements a function lucky_sum(a: int, b:int , c:int) -> int
 that takes as input three integers and returns their sum. However, if one of the values
  is 13 then it does not count towards the sum and values to its right do not count. So for
   example, if b is 13, then both b and c do not count.

Implement a main method that tests this function by calling it at least five times with
 different test cases. For full credit, make sure your test cases test different possible
  conditions. 
'''
def lucky_sum(a: int, b: int, c: int) -> int:
    """
    while (type(a) != int or type(b) != int or type(c) != int):
        print("***Error*** \n Variables must be integers only!")
        a = input("Enter 1st integer: ")
        b = input("Enter 2nd integer: ")
        c = input("Enter 3rd integer: ")
        try:
            a = int(a)
            b = int(b)
            c = int(c)
        except:
            pass
        if (type(a) == int and type(b) == int and type(c) == int):
            break
    """
    if (a == 13):
        total = 0
    elif (b == 13):
        total = a
    elif (c == 13):
        total = a + b
    else:
        total = a + b + c
    return total

def main():
    print(lucky_sum(2, 3, 5))
    print(lucky_sum(13, 3, 5))
    print(lucky_sum(2, 13, 5))
    print(lucky_sum(2, 3, 13))
    print(lucky_sum(5, 4, 13))


if __name__ == '__main__':
    main()
