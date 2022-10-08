import re

text = 'Hillel auto developed in Hillel IT school for educational purposes of QA courses.'

result = re.search(r"[A-Z]+", text)
print(result)