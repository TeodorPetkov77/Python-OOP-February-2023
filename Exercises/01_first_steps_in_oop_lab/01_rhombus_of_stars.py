def draw_rhombus(stars):
    for i in range(1, stars + 1):
        print(" " * (stars - i) + "*" + " *" * (i - 1))
    for i in range(stars - 1, 0, -1):
        print(" " * (stars - i) + "*" + " *" * (i - 1))


draw_rhombus(int(input()))

# https://judge.softuni.org/Contests/Practice/Index/1934#0

# 1.	Rhombus of Stars
# Create a program that reads a positive integer N as input and prints on the console a rhombus with size n:
# Examples
# Input	Output
# 1	*
# 2	 *
# * *
#  *
# 3	  *
#  * *
# * * *
#  * *
#   *
# 4	   *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *