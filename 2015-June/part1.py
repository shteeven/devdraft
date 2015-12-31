import sys
import random


def cascade(index, item_list):
    current_domino = item_list[index]
    if current_domino == 0:
        return 0
    cascade_values = [0]  # error in max() if list is empty
    for i in range(current_domino+1):  # i = domino fallen on by current_domino
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
def createTestSet(num):
    test_set = []
    for i in range(num):
        x = random.randint(0, 200)
        test_set.append(x)
    return test_set

# num_dominoes = int(sys.stdin.readline())
# dominoes = sys.stdin.readline()
num_dominoes = 500000
right = createTestSet(num_dominoes)

# right = [int(x) for x in dominoes.split()]
left = right[::-1]

# get results from both cascades
result_right = iterate_dominoes(num_dominoes, right)
result_left = iterate_dominoes(num_dominoes, left)[::-1]

# output
write = sys.stdout.write
write(" ".join(str(x) for x in result_right) + '\n')
write(" ".join(str(x) for x in result_left))


