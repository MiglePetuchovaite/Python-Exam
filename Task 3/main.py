# Sukurkite funkciją "addDigits", kuri priims sveiką skaičių nuo 10 iki 999 ir grąžins jo skaitmenų sumą. 

# Pvz.
# Jeigu duota 34, funckiją turėtų grąžinti 7.
# Jeigu duota 999, funckija turėtų grąžinti 27.


def addDigits(number):
  if number < 10 or number > 999:
    return None
  return sumDigits(number)

def sumDigits(number):
  sum = 0
  for digit in str(number):
    sum += int(digit)
  return sum

print(addDigits(34))
