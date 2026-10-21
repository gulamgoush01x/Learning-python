# info = {
#     "name" : "aarav",
#     "CGPA" : "7.5",
#     "sub" : ["math", "science"]
# }

# print(info["name"])
# print(info["sub"])

# info = {
#     "name" : "aarav",
#     "CGPA" : 7.5,
#     "sub" : ["math", "science"]
# }
# info["CGPA"] = 8.0
# print(info["name"])
# print(info["CGPA"])

 


# dictionary type 




# key
 
# info = {
#     "name" : "aarav",
#     "CGPA" : "7.5",
#     "sub" : ["math", "science"]
# }
# dict_key =list(info.keys())
# print(type(dict_key))




# value

# info = {
#     "name" : "aarav",
#     "CGPA" : "7.5",
#     "sub" : ["math", "science"]
# }
# dict_val =list(info.values())
# print(dict_val)



# iteams

# info = {
#     "name" : "aarav",
#     "CGPA" : "7.5",
#     "sub" : ["math", "science"],
#     "college" : "technocrats institute of technology"
# }

# print(info.items())


# get method


# info = {
#     "name" : "aarav",
#     "CGPA" : "7.5",
#     "sub" : ["math", "science"],
#     "college" : "technocrats institute of technology"
# }

# print(info.get("cgpa2"))

# print("end of the code")



# update method 


info = {
    "name" : "aarav",
    "CGPA" : "7.5",
    "sub" : ["math", "science"],
    "college" : "technocrats institute of technology"
}

info.update({
    "city"  : "muzaffar pur",
    "pin code" : 842004
})

print(info)



