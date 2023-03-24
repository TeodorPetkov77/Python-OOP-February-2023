class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a") as file:
            file.write(f"Function '{self.func.__name__}' "
                       f"was called. Result: {self.func(*args, **kwargs)}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)

# 7.	*Store Results
# Create a class called store_results. It should be used as a decorator and store information about the executed functions in a file called results.txt in the format: "Function {func_name} was called. Result: {func_result}"
# Note: The solutions to this problem cannot be submitted in the judge system
# Examples
# Test Code	results.txt
# @store_results
# def add(a, b):
#     return a + b
#
# @store_results
# def mult(a, b):
#     return a * b
#
# add(2, 2)
# mult(6, 4)	Function 'add' was called. Result: 4
# Function 'mult' was called. Result: 24

