import re

s = 'With the help of the Hillel auto project, you will have the opportunity to get hands-on experience in manual testing.'

match = re.search(r'auto', s)

print('Start Index:', match.start())
print('End Index:', match.end())