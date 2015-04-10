"""
Python debugging exercise.

Tasks:

1) Convert to Python 3 compatible.
2) Remove any syntax or semantic errors.
3) Verify correctly working state.
4) Submit a pull request with the corrected version.
"""

class Time(object):
    """represents the time of day.
       attributes: hour, minute, second
    """
    def __init__(self, h=12, m=0, s=0):
        self.hour = h
        self.minute = m
        self.second = s
        if self.validate():
            raise ValueError("Bad time data")

    def print_time(self):
        print '%.2d:%.2d:%.2d' % (self.hour, self.minute,
                                  self.second)

    def time_to_int(self):
        """Computes the number of seconds since midnight.
        """
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds


    def validate(self):
        """Checks whether a Time object satisfies the invariants.
        """
        if self.hour <= 0 or self.minute <= 0 or self.second <= 0:
            return False
        elif self.minute > 60 or self.second > 60:
            return False
        else:
            return True


def add_times(t1, t2):
    """Adds two time objects.
    """
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def main():
    # if a movie starts at noon...
    noon_time = Time(12, 1, 1)

    print 'Starts at',
    print_time(noon_time)

    # and the run time of the movie is 109 minutes...
    movie_minutes = 109
    run_time = int_to_time(movie_minutes * 60)
    print 'Run time',
    print_time(run_time)

    # what time does the movie end?
    end_time = add_times(noon_time, run_time)
    print 'Ends at',
    print_time(end_time)

if __name__ == '__main__':
    main()