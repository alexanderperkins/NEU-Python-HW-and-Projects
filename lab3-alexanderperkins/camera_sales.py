"""
    CS 5001
    Lab 3
    Exercise 1
    Name: Alex Perkins
"""

'''
In this example we are going to calculate the salary of a camera salesperson. 
Their basic salary is 1500, for every camera they will sell they will get 200 and 
the commission on the month’s sale is 2%. The input will be number of cameras sold 
and total price of the cameras.

For full credit, your solution must have all of the following functions:

    A function welcome that takes no parameters and returns no values. 
    The function will print a friendly welcome message to the user.
    A function get_cameras_sold that takes no parameters, prompts the user for
     the number of cameras sold, and returns the user's input as an integer.
    A function get_camera_price that takes no parameters, prompts the user for
     the price of each camera, and returns the user's input as a float.
    A function calculate_total_pay that takes two parameters: the number of
     cameras sold and the price per camera. The function will calculate the
      total pay as described above and return that value.
    A function display_total that will take as input the total and print it for
     the user in a nicely formatted message.
    A main function that will call the functions above appropriately. 
'''
def welcome():
    print("Hi, welcome to the shop!")

def get_cameras_sold():
    cameras_sold = int(input("How many cameras were sold? "))
    return cameras_sold

def get_camera_price():
    camera_price = float(input("What's the camera price? $"))
    return camera_price

def calculate_total_pay(cameras_sold, camera_price):
    salary = 1500 + (200 * cameras_sold) + (0.02 * cameras_sold * camera_price)
    return salary

def display_total(total_pay):
    print(f'The total pay towards the seller is ${total_pay}.')

def main():
    welcome()
    cameras_sold = get_cameras_sold()
    camera_price = get_camera_price()
    total_pay = calculate_total_pay(cameras_sold, camera_price)
    display_total(total_pay)


if __name__ == '__main__':
    main()
