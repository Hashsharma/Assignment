import re

# Regex for contact numbers
phone_regex = "^(\\+\\d{1,2}\\s)?\\(?\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"

list1 = [
'2124567890',
'212-456-7890',
'(212)456-7890',
'(212)-456-7890',
'212.456.7890',
'212 456 7890',
'+12124567890',
'+12124567890',
'+1 212.456.7890',
'+212-456-7890',
'1-212-456-7890'
]
for i in list1:
    match = re.search(phone_regex, i)
    print(i, match)
