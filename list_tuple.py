my_list = [1, 2, 3, 4, 5, 6]

print("primary id of my_list is: ", id(my_list), "list is", my_list)

my_list.append(7)

print("secondary id of my_list is: ", id(my_list), "list is", my_list)


my_tuples = (1, 2, 3, 4, 5, 6)

print("primary id of my_tuples is: ", id(my_tuples), "tuples is", my_tuples)

"""

id will be same after appending 

"""

