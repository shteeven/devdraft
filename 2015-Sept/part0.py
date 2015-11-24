import sys

# List of all possible combinations; list compiled by helper functions not
# submitted with code block below.
word_list = ['BARAB', 'FIZIF', 'FIZAB', 'ZABAZ', 'ZABAR', 'BAZIF', 'BAZAB',
             'ZIFIZ', 'RABAZ', 'RABAR', 'ZIF', 'ZAB', 'FIZ', 'BAZ', 'BAR',
             'RAB']

# checks to see if the string contains a compound or complex compound
def is_compound(string):
    for i in word_list:
        if i in string:
            return i
    return False


# Perform swap and test if swap has a match; if no match, return original string
def do_swap(string, position):
    # conver str to list
    new_string = list(string)
    # perform swap of letters
    new_string.insert((position + 1), new_string.pop(position))
    # create new str
    new_string = ''.join(new_string)
    # test for match
    compound = is_compound(new_string)
    if not compound:
        # move is refused; original string returned
        return string
    while compound:
        # move accepted and new sting produced
        new_string = new_string.replace(compound, '')
        compound = is_compound(new_string)
        if not compound:
            return new_string


# retrieve sys arguments
length = int(sys.stdin.readline().strip())
string = sys.stdin.readline().strip()
moves = int(sys.stdin.readline().strip())
positions = [int(x) for x in sys.stdin.readline().strip().split()]

# perform search for compounds; loop for each 'move' passed to app
for position in positions:
    string = do_swap(string, position)

# write results
print(string)