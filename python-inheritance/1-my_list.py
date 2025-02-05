#!/usr/bin/python3
'''
This is the main module for MyList class
which inherits from the built-in list class.
'''


class MyList(list):
    '''
    A custom list class that inherits from the built-in list class.
    Adds a method to print the list in sorted order.
    '''

    def print_sorted(self):
        '''
        Prints the elements of the list in sorted order.
        '''

        newlist = sorted(self)
        print(newlist)
