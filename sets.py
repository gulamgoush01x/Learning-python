# s  = {1,2,3,4,5,2,2,4,5,}

# s.add(9)

# print(s)

# empty_set = set()
# print(type(empty_set))



# sets method 

# remove

# s = {1,2,3,4,5,2,2,4,5,}
# s.remove(2)

# print(s)


# clear

# s = {1,2,3,4,5,2,2,4,5,}
# s.clear()

# print(s)


# pop

# s = {1,2,3,4,5,2,2,4,5,}
# print(s)
# s.pop()
# print(s)




# union & intersection

# s1 = {1,2,3,4,5,2,2,4,5}
# s2 = {1,3,4,9,4,5,3,6}

# print(s1.union(s2))
# print(s1.intersection(s2))





# practics problem


# info = [
#     ("Alice", "Math"),
#     ("Bob", "Science"),
#     ("Alice", "Science"),
#     ("Charlie", "Math"),
#     ("Bob", "Math"),
#     ("Alice", "English"),
#     ("Charlie", "English"),
# ]

# 1st method
# 1st problem 

# unique_course = set()
# for tup in info:
#     unique_course.add(tup[1])
# print(unique_course)

# 2nd method

# unique_course = set()
# for name,courses in info:
#     print(name,courses)


# 2nd problem

# for name,courses in info:
#     if(courses == "English"):
#         print(name)


# 3rd problem

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

dict= {}
for name,course in info:
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)





