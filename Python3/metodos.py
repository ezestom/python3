#Métodos de cadena en Python

title = "temperatures and facts about the moon".title()
print(title)

heading = "temperatures and facts about the moon"
imprimir1 = heading.title()
print(imprimir1)

#!División de una cadena
temperatures = """Daylight: 260 F
... Nighttime: -280 F"""
# print(temperatures)
# print(temperatures .split())

split = temperatures .split('\n')
['Daylight: 260 F', 'Nighttime: -280 F']
print(split)

#Búsqueda de una cadena
search1 = "Moon" in "This text will describe facts and challenges with space travel"
False
search2 = "Moon" in "This text will describe facts about the Moon"
True
print(search1)
print(search2)

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""

findFalse = print(temperatures.find("Moon"))
-1
findTrue = print(temperatures.find("Mars"))
68



count = temperatures.count("Mars")
1
count2 = temperatures.count("Moon")
0

print(count)
print(count2)

lower = "ThE MooN AnD ThE Earth".lower()
print(lower)

upper = "ThE MooN AnD ThE Earth".upper()
print(upper)

temperatures = "Mars Average Temperature: -60 C"

parts = temperatures.split(':')
print(parts)
['Mars average temperature', ' -60 C']
partsSerach = parts[-1]
' -60 C'
print(partsSerach)


mars_temperature = "The highest temperature on Mars is about 30 C and the lowest is -140.09 C"
for item in mars_temperature.split():
     if item.isnumeric():  # < = or item.isdecimal()
       print(item)
...
30

#!Valores negativos
empiezaConBarra = "-60".startswith('-')
True
print(empiezaConBarra)

if "30 C".endswith("C"):
    print("This temperature is in Celsius")

#'This temperature is in Celsius'

#!Transformar texto
replace = "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C")
print(replace)
'Saturn has a daytime temperature of -170 degrees C, while Mars has -28 C.'

text = "Temperatures on the Moon can vary wildly."
returnFalse = "temperatures" in text
False
returnTrue = "temperatures" in text.lower()
True
print(returnFalse)
print(returnTrue)

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
print(moon_facts)

'\n'.join(moon_facts)
print(moon_facts)
'The Moon is drifting away from the Earth.\nOn average, the Moon is moving about 4cm every year'


#!Exercices
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

sentences = text.split(".")
print(sentences)

# Enter code below:
for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence)
