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

#!Argumentos de variable
def variable_length(*args):
    print(args)

variable_length(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

variable_length()
# ()
variable_length("one", "two")
# ('one', 'two')
variable_length(None)
# (None,)

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"

print(sequence_time(4, 14, 18))
'Total time to launch is 36 minutes' 
print(sequence_time(4, 14, 48))
'Total time to launch is 1.1 hours'

#!Argumentos de palabra clave valor
def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day="Wednesday", pilots=3)
{'tanks': 1, 'day': 'Wednesday', 'pilots': 3}

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")
# 3 astronauts assigned for this mission:
# captain: Neil Armstrong
# pilot: Buzz Aldrin
# command_pilot: Michael Collins

# crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", pilot="Michael Collins")
#   File "<stdin>", line 1
# SyntaxError: keyword argument repeated: pilot