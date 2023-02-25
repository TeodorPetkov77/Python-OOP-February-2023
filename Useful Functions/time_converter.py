def time_to_total_seconds(hours, minutes, seconds):
    return (hours * 3600 + minutes * 60 + seconds) % 86400


"""Use this to convert time to total seconds."""


def seconds_to_time(total_seconds):
    total_seconds %= 86400
    seconds = total_seconds % 60
    minutes = total_seconds // 60 % 60
    hours = total_seconds // 3600

    return hours, minutes, seconds


"""Use this to convert total seconds to time."""
