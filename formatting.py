name = "Alice"
age = 30
address ="CORNAMADDY"

formatted_string = "My name is %s and I am %d years old live in %s." % (name, age, address)
print(formatted_string)

# This is a regular comment.
'''
This is a multiline comment
using triple quotes.
It won't be executed.
'''
"""
Common Format Specifiers
%s - String (or any object’s string representation)
%d - Integers (decimal format)
%f - Floating-point numbers
%% - Literal % character
"""

print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")


subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)


name = 'Ganymede'
planet = 'Mars'
gravity = '1.43'

template = """Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

print(template.format(name=name, planet=planet, gravity=gravity))


#distance between planets

first_planet = 149597870
second_planet = 778547200
distance_km = second_planet - first_planet
print(distance_km)

distance_mi = distance_km / 1.609344
print(distance_mi)