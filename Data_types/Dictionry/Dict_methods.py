"""
#create an empty dict
dict1 = {}
print(type(dict1))

#or using dict function
dict1 = ({ 1: "one", 2: "two", 3: "three"})
dict2  = { 1: "one", 2: "two", 3: "three"}
print(type(dict1), type(dict2))

# or creating dictionary using each item as a pair

#dict3 = dict({[1, "hello"], [2 , "hi"]})  # TypeError: unhashable type: 'list'
dict4 = {(1, "hello"), (2 , "hi")}  #it take as a set
#print(dict3, type(dict3))
print(dict4, type(dict4))

dict5 = dict({(1, "hello"), (2 , "hi")})
dict6 = dict([(1, "hello"), (2 , "hi")])
print(dict5, type(dict5))
print(dict6, type(dict6))

list1 = [1, 2, 3]
set1 = {1, 2, 3}
tuple1 = (1, 2, 3)
string = "geeks for geeks"
dics = {1: "one"}
#dict7 = {list1: 1} #TypeError: unhashable type: 'list'
#dict7 = {set1 : 1} #TypeError: unhashable type: 'set'
dict7 = {tuple1 : 1}
dict7 = {string : 1}
#dict7 = {dics : 1} #TypeError: unhashable type: 'dict'

print("dict7 = ", dict7)

#nested dictionary
nest_dict = {1: "one", 2: {"A":"welcome", "B": "To"}}

for key,values in nest_dict.items():
    if type(values) is dict:
        for nest_key, nest_values in values.items():
            print(nest_key, nest_values)
    else:
        print(key, values)
print()
#or accessing an element using key
print("using key of the dictionry")
print(nest_dict[1])
print(nest_dict[2])
print(nest_dict[2]["A"])
print(nest_dict[2]["B"])
#print(nest_dict[3])  #key error
print()

# access the element using get method
#1. get method
print("using get method")
print(nest_dict.get(1))
print(nest_dict.get(2))
print(nest_dict.get(3))  # it returns none if the key is not existing
print(nest_dict.get(3,  "key not found"))
print("-----------------------------------")
print(nest_dict.get(2, {}).get("A"))
print()

# or Adding an element using key

dict_var = {1 : "A"}
dict_var[2] = "B"
dict_var[3] = "C"
#adding a set of values
dict_var[4] = 2, 3, 4
# Adding Nested Key value to Dictionary
dict_var[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print(dict_var)
print(dict_var[4], type(dict_var[4]))
"""
#2. clear

dict_var = {1 : 'one', 2: 'two'}
dict_var.clear()
print(dict_var)

#3. copy

dict_var = {1 : 'one', 2: 'two'}
dict_var_cpy = dict_var.copy()
print(dict_var_cpy)
if dict_var == dict_var_cpy:
    print("both dict are same")

#4. pop
dict_var = {1 : 'one', 2: 'two'}
print(dict_var.pop(1)) #need to pass the key
#print(dict_var.pop(3)) #gives key error if key not present
print(dict_var.pop(3, "key not found"))#default value is optional if key not present it returns default value which is none
print(dict_var.pop(3, 1))  #it takes default value of any data type
print(dict_var)

#5. popItems - it return the tuple containing the key-value pair from dictionary. That pair is removed from dictionary.
dict_var = {1 : 'one', 2: 'two'}
dict_var.popitem()
dict_var.popitem()
print(dict_var)

#6. items
dict_var = {1 : 'one', 2: 'two'}

print(dict_var.items(), type(dict_var.items())) #- it returns the list of key, value pair tuple

#7. keys
dict_var = {1 : 'one', 2: 'two'}
print(dict_var.keys())   #list of keys

#8. values
dict_var = {1 : 'one', 2: 'two'}
print(dict_var.values()) #list of values

#9. fromkeys() - to create a dictionary
dict1 = dict.fromkeys((1,2,4), "value")
dict2 = dict.fromkeys((1, 2, 3), [2, 3])
print(dict1)
print(dict2)

list1 = [1, 2, 3]
dict1 = {1 : list1}
list1.append(4)
print(dict1)

#10. setdefault
dict_var = {1 : 'one', 2: 'two'}
dict_var.setdefault(" ", "oneone")
print(dict_var)
print(dict_var.setdefault(1, "three"))
print(dict_var) # when we use method existing key, it’ll return the value of the existing key, but will not modify the dictionary key.


#11. update
dict_var1 = {1 : 'one', 2: 'two'}
dict_var2 = {3 : "three", 4: "four"}
dict_var1.update(dict_var2)
print(dict_var1)

#12. haskey  -returns true if key present else false
dict_var1 = {1 : 'one', 2: 'two'}
#print(dict_var.has_key(1))   # this metjod has removed from python 3



