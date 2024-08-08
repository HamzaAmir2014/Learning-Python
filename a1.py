def seconds_difference(time_1, time_2):
    """ (number, number) -> number

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    """
    return time_2 - time_1


def hours_difference(time_1, time_2):
    """ (number, number) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    """
    time_1 = time_1 / 3600
    time_2 = time_2 / 3600

    return time_2 - time_1


def to_float_hours(hours, minutes, seconds):
    """ (int, int, int) -> float

    Return the total number of hours in the specified number
    of hours, minutes, and seconds.

    Precondition: 0 <= minutes < 60  and  0 <= seconds < 60

    >>> to_float_hours(0, 15, 0)
    0.25
    >>> to_float_hours(2, 45, 9)
    2.7525
    >>> to_float_hours(1, 0, 36)
    1.01
    """
    minutes = minutes / 60
    seconds = seconds / 3600
    return hours + minutes + seconds


def to_24_hour_clock(hours):
    """ (number) -> number

    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.

    Precondition: hours >= 0

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(48)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    >>> to_24_hour_clock(28.5)
    4.5
    """

    return hours % 24



### Write your get_hours function definition here:
def get_hour (total_seconds):
    """
    (number) -> number
    Calculate the total number of whole hours from a given number of seconds.

    This function takes an integer input representing the total number of seconds
    and returns the corresponding number of whole hours.

    Parameters:
    total_seconds (int): The total number of seconds.

    Returns:
    int: The total number of whole hours.

    >>> get_hour(3600)
    1

    >>> get_hour(7200)
    2

    >>> get_hour(3661)
    1

    >>> get_hour(0)
    0
    """
    total_seconds = total_seconds // 3600
    return total_seconds

### Write your get_minutes function definition here:
def get_minutes(total_seconds):
    """
    Calculate the remaining whole minutes after extracting hours from a given number of seconds.

    This function takes an integer input representing the total number of seconds,
    converts it to minutes, and then returns the remaining minutes after full hours 
    have been accounted for.

    Parameters:
    total_seconds (int): The total number of seconds.

    Returns:
    int: The remaining whole minutes after full hours have been extracted.

    Examples:
    --------
    >>> get_minutes(3600)
    0

    >>> get_minutes(3661)
    1

    >>> get_minutes(3720)
    2

    >>> get_minutes(59)
    0
    """
    total_seconds =  total_seconds // 60
    return total_seconds % 60

### Write your get_seconds function definition here:
def get_seconds(total_seconds):
    """
    Calculate the remaining seconds after extracting full minutes from a given number of seconds.

    This function takes an integer input representing the total number of seconds
    and returns the remainder when those seconds are divided by 60. This remainder
    represents the number of seconds left after accounting for full minutes.

    Parameters:
    total_seconds (int): The total number of seconds.

    Returns:
    int: The remaining seconds after full minutes have been extracted.

    Examples:
    --------
    >>> get_seconds(3600)
    0

    >>> get_seconds(3661)
    1

    >>> get_seconds(3725)
    5

    >>> get_seconds(59)
    59
    """
    return  total_seconds % 60

def time_to_utc(utc_offset, time):
    """ (number, float) -> float

    Return time at UTC+0, where utc_offset is the number of hours away from
    UTC+0.

    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    >>> time_to_utc(-1, 12.0)
    13.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(-1, 0.0)
    1.0
    >>> time_to_utc(-1, 23.0)
    0.0
    """
    if utc_offset > 0:
        utc_offset = -utc_offset
    else: 
        utc_offset = abs(utc_offset)

    return (time + utc_offset) % 24


def time_from_utc(utc_offset, time):
    """ (number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    # >>> time_from_utc(-7, 6.0)
    23.0
    # >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    # >>> time_from_utc(+1, 23.0)
    0.0
    """
    
    return (utc_offset + time) % 24