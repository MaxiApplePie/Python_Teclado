# First, ask the user for their name. Then, print out the greeting "Hello, NAME"
# Remember the uppercase H, the comma, and the space between words!
name = input('Write your name >> ')
print(f"Hello, {name.upper()}")

# Secondly, ask the user for their age and convert it into a number.
# Then, print out how many months that equals to (you'll have to multiply the age by 12).
age = input('Write your age >> ')
months = int(age) * 12
print(months)