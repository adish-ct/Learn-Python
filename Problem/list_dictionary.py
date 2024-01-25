"""
Print name of students, who doesn't have age field.

"""

my_list = [{'name': 'adish', 'age': 20}, {'name': 'suaida'}, {'name': 'adarsh', 'age': 20}]

for i in my_list:
    if 'age' not in i:
        print(i['name'])



data = {'Math':89, 'Physics':83, 'Chemistry':87}

