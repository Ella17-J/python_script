#Printing range of numbers 
for value in range(1,11):
    print(value)

numbers = list(range(1,11))
print(numbers)

#printing odd numbers in the list
odd_numbers = list(range(1,11,2))
print(odd_numbers)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#minimum,maximum and sum of digits
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
min(digits)
max(digits)
sum(digits)