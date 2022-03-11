#!/usr/bin/env python


def main():
    list = [i for i in range(1, 100)]
    item = int(input('Number to find: '))
    low = 0
    high = len(list) - 1
    while (low<=high):
        mid = (low + high)//2
        if list[mid] == item:
            print('Guess is correct!', mid + 1)
            return mid
        if list[mid] > item:
            print('High!')
            high = mid - 1
        else:
            print('Low')
            low = mid + 1
    return None

    


if __name__ == '__main__':
    main()