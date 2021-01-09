import random

def randInt(min=0,max=100):
    minVariable = 100-min 
    maxVariable = max-1
    if(min==0 and max==100):
        num=random.random() * 100
        print("min==0 max==100 is run")
    elif(min>0 and max==100):
        num=random.random() * minVariable + min
        print("when you have something in min")
    elif(min==0 and max<100):
        num=random.random()*maxVariable
        print("when you have something in max")
    else:
        num=random.random()*max+min
        print("when you have something 2 in there")    
    return round(num)

print(randInt(),"\n") 		    # should print a random integer between 0 to 100
print(randInt(max=50),"\n") 	    # should print a random integer between 0 to 50
print(randInt(min=50),"\n") 	    # should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

    