def total_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds


"""Use this to convert time to total seconds."""


def convert_seconds_to_time(total_seconds):
    seconds = total_seconds % 60
    minutes = total_seconds // 60 % 60
    hours = total_seconds // 3600
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


"""Use this to convert total seconds to time."""
