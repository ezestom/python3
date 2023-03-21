#Funciones
#!Funciones sin argumentos
def rocket_parts():
    print("payload, propellant, structure")

# rocket_parts()

# output = rocket_parts()
# payload, propellant, structure
# output is None


def rocket_parts():
     return "payload, propellant, structure"

output = rocket_parts()
print(output)

#!Argumentos opcionales y requeridos any()

any([True, False, False])
True
any([False, False, False])
False

# >>> any()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: any() takes exactly one argument (0 given)

vacia = str()
''
completa = str(15)
'15'

print(vacia)
print(completa)

#?Uso de argumentos de función en Python
#!Exigencia de un argumento
def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
    
#     >>> distance_from_earth()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: distance_from_earth() missing 1 required positional argument: 'destination'

distance_from_earth("Moon")
print(distance_from_earth("Moon"))
# '238,855'

distance_from_earth("Saturn")
# 'Unable to compute to that destination'
print(distance_from_earth("Saturn"))

#!Varios argumentos necesarios
def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24


print(days_to_complete(238855, 75))
# 132.69722222222222

#!Funciones como argumentos

total_days = days_to_complete(238855, 75)
print(round(total_days))
# 133

print(round(days_to_complete(238855, 75)))
# 133

#!Excercise

def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank} 
    """
    print(output)

generate_report(80, 70, 75)