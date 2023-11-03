
def print_nums_iterative(n: int):
    counter = 0
    while counter < n:
        print(counter)
        counter += 1

def print_nums_iterative2(n: int):
    for counter in range(n):
        print(counter)
        counter += 1

def print_nums_recursive(n: int):
    if n == 0:
        return
    print(n)
    return print_nums_recursive(n-1)

def print_nums_recursive2(n: int, a):
    if a == n:
        print(n)
        return
    print(a)
    a += 1
    print_nums_recursive2(n, a)

def main():
    number = int(input('Enter a int: '))
    # print_nums_iterative(number)
    # print_nums_iterative2(number)
    # print_nums_recursive(number)
    a = 0
    print_nums_recursive2(number, a)


if __name__ == '__main__':
    main()
