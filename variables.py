from datetime import date;

# Tipos de Datos

# Tipo Numerico => int, float, complex, no
# Tipo Texto => str
# Tipo Booleano => True, False


# Examples
planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string 
distance_to_alpha_centauri = 4.367 # looks like a float !!!!

# Usar una funcion
type(distance_to_alpha_centauri) ## <class 'float'>

# Dates
# from datetime import date;

todayDate = date.today();
print(todayDate);
print("Today's date:", todayDate);
todayDAte2 = print("Today's date is: " + str(date.today()))

# Import para capturar elementos de la consola

import sys

# print(sys.argv)
# print(sys.argv[0]) # program name
# print(sys.argv[1]) # first arg


print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings is " + name)

print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(first_number + second_number)
print(int(first_number) + int(second_number));