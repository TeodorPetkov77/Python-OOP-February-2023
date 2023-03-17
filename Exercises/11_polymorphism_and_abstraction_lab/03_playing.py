def start_playing(obj):
    return obj.play()


class Guitar:
    def play(self):
        return "Playing the guitar"


guitar = Guitar()
print(start_playing(guitar))


class Children:
    def play(self):
        return "Children are playing"


children = Children()
print(start_playing(children))

# https://judge.softuni.org/Contests/Practice/Index/1942#1

# 3.	Playing
# Create a function called start_playing which will receive an instance and will return its play() method.
# Submit only the start_playing function in the judge system
# Examples
# Test Code	Output
# class Guitar:
#     def play(self):
#         return "Playing the guitar"
#
# guitar = Guitar()
# print(start_playing(guitar))	Playing the guitar
# class Children:
#     def play(self):
#         return "Children are playing"
#
# children = Children()
# print(start_playing(children))	Children are playing
