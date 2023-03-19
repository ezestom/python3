#Aspectos básicos de las cadenas en Python

#Inmutabilidad de las cadenas
fact = "The Moon has no atmosphere."
newFact = fact + "No sound can be heard on the Moon."
print(newFact)

two_facts = fact + "No sound can be heard on the Moon."
two_facts
print(two_facts)

#Acerca del uso de comillas
moon_radius = "The Moon has a radius of 1,080 miles"
"We only see about 60% of the Moon's surface"
tripleComilla = """We only see about 60% of the Moon's surface, this is known as the "near side"."""

#Texto multilínea
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

multiline = """Facts about the Moon:
...  There is no atmosphere.
...  There is no sound."""
print(multiline)