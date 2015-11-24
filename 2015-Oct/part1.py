import sys

__author__ = 'stevenbarnhurst'


###################
# program functions
###################
def determine_hour(time):
    hour = int(time / 60)
    return hour


def recursive_wait_calculator(current_time, attractions_remaining):
    current_hour = determine_hour(current_time)
    global least_wait
    for index, current_attraction in enumerate(attractions_remaining):

        # wait time with this attraction and current time
        attractions_current_wait = attractions_wait[current_attraction][
            current_hour]
        current_time += attractions_current_wait

        # terminates current branch if time is already exceeded
        # make sure that this least time is not counted
        if current_time > closing_time * 60:
            return least_wait + closing_time * 60

        # remove current_attraction
        removed_attraction = attractions_remaining.pop(index)

        if attractions_remaining:
            # dive deeper
            new_least_wait = recursive_wait_calculator(current_time,
                                                       attractions_remaining)
            if new_least_wait < least_wait:
                least_wait = new_least_wait
        else:
            return current_time - arrival_time

        # insert removed attraction and remove wait from current wait
        attractions_remaining.insert(index, removed_attraction)
        current_time -= attractions_current_wait

    return least_wait


def recursive_wait_calculator_2(current_wait, attrs_remaining):

    for index, current_attr in enumerate(attrs_remaining):
        current_hour = determine_hour(current_wait)
        if current_hour < closing_time:
            attr_wait = attractions_wait[current_attr][current_hour]
            removed_attr = attrs_remaining.pop(index)
            current_wait += attr_wait
            print recursive_wait_calculator_2(current_wait, attrs_remaining)
            attrs_remaining.insert(index, removed_attr)
            current_wait -= attr_wait


    return current_wait

#######################
# READ INPUT AND ASSIGN
#######################
attractions_count, closing_time = [int(i) for i in sys.stdin.readline().split()]
attractions_wait = {}
for i in range(attractions_count):
    # GLOBAL
    attractions_wait[i] = [int(x) for x in sys.stdin.readline().split()]
guest_count = int(sys.stdin.readline())

guest_info = []
for i in range(guest_count):
    # arrival time, num of desired attractions, attractions guest selected
    info = (int(sys.stdin.readline()), int(sys.stdin.readline()),
            [int(x) for x in sys.stdin.readline().split()])
    guest_info.append(info)

#############
# RUN PROGRAM
#############
for i in range(guest_count):
    # beginning time
    least_wait = closing_time * 60 + 1
    arrival_time = guest_info[i][0]
    guest_attractions = guest_info[i][2]
    print(guest_attractions)
    winning_time = recursive_wait_calculator_2(arrival_time, guest_attractions)
    print(winning_time)
