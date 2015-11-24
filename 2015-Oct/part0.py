import sys

__author__ = 'Steven Barnhurst'


def create_dict(times_between_attractions, num_attractions):
    times_dict = {}
    for i in range(num_attractions):
        total_time = 0

        for x in range(i+1, num_attractions + i):
            if x >= num_attractions:
                x -= num_attractions
            total_time += times_between_attractions[x-1]
            times_dict[(i, x)] = total_time
    return times_dict


def calc_guest_time(guest_pref, times_dict):
    total_guest_travel_time = 0
    num_attractions = len(guest_pref)
    for i in range(num_attractions):
        # exit at the last ride
        if i >= num_attractions - 1:
            break
        start_attr = guest_pref[i]
        end_attr = guest_pref[i+1]
        if times_dict[(start_attr, end_attr)] > times_dict[(end_attr, start_attr)]:
            guest_travel_time = times_dict[(end_attr, start_attr)]
        else:
            guest_travel_time = times_dict[(start_attr, end_attr)]
        total_guest_travel_time += guest_travel_time
    return total_guest_travel_time


num_attractions = int(sys.stdin.readline())
time_between = [int(x) for x in sys.stdin.readline().split()]
num_guests = int(sys.stdin.readline())
the_list = []
for i in range(num_guests):
    the_list.append((int(sys.stdin.readline()), [int(x) for x in sys.stdin.readline().split()]))

my_dict = create_dict(time_between, num_attractions)

for i in the_list:
    print(calc_guest_time(i[1], my_dict))


#
# guest_one = [0, 1]
# guest_one_num = 2
#
# guest_two = [0, 5, 3]
# guest_two_num = 3
#
# guest_three = [0, 4, 2, 5]
# guest_three_num = 4
#
#
# my_dict = create_dict(time_between, num_attractions)
#
#
# calc_guest_time(guest_three, my_dict)
