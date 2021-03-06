"""
Copyright (c) 2020, Souvik Ghosh.

Distributed under the terms of the MIT License.

The full license is in the file LICENSE, distributed with this software.

Created on Feb 25, 2020

@author
"""

def func_list():
    x = input("\n input the items of list: ")
    return list(x)


if __name__ == "__main__":    ## only runs in this environment.
    i = 0
    number_of_lists = int(input("enter the number of lists to input: "))
    while i <= (number_of_lists - 1):
        updated_list_1 = func_list()  ## returns a list with the input entries.
        print(updated_list_1)         ## prints the list.
        for j in updated_list_1:      ## iterates over the items of the list.
            print(j, end=' ')         ## prints individual items of the list.
        i += 1
