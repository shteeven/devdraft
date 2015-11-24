import sys

__author__ = 'stevenbarnhurst'

MINUTES_IN_DAY = 24 * 60


def toMinutes(hhmm):
    """Converts a time to minutes past midnight.

	Converts a string in the format hh:mm (of a 24-hour clock)
	to minutes past midnight.  For example, 01:30 becomes 90.

	Args:
		hhmm: a string in the format hh:mm such as 23:41

	Returns:
		how many minutes past midnight have elapsed

	"""
    parts = hhmm.split(":")
    return int(parts[0]) * 60 + int(parts[1])


def formatMinutes(minutes):
    """Converts minutes past midnight to a time.

	Converts a number of minutes past midnight into a String representation
	in the format hh:mm of a 24-hour clock.  For example, 90 becomes 01:30.

	Args:
		minutes: time past midnight

	Returns:
		the time in format h:mm or hh:mm, such as 23:41

	"""
    return "%02d:%02d" % (minutes // 60, minutes % 60)


class LightRailApp:
    """Models the stations and trains of a light rail system.

	Models the stations and trains of a light rail system
	to calculate when the next train arrives at a particular stop.

	"""

    def __init__(self, travelTimes, intervalStarts, intervalPeriods,
                 northFirst, northLast, southFirst, southLast):
        """Initializes the App so it can answer queries.

		Args:
			travelTimes: How long it takes (in minutes) to go between stops i and i +
				1, either northbound or southbound.
			intervalStarts: The starts of time intervals that describe the frequency of
				trains leaving from the northernmost and southernmost
				stations. An interval starts at the ith entry and ends 1
				minute earlier than the (i + 1)th entry. The starts should
				be ordered chronologically.
			intervalPeriods: How frequently (in minutes) trains leave from the
				northernmost and southernmost stations during a time interval described by
				intervalStarts. That is, between the times intervalStarts[i]
				and intervalStarts[i + 1] - 1, trains leave every
				intervalPeriods[i] minutes. The last element describes the
				frequency until the last train leaves.
			northFirst: When the first northbound train leaves the southernmost
				station, as minutes past midnight.
			northLast: The latest a northbound train may leave the southernmost
				station. This does not guarantee a train leaves then--it just
				means a train won't leave the southernmost station if it's
				past this time.  Expressed as minutes past midnight.
			southFirst: When the first southbound train leaves the northernmost
				station, as minutes past midnight.
			southLast: The latest a southbound train may leave the northernmost
				station. This does not guarantee a train leaves then--it just
				means a train won't leave the northernmost station if it's
				past this time.  Expressed as minutes past midnight.
		"""
        self.travelTimes = travelTimes
        self.intervalStarts = intervalStarts
        self.intervalPeriods = intervalPeriods
        self.northFirst = northFirst
        self.northLast = northLast
        self.southFirst = southFirst
        self.southLast = northLast

    def nextTrain(self, leave, stop, north):
        """Finds when the next train will arrive.

		Finds the earliest time at or after the given time when a train
		will arrive at the stop.

		Args:
			leave: the time at or after the train may leave.
			stop: which stop to leave from (0 being southernmost)
			north (bool): whether the train is northbound (otherwise southbound)

		Returns:
			the earliest time a train will leave at or after the time given.
		"""

        # How many minutes ahead this stop is from the first station
        # (the "first" station is the southernmost station if northbound,
        # and northernomst station if southbound).
        offset = None

        # The earliest departure time of a train at the first station
        first = None

        # The latest possible departure time of a train at the first stop
        last = None

        if north:
            first = self.northFirst
            last = self.northLast
            offset = sum(self.travelTimes[:stop])
        else:
            first = self.southFirst
            last = self.southLast
            offset = sum(self.travelTimes[stop + 1:])

        # Normalized leave time--when the rider would want to leave, if they were
        # at the first station.
        normLeave = leave - offset

        # If outside train operating hours, just return the first train.
        if normLeave > last or normLeave < first:
            return first + offset

        # When the desired train leaves the first station
        trainLeave = first
        i = 0
        while trainLeave < normLeave:
            trainLeave += intervalPeriods[i]
            if i + 1 < len(self.intervalStarts) and trainLeave >= \
                    self.intervalStarts[i + 1]:
                i += 1
        return trainLeave + offset


# Main
if __name__ == "__main__":
    input = sys.stdin

    # read stop count
    stopCount = int(input.readline().strip())

    # read stops
    stops = [int(v) for v in input.readline().strip().split(" ")]


    # Read first and latest departure times, for northbound and southbound
    northFirst, northLast = [toMinutes(v) for v in
                             input.readline().strip().split(" ")]
    southFirst, southLast = [toMinutes(v) for v in
                             input.readline().strip().split(" ")]


    # read intervals and periods
    intervalCount = int(input.readline().strip())
    intervalStarts = []
    intervalPeriods = []
    for i in range(intervalCount):
        parts = input.readline().strip().split(" ")
        intervalStarts.append(toMinutes(parts[0]))
        intervalPeriods.append(int(parts[1]))

    # read query count
    queryCount = int(input.readline().strip())

    # read and process queries
    app = LightRailApp(stops, intervalStarts, intervalPeriods,
                       northFirst, northLast, southFirst, southLast)
    for i in range(queryCount):
        parts = input.readline().strip().split(" ")
        print(formatMinutes(
            app.nextTrain(toMinutes(parts[0]), int(parts[1]), parts[2] == 'N')))
