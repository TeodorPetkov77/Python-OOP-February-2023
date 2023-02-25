class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds += 1
        self.minutes += 1 if self.seconds > 59 else 0
        self.hours += 1 if self.minutes > 59 else 0
        self.seconds = 0 if self.seconds > 59 else self.seconds
        self.minutes = 0 if self.minutes > 59 else self.minutes
        self.hours = 0 if self.hours > 23 else self.hours
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"


# https://judge.softuni.org/Contests/Compete/Index/1937#1

# 2.	Time
# Create a class called Time. Upon initialization, it should receive hours, minutes, and seconds (integers). The class should also have class attributes max_hours equal to 23, max_minutes equal to 59, and max_seconds equal to 59. You should also create 3 additional instance methods:
# -	set_time(hours, minutes, seconds) - updates the time with the new values
# -	get_time() - returns "{hh}:{mm}:{ss}"
# -	next_second() - updates the time with one second (use the class attributes for validation) and returns the new time (use the get_time() method)
# Examples
# Test Code	Output
# time = Time(9, 30, 59)
# print(time.next_second())	09:31:00
# time = Time(10, 59, 59)
# print(time.next_second())	11:00:00
# time = Time(23, 59, 59)
# print(time.next_second())	00:00:00