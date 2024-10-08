# dictionary in python

birth_day = {
    "Soujanya": "30-08-1996",
    "Abhi": "08-09-1993",
    "Amma": "19-08-1973",
    "Daddy": "05-08-1963",
}

# dictionary is order, it display elements in the ordered elements added

print(birth_day)

# access value in dictionary using key

print(birth_day["Soujanya"])

# If key not there in dictionary it will give error
#print(birth_day["Sheela"])

# to avoid key error , we can go with get method to fetch the values from dictionary
# if key found it will give value , else print "Not found"

print(birth_day.get("Soujanya", "Not found"))
print(birth_day.get("ddd", "ddd Not found"))

# add new element in dictionary

birth_day["Sheela"] = "12-06-2009"

print(birth_day)

# deletes given key value from the list , specifying key is mandatory
# poped value can be stored in a variable
x = birth_day.pop("Sheela")

print(birth_day)
print(x)

# deletes given last 'key value' from the list  by default , no need to specify key
birth_day.popitem()
print(birth_day)

# 3rd method to delete element from dictionary is using del keyword
# values deleted using del cannot be stored in any variable
del birth_day["Soujanya"]

print(birth_day)

# used to add new item to existing dictionary
birth_day.update({"New": "10-10-2024"})
print(birth_day)

new1 = {"bat": "used to hit", "ball": "used to ball"}
# used to add new dictionary elements to existing dictionary

birth_day.update(new1)
print(birth_day)

# how to fetch only key list

print(birth_day.keys())

# how to fetch only value list

print(birth_day.values())

# items method is used to convert key value pair into a tuple and return list of elements

print(birth_day.items())

#this gives error as we are uisng set as key
# birth = {
#     2: 8, 1: 3 , (3,):1 , {1}:"hello", "h":"hellow", 'l':[1,2,3]
# }
# print(birth)

# how easy it is to access elements in dictionary
item1 = {
    "Sugar":1 ,
"price":20
}

item2 = {
    "Tea":1 ,
"price":40
}

print(f"{item1["price"]  + item2["price"]}")