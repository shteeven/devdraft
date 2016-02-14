import sys


def cascade(index, true_index, reach_list):
    current_domino = reach_list[index]
    if current_domino == 0:
        return true_index
    end = index + current_domino
    if end > 0:
        reach_values = reach_list[index:] + [current_domino + true_index]
    else:
        reach_values = reach_list[index:index + current_domino + 1] + [current_domino + true_index]
    result = max(reach_values)
    return result  # return greatest cascade+offset


def iterate_dominoes(num_dominoes, domino_heights):
    for i in range(num_dominoes):
        x = (i + 1) * -1  # x provides a neg int so that indexes start at end
        true_index = num_dominoes + x
        domino_heights[x] = cascade(x, true_index, domino_heights)

    for i in range(num_dominoes):
        domino_heights[i] -= i
    return domino_heights

# retrieve system arguments
num_dominoes = int(sys.stdin.readline())
dominoes = sys.stdin.readline()

right = [int(x) for x in dominoes.split()]
left = right[::-1]


# get results from both cascades
result_right = iterate_dominoes(num_dominoes, right)
result_left = iterate_dominoes(num_dominoes, left)[::-1]

# for i in

# output
write = sys.stdout.write
write(" ".join(str(x) for x in result_right) + '\n')
write(" ".join(str(x) for x in result_left))
