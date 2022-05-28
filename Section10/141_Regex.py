import re

email = 'lmc@outlook.fr'
expression = '[a-z\.]+'

matches = re.findall(expression, email)
name, domain = re.findall(expression, email)

print(matches)
print(domain)

# ---------------------------------------------------------------

price = 'Price: $47,189.50'
expre = 'Price: \$([\d,]*\.[\d])'

matches = re.search(expre, price)
print(matches.group(0))
print(matches.group(1))

value = float(matches.group(1))
