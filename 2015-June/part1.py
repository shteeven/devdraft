__author__ = 'stevenbarnhurst'
# your code goes here
import sys

def cascade(index, item_list):
    current_domino = item_list[index] + 1
    cascade_values = [0]  # error in max() if list is empty
    for i in range(current_domino):  # i = domino fallen on by current_domino
        b = i + index  # b iterates through indexes which the domino falls
        if b >= 0:  # does domino reach EOList
            break
        else:  # if domino falls on a cascaded item, add item+offset(i) to list
            cascade_values.append(item_list[b] + i)
    return max(cascade_values)  # return greatest cascade+offset


def iterate_dominoes(num_dominoes, domino_heights):
    for i in range(num_dominoes):
        x = (i + 1) * -1  # x provides a neg int so that indexes start at end
        domino_heights[x] = cascade(x, domino_heights)
    return domino_heights

# retrieve system arguments
right = []
for line in sys.stdin:
    right.append([int(x) for x in line.split()])
left = [right[0], right[1][::-1]]

# get results from both cascades
result_right = iterate_dominoes(right[0][0], right[1])
result_left = iterate_dominoes(left[0][0], left[1])[::-1]

# output
write = sys.stdout.write
write(" ".join(str(x) for x in result_right) + '\n')
write(" ".join(str(x) for x in result_left))