# Prompting and Passing
from sys import argv

pydev_imports.execfile(file, globals, locals)  # execute the script
script, user_name = argv
play = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(play)

print(f"Where do you live {user_name}?")
lives = input(play)

print("What kind of computer do you have?")
computer = input(play)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
