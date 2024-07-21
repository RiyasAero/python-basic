#Create a dictionary
my_dict = {'m5cs':'bmw', 'continental gt':'bentley', 'spectre':'RR','carrera':'porsche'}
print(my_dict)

#Adding a new pair value
my_dict['EQC']= 'mercedes'
print(my_dict)

#Updating a value
my_dict['RR']= 'ghost'
print(my_dict)

#Deleting a value
del my_dict['carrera']
print(my_dict)

# Checking if a key exists
if "m5cs is in dictionary":
    print("m5cs is in the dictionary")
else:
    print("m5cs is not in the dictionary")

#Clearing all values
my_dict.clear()
print(my_dict)

