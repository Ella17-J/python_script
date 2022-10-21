from sqlite3 import adapt

#This program outputs names either in title case, upper case and lower case letters 
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#concatenation
first_name = "Ada"
last_name = "Lovelace"
full_name = "Ada" + " " + "Lovelace"
message = "Hello, " +  full_name.title() + "!"
print(message)