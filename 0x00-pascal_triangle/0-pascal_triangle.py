#!/usr/bin/env python3
"""A script to determine pascal's triangle for any number"""

def pascal_triangle(n):
    """Returns a list of list representing the
    pascal's triangle for the number n
    """
    pt = []  # will be a list of lists representing the Pascal's triangle

    for x in range(1, n+1):
        # print(x)
        if x == 1:
            output = [1]
            pt.append(output)
        else:
            current_list = pt[x - 2]
            # get length of current list
            n_list = len(current_list)
            i = 0
            output = [1]
            while (i < n_list-1):
                output.append(current_list[i] + current_list[i+1])
                i += 1

            # append 1 to the end of the generated list
            output.append(1)
            # append output to pt
            pt.append(output)

    return pt
