import functools
import operator
import os


# %% Capitalize Names

names = ['jack', 'tom', 'brown', 'sri']

# Normal
capital_names_1 = [name.capitalize() for name in names]

# Advanced
converter = operator.methodcaller('capitalize')
capital_names_2 = list(map(converter, names))


# %% Get the Real Part

numbers = [5+4j, 2+1j, 0, 3j, 1+5j]

# Normal
real_numbers_1 = []
for number in numbers:
    real_numbers_1.append(number.real)

# Advanced
getter = operator.attrgetter('real')
real_numbers_2 = list(map(getter, numbers))


# %% Get the Second Item

items = [os.path.splitext(file) for file in os.listdir()]  # splitext('main.py') --> ('main', '.py')

# Normal
extensions_1 = [item[1] for item in items]

# Advanced
extensions_2 = list(map(operator.itemgetter(1), items))


# %% Check If All the Answers Are True

true_answers = [2, 3, 6]
user_answers = [2, 3, 7]

# Normal
qualify_1 = True
for true_a, user_a in zip(true_answers, user_answers):
    if true_a != user_a:
        qualify_1 = False

# Advanced
qualify_2 = all(map(lambda x: operator.eq(*x), zip(true_answers, user_answers)))


# And all other operators (mathematical, statistical, comparative, bitwise, boolean, ...)
