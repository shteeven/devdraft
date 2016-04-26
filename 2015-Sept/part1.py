import sys

""" This algorithm works in test case 1 """
def get_value(weights, position, span):
    values = weights[position:position + span]
    return values

def iter_blocks(blocks, weights, span):
    current_high = 0
    for i in range(blocks):
        span_vals = get_value(weights, i, span)
        val = sum(span_vals)
        if val > current_high:
            current_high = val
    return current_high


""" This algorithm works in test case 2 """
def values_generator(blocks, weights, span):
    cumulative_vals = ()
    for i in range(blocks):
        val_sum = sum(weights[i:(i + span)])
        cumulative_vals = cumulative_vals + (val_sum,)
    return cumulative_vals

def memoize(f):
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__


@memoize
def recursiveCrimeFighter(my_args):
    blocks, remaining, current_block, officer_span = my_args
    greatest_position = 0
    if current_block < blocks:
        for offset in range(current_block, blocks):
            try:
                officer_weight = true_vals[offset]
            except IndexError:
                break
            if remaining > 1:
                current_block_copy = officer_span + offset
                remaining -= 1  # remove officer on each dive
                my_args = (blocks, remaining, current_block_copy, officer_span)
                new_amount = recursiveCrimeFighter(my_args)
                remaining += 1  # add officer for next iter
                officer_weight += new_amount
            if officer_weight > greatest_position:
                greatest_position = officer_weight
    return greatest_position



@memoize
def recursiveCrimeFighter2(my_args):
    blocks, remaining, current_block, officer_span = my_args
    remaining = list(remaining)
    greatest_position = 0
    officer_weight_copy = 0
    if current_block < blocks:
        for offset in range(current_block, blocks):
            remaining.remove(officer_span)
            officer_weight = true_vals[officer_span][offset]
            for i in varieties:
                if i in remaining:
                    my_args = (blocks, tuple(remaining), (officer_span + offset), i)
                    new_amount = recursiveCrimeFighter2(my_args)
                    officer_weight_copy = new_amount + officer_weight
                if officer_weight_copy > greatest_position:
                    greatest_position = officer_weight_copy
            remaining.append(officer_span)
            if greatest_position == 0 or officer_weight > greatest_position:
                greatest_position = officer_weight
    return greatest_position



# retrieve sys arguments
blocks, variety = [int(x) for x in sys.stdin.readline().strip().split()]
weights = tuple(int(x) for x in sys.stdin.readline().strip().split())
temp = [int(x) for x in sys.stdin.readline().strip().split()]
total_crime = sum(weights)

# Run for test set 1
if variety == 1 and temp[1] == 1:
    val = iter_blocks(blocks, weights, temp[0])

# Run for test set 2
if variety == 1 and temp[1] != 1:
    true_vals = values_generator(blocks, weights, temp[0])  # officer_span)
    my_args = (blocks, temp[1], 0, temp[0])  # blocks, officer_dict, current_block, officer_span
    val = recursiveCrimeFighter(my_args)

# Run for test set 3
if variety != 1:
    true_vals = {}
    varieties = []
    remaining_officers = ()
    val = 0
    for i in range(0, variety * 2, 2):
        varieties.append(temp[i])
        # val of different spans
        true_val_set = values_generator(blocks, weights, temp[i])
        true_vals[temp[i]] = true_val_set
        for x in range(temp[i + 1]):
            remaining_officers = remaining_officers + (temp[i],)
    for i in varieties:
        my_args = (blocks, remaining_officers, 0, i)  # blocks, officer_dict, current_block, officer_span
        return_val = recursiveCrimeFighter2(my_args)
        if return_val > val:
            val = return_val

# write results
print(total_crime - val)