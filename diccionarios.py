#diccionarios de Python

planet = {
    'name': 'Earth',
    'moons': 1
}

opcion1 = planet.get('name')
opcion2 = planet['name']
print("There is two options to print ",opcion1," and " ,opcion2)
# Earth

# wibble1 = planet.get('wibble') # -------> Returns None
# print(wibble1)
# wibble2 = planet['wibble'] # -----------> Throws KeyError
# print(wibble2)

#!Modificación de valores de diccionario
planet.update({'name': 'Makemake'})
print(planet['name'])
# Makemake
planet['name'] = 'NewMakemake'
print(planet['name'])
# NewMakemake

# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Using square brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79

print(planet)

#!Adición y eliminación de claves
planet['orbital period'] = 4333
print(planet)

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }
planet.pop('orbital period')
print(planet)
# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }

#!Tipos de data complejos
# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}
print(planet)

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')

#!Excercise
planet = {
    'name': 'Mars',
    'moons': 2
}
print(f'{planet["name"]} has {planet["moons"]} moon(s)')

planet['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}
print(planet)
print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]} and the Equatorial Line is {planet["circumference (km)"]["equatorial"]} km long')

#----------------> Programación dinámica con diccionarios

#!Recuperación de todas las claves y valores de un diccionario
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
for key in rainfall.keys():
    print(f'{key} : {rainfall[key]}cm')

#!Determinación de la existencia de una clave en un diccionario
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

# Because december exists, the value will be 3.1

#!Recuperación de todos los valores
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter')

# Output:
# There was 10.8cm in the last quarter

#!Excercise
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
moons = planet_moons.values()
total_planets = len(planet_moons.keys())
print(f'There are {total_planets} planets in the solar system and {sum(moons)} moons in the solar system')

total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

average = total_moons / total_planets

print(f'Each planet has an average of {average} moons')




