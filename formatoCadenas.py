#Formato de cadenas en Python

#!Formato de signo de porcentaje (%)
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" % mass_percentage)
# On the Moon, you would weigh about 1/6 of your weight on Earth

print("""Both sides of the %s get the same amount of sunlight,
... but only one side is seen from %s because
... the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))
# Both sides of the Moon get the same amount of sunlight,
# but only one side is seen from Earth because
# the Moon rotates around its own axis when it orbits Earth.

#!El método format()
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage))
# On the Moon, you would weigh about 1/6 of your weight on Earth

print("""You are lighter on the {0}, because on the {0} 
... you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))
# You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth

print("""You are lighter on the {moon}, because on the {moon} 
... you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))
# You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth

#!Acerca de las cadenas f-strings
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")
# On the Moon, you would weigh about 1/6 of your weight on Earth


round2 = round(100/6, 1)
print(round)
# 16.7

print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")
# On the Moon, you would weigh about 16.7% of your weight on Earth

subject = "interesting facts about the moon"

# 'Interesting Facts About The Moon'
print(f"{subject.title()}")
