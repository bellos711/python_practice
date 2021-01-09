# print("Halo World")

# name = "Kahlil"

# print(f"Hello, what it d0 {name} ?")
# print("Hello, what it d0 {} ?".format(name))
# print("Hello, what it d0 %s ?" % (name))
# print("Hello " + name)

# 1. TASK: print "Hello World"copy
print("Halo World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Kahlil"
print( "Hello ", name )	# with a comma
print("Hello " + (name))	# with a +
# 3. print "Hello 42!" with the number in a variable
num = 42
print( "Hello ", num )	# with a comma
print("Hello " + str(num))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}".format(fave_food1,fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string