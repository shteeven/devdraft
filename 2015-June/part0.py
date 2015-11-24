import sys

# returns the number of minions killed in a single chain atck
# N list of minions' health, X is atck pwr, and Y increments decrease in atck
def chain_spell(N, X, Y, minions):
    # Constraints: N < 10, X < 10000, Y < 10000
    # Note: N in test 3 has 10 values, causing it to fail; changed to N <= 10
    minions = minions[:10]
    if X >= 10000: X = 9999
    if Y >= 10000: Y = 9999

    minions.sort(reverse=True)  # order minions from greatest to least health
    mutated_list = list(minions)  # mutated list

    for i in minions:
        if i <= X:  # remove minion if atck pwr is > health
            mutated_list.remove(i)
            X -= Y  # apply atck pwr reduction
    killed = N - len(mutated_list)

    return killed

# retrieve system arguments
b = []
for line in sys.stdin:
    b.append([int(x) for x in line.split()])
result = str(chain_spell(b[0][0], b[0][1], b[0][2], b[1]))
write = sys.stdout.write
write(result)