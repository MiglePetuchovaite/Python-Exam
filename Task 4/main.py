# Turimas sąrašas, pvz.:

# canvas = [
#   "abc",
#   "ded"
# ]

# Sukurkite funkciją "addFrame", kuri pridėtų rėmelį ir grąžintų pamodifikuotą sąrašą:

# canvas_with_frame = [
#   "*****"
#   "*abc*",
#   "*ded*",
#   "*****"
# ]

# Pastaba: sąrašas gali ir neturėti nei vieno elemento arba turėtų tusčių elementų. pvz.
# canvas = [] arba canvas = [""]

# Jeigu sąrašas yra tusčias arba visi elementą tušti išmeskite klaidą - "Error: empty canvas provided".
# Beje, sąraše esantis tekstas, gali būti ir skirtingo ilgio. Todėl rėmelis turėtų būti brėžiamas pagal ilgiausią saraše esantį elementą.

canvas = [
  "abb",
  "ded",
  ]

def addFrame(canvas):
    if (len(canvas) == 0):
        raise Exception("Error: empty canvas provided")
    for element in canvas:
      if element != "":
        break
      raise Exception("Error: empty canvas provided")

    frame = "*" * (len(max(canvas)) + 2)
    canvas_with_frame = [frame]

    for str in canvas:
        canvas_with_frame.append("*" + str + "*")
    
    canvas_with_frame.append(frame)

    return canvas_with_frame

print(addFrame(canvas))