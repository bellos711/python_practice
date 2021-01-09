# Update Values in Dictionaries and Lists
x = [ [5,2,3], [15,8,9] ] #x[1][0] = 15
students = [
     {'first_name':  'Michael', 'last_name' : 'Bryant'}, #students[0]['last_name'] = Bryant
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'], 
    'soccer' : ['Andres', 'Ronaldo', 'Rooney'] #sports_directory['soccer'][0] = "Andres"
}
z = [ {'x': 10, 'y': 30} ] #z[0]['y'] = 30
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30


students2 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
#2
# Create a function iterateDictionary(some_list) that, given a list of dictionaries,
# the function loops through each dictionary in the list and prints each key and the associated value.
# For example, given the following list:

def iterateDictionary(some_list):
    for dict_items in some_list:
        for keys in dict_items:
            print(f"{keys} - {dict_items[keys]}", end=", ")  
               
        print(" ")
iterateDictionary(students2)
print("\n###########################################\n")

#3
# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
print("\First Names:")
def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(f"{item[key_name]} ")

iterateDictionary2('first_name', students2)
print("\nLast Names:")
iterateDictionary2('last_name', students2)


print("\n##############################\n")
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_list):
    locationCount = len(some_list['locations'])
    print(locationCount, "LOCATIONS")
    for item in some_list['locations']:
        print(item)
        

    instructorCount = len(some_list['instructors'])
    print("\n",instructorCount, "INSTRUCTORS")
    for item in some_list['instructors']:
        print(item)
        
 
printInfo(dojo)
