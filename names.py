#Printing a few names in a list
names = ['Ruby', 'Jude', 'Daniella', 'Emmanuella']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
#del names[]
#print(names)

#Printing a message to each name
message = names[0] + ", you are blessed."
print(message)
message = names[1] + ", you are blessed."
print(message)
message = names[2] + ", you are blessed."
print(message)
message = names[3] + ", you are blessed."
print(message)

#Printing models of cars in a statement
fav_models = ['Toyota fortuner', 'Mahindra XUV', 'Honda CR-V', 'Hyundai Tucson', 'Renault Captur']
message = "I own a " + fav_models[0] + " car."
print(message)
message = "I own a " + fav_models[1] + " car."
print(message)
message = "I own a " + fav_models[2] + " car."
print(message)
message = "I own a " + fav_models[3] + " car."
print(message)
message = "I own a " + fav_models[4] + " car."
print(message)



motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop() 
print(motorcycles)
print(popped_motorcycle)
last_owned = motorcycles.pop() 
print("The last motorcycle I owned was a " + last_owned.title() + ".")