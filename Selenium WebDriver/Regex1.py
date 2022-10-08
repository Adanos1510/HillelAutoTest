import re

text = 'With the help of the Hillel auto project, you will have the opportunity to get hands-on experience in manual testing.'

result = re.search(r".", text)
print(result)