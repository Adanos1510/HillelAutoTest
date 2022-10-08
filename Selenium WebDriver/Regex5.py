import re

s = 'Keep track of your replacement schedule and plan your vehicle maintenance expenses in advance.'

match = re.search(r'[abcd]', s)

print('Start Index:', match.start())
print('End Index:', match.end())
print(match)