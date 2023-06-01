from random import randint as generate_number, choice
from person import Person
from calculator import addition, subtraction
from termcolor import colored, cprint
import emoji

from decouple import config
print(generate_number(1, 10))

teacher = Person('Jim', 25)
print(teacher.full_name + ' ' + str(teacher.age))

print(addition(8, 2))



import sys

from termcolor import colored, cprint

text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
print(text)
cprint("Hello, World!", "green", "on_red")

print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")
print_red_on_cyan("Hello, World!")
print_red_on_cyan("Hello, Universe!")

for i in range(10):
    cprint(i, "magenta", end=" ")

cprint("Attention!", "red", attrs=["bold"], file=sys.stderr)


print(emoji.emojize('Python is :thumbs_up:'))

print(config('DATABASE_URL'))
num = config('COMMENTED', default='0', cast=int)
print(num * 2)