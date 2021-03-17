first = 'Ben'
last = 'Waples'

# message = first + ' [' + last + '] is a coder'

# formatted string
msg = f'{first} [{last}] is a coder'
print(msg)

string = 'hello my name is random'
# len() to find length
print(len(string))

# we can still call methods on things, .upper() doesnt mutate original string
print(string.upper())
print(string)

# still can find things, I wonder if not mutating things is common in py
print(string.replace('o', 'ow'))
print(string)
