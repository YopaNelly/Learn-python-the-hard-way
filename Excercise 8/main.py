# Printing Printing
formatter = "{} {} {} {}"  # will take 4 positional args tuple. not more or less

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("Hi there I am Nelly", "Hope you are doing well", "Let keep doing our best.", "Python is nothing to fear"))
