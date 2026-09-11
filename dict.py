#creating a dictionary

# mydict = {"student": "John", "age":20,"grade":"B","subject":["Math","English"]}
# print(mydict)


# #accessing items from dictionary
# print(mydict["subject"])
# print(mydict["subject"][0])  #prints the first item from the list in the dictionary
# print(mydict.get("age")) #accessing the value of the key using get() method
# print(mydict.keys()) #print all the keys from the dictionary in the list format
# print(mydict.values()) #print all the values from the dictionary in the list format
# print(mydict.items()) #print all the items from the dictionary in the list format but key value pair is in tuple format

# here if we repeat the key in the dictionary then it will not give any error but it will take the lastest value of the key
#mydict = {"student": "John", "age":20,"grade":"B","subject":["Math","English"],"student":"shreya"} o/p-dict_values(['shreya', 20, 'B', ['Math', 'English']])

#check if key exists in the dictionary can't check values exists or not 

# if "age" in mydict:
#     print("yes age exists")
# else:
#     print("does not exist")    


#adding the new items 

mydict = {"student": "John", "age":20,"grade":"B","subject":["Math","English"]}
# mydict["marks"]=70
# print(mydict)
# mydict.update({"marks": 75})
mydict ["subject"].append("kannada")
print(mydict)

#removing the items

# mydict = {"student": "John", "age":20,"grade":"B","subject":["Math","English"]}
# #mydict.pop("grade") #delete the key which is passed
# #mydict.popitem() #delete last key
# del mydict # delete entire dictionary 
# print(mydict) #after deletion we get name error

#copying the dictionary

# mydict = {"student": "John", "age":20,"grade":"B","subject":["Math","English"]}

# mydict1= mydict.copy()
# print(mydict)
# print(mydict1)


# looping the dictionary
# mydict = {"student": "John", "age":20,"grade":"B","subject":["Math","English"]}
# for x in mydict:
#     print(x)
  

# for x in mydict.keys():
#      print(x)

# for x in mydict.values():
#      print(x)

# for x in mydict:
#     print(mydict[x])  

# for x,y in mydict.items():
#     print(x,y)