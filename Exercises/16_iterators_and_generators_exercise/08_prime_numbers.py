def get_primes(nums: list):
    for num in nums:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                yield num


print(list(get_primes([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])))

# https://judge.softuni.org/Contests/Compete/Index/1945#7

# 8.	Prime Numbers
# Create a generator function called get_primes() which should receive a list of integer numbers and return a list containing only the prime numbers from the initial list. You can learn more about prime numbers from here:
# Note: Submit only the function in the judge system
# Examples
# Test Code	Output
# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))	[2, 3, 5]
# print(list(get_primes([-2, 0, 0, 1, 1, 0])))	[]