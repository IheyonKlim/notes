"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""
# def is_on_list(list,dayString):
#   if type(list):
#     for day in list:
#       if day == dayString:
#         return "True"
#   else :
#     return "It's not a list"

def is_on_list(list = [], word=""):
    if word in list:
        return "True"
    else:
        return "False"

# def get_x(list, number):
#   if type(list):
#     for index, value in enumerate(list):
#       if index == number:
#         return value
#   else :
#     return "It's not a list"      

def get_x(list=[], index=""):
    return list[index]

# def add_x(list, dayString):
#   if type(list):
#     list.append(dayString)
#     return list

def add_x(a_list =[], word=""):
    return a_list.append(word)

def remove_x(a_list=[], word=""):
    return a_list.remove(word)

# def remove_x(list, dayString):
#   if type(list):
#     list.remove(dayString)
#     return list
    
# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)


# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #
